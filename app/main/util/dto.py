from flask_restx import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })


class CollectionsDto:
    api = Namespace('collections', description='collection related operations')
    collection = api.model('collections', {
        'collection_id': fields.String(required=True, description='collection id'),
        'item_id': fields.String(required=True, description='item id'),
    })


class ValidateDto:
    api = Namespace('validate', description='validate related operations')
    validate = api.model('validate', {
        # takes a JSON object
        'json': fields.Raw(required=True, description='JSON object to validate'),
    })

class StacIngestionStatusDto:
    api = Namespace('stac_ingestion_status', description='stac ingestion status related operations')
    stac_ingestion_status = api.model('stac_ingestion_status', {
        'status_id': fields.String(required=False, description='status id'),
    })