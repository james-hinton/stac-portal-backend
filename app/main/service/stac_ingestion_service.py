import datetime
import json
from typing import Dict, Tuple, List

import requests
import sqlalchemy

from app.main.model.public_catalogs_model import PublicCatalog
from .. import db
from ..model.stac_ingestion_model import StacIngestionStatus, StoredSearchParameters


def get_all_stac_ingestion_statuses() -> List[Dict[any, any]]:
    a: StacIngestionStatus = StacIngestionStatus.query.all()
    for i in a:
        print("Newly stored collections are: ", i.newly_stored_collections)
    return [i.as_dict() for i in a]


def get_stac_ingestion_status_by_id(id: str) -> Dict[any, any]:
    a: StacIngestionStatus = StacIngestionStatus.query.filter_by(id=id).first()
    return a.as_dict()


def _make_stac_ingestion_status_entry(source_stac_api_url: str,
                                      target_stac_api_url: str,
                                      update: bool) -> (int, int):
    print("source_stac_api_url: ", source_stac_api_url)
    public_catalogue_entry: PublicCatalog = PublicCatalog.query.filter(
        PublicCatalog.url == source_stac_api_url).first()

    if public_catalogue_entry is None:
        raise ValueError("Target STAC API URL not found in public catalogs.")
    # stac_search_parameters: StoredSearchParameters = StoredSearchParameters()
    # stac_search_parameters.associated_catalog_id = public_catalogue_entry.id
    stac_ingestion_status: StacIngestionStatus = StacIngestionStatus()
    stac_ingestion_status.source_stac_api_url = source_stac_api_url
    stac_ingestion_status.target_stac_api_url = target_stac_api_url
    stac_ingestion_status.update = update
    stac_ingestion_status.time_started = datetime.datetime.utcnow()
    db.session.add(stac_ingestion_status)
    db.session.commit()
    return stac_ingestion_status.id, public_catalogue_entry.id


def ingest_stac_data_using_selective_ingester(parameters) -> [str, int]:
    source_stac_api_url = parameters['source_stac_catalog_url']
    target_stac_api_url = parameters['target_stac_catalog_url']
    update = parameters['update']
    status_id, associated_catalogue_id = _make_stac_ingestion_status_entry(
        source_stac_api_url, target_stac_api_url, update)

    try:
        stored_search_parameters = StoredSearchParameters()
        stored_search_parameters.associated_catalog_id = associated_catalogue_id
        stored_search_parameters.used_search_parameters = json.dumps(
            parameters)
        db.session.add(stored_search_parameters)
        db.session.commit()
    except sqlalchemy.exc.IntegrityError:
        pass
    finally:
        # roolback if there is an error
        db.session.rollback()

    parameters["callback_id"] = status_id
    parameters[
        "callback_endpoint"] = "http://172.17.0.1:5000/stac_ingestion/status/" + str(
        status_id)  # TODO: make this environment variable
    STAC_SELECTIVE_CLONER_ENDPOINT = "http://localhost:8888/ingest"  # TODO: this needs to accept CIDR range and try every ip
    # print(parameters)
    # make a post request to STAC_SELECTIVE_CLONER_ENDPOINT
    stac_selective_cloner_endpoint = requests.post(
        STAC_SELECTIVE_CLONER_ENDPOINT, json=parameters)
    # get http code from stac_selective_cloner_endpoint
    return stac_selective_cloner_endpoint.text, status_id


def set_stac_ingestion_status_entry(
        status_id: str, newly_stored_collections_count: int,
        newly_stored_collections: List[str], updated_collections_count: int,
        updated_collections: List[str], newly_stored_items_count: int,
        updated_items_count: int,
        already_stored_items_count: int) -> Tuple[Dict[any, any]]:
    # get StacIngestionStatus object with id = status_id
    a: StacIngestionStatus = StacIngestionStatus.query.get(status_id)
    # update the object
    a.newly_stored_collections_count = newly_stored_collections_count
    a.newly_stored_collections = ",".join(newly_stored_collections)
    a.updated_collections_count = updated_collections_count
    a.updated_collections = ",".join(updated_collections)
    a.newly_stored_items_count = newly_stored_items_count
    a.updated_items_count = updated_items_count
    a.already_stored_items_count = already_stored_items_count
    a.time_finished = datetime.datetime.utcnow()

    db.session.add(a)
    db.session.commit()
    return a.as_dict()


def update_all_collections() -> List[Tuple[str, int]]:
    # Todo: test this
    stored_search_parameters: [StoredSearchParameters] = StoredSearchParameters.query.all()
    return _run_ingestion_task_force_update(stored_search_parameters)


def update_specific_collections_via_catalog_id(catalog_id: int, collections: [str] = None) -> List[Tuple[str, int]]:
    # TODO : implement this
    pass


def update_specific_collections_via_catalog_url(catalog_url: str, collections: [str] = None) -> List[Tuple[str, int]]:
    # TODO : implement this
    pass


def _run_ingestion_task_force_update(stored_search_parameters: [StoredSearchParameters]) -> List[Tuple[str, int]]:
    responses_from_ingestion_microservice = []
    for i in stored_search_parameters:
        try:
            used_search_parameters = json.loads(i.used_search_parameters)
            used_search_parameters["update"] = True
            microservice_response, work_id = ingest_stac_data_using_selective_ingester(
                used_search_parameters)
            responses_from_ingestion_microservice.append(
                (microservice_response, work_id))
        except ValueError:
            pass
    return responses_from_ingestion_microservice


def remove_stac_ingestion_status_entry(
        status_id: str) -> Tuple[Dict[any, any]]:
    a: StacIngestionStatus = StacIngestionStatus.query.filter_by(
        id=status_id).first()
    db.session.delete(a)
    db.session.commit()
    return a.as_dict()
