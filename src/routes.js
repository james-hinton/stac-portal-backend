/**
=========================================================
* Material Dashboard 2 React - v2.1.0
=========================================================
* Product Page: https://www.creative-tim.com/product/material-dashboard-react
* Copyright 2022 Creative Tim (https://www.creative-tim.com)
Coded by www.creative-tim.com
 =========================================================
* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
*/
/** 
  All of the routes for the Material Dashboard 2 React are added here,
  You can add a new route, customize the routes and delete the routes here.
  Once you add a new route on this file it will be visible automatically on
  the Sidenav.
  For adding a new route you can follow the existing routes in the routes array.
  1. The `type` key with the `collapse` value is used for a route.
  2. The `type` key with the `title` value is used for a title inside the Sidenav. 
  3. The `type` key with the `divider` value is used for a divider between Sidenav items.
  4. The `name` key is used for the name of the route on the Sidenav.
  5. The `key` key is used for the key of the route (It will help you with the key prop inside a loop).
  6. The `icon` key is used for the icon of the route on the Sidenav, you have to add a node.
  7. The `collapse` key is used for making a collapsible item on the Sidenav that has other routes
  inside (nested routes), you need to pass the nested routes inside an array as a value for the `collapse` key.
  8. The `route` key is used to store the route location which is used for the react router.
  9. The `href` key is used to store the external links location.
  10. The `title` key is only for the item with the type of `title` and its used for the title text on the Sidenav.
  10. The `component` key is used to store the component of its route.
*/
// Material Dashboard 2 React layouts
import Dashboard from "layouts/dashboard";

// STAC Portal pages
import PublicSources from "pages/PublicSources/PublicSources";
import Validator from "pages/Validator/Validator";
import AreaDownloader from "pages/AreaDownloader/AreaDownloader";
import Settings from "pages/Settings/Settings";
import Applications from "pages/Applications/Applications";
import Uploader from "pages/Uploader/Uploader";
import Searcher from "pages/Searcher/Searcher";
// @mui icons
import Icon from "@mui/material/Icon";
const routes = [
  {
    type: "title",
    title: "Analytics",
  },
  {
    type: "collapse",
    name: "Dashboard",
    key: "dashboard",
    icon: <Icon fontSize="small">dashboard</Icon>,
    route: "/dashboard",
    component: <Dashboard />,
  },

  {
    type: "title",
    title: "Import",
  },
  {
    type: "collapse",
    name: "Uploader",
    key: "uploader",
    icon: <Icon fontSize="small">cloud_upload</Icon>,
    route: "/upload",
    component: <Uploader />,
  },

  {
    type: "collapse",
    name: "Downloader",
    key: "downloader",
    icon: <Icon fontSize="small">cloud_download</Icon>,
    route: "/area-downloader",
    component: <AreaDownloader />,
  },
  {
    type: "collapse",
    name: "Searcher",
    key: "searcher",
    icon: <Icon fontSize="small">search</Icon>,
    route: "/searcher",
    component: <Searcher />,
  },

  {
    type: "collapse",
    name: "Updater",
    key: "updater",
    icon: <Icon fontSize="small">update</Icon>,
    route: "/updater",
    component: "",
  },
  {
    type: "title",
    title: "Utilities",
  },
  {
    type: "collapse",
    name: "Validator",
    key: "validator",
    icon: <Icon fontSize="small">verified_user</Icon>,
    route: "/validator",
    component: <Validator />,
  },
  {
    type: "collapse",
    name: "Public Sources",
    key: "public-sources",
    icon: <Icon fontSize="small">public</Icon>,
    route: "/public-sources",
    component: <PublicSources />,
  },

  {
    type: "collapse",
    name: "Building Blocks",
    key: "building-blocks",
    icon: <Icon fontSize="small">code</Icon>,
    route: "/applications",
    component: <Applications />,
  },
  {
    type: "collapse",
    name: "Settings",
    key: "settings",
    icon: <Icon fontSize="small">settings</Icon>,
    route: "/settings",
    component: <Settings />,
  },
];
export default routes;
