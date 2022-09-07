#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

#
# This is an example "local" configuration file. In order to set/override config
# options that ONLY apply to your local environment, simply copy/rename this file
# to docker/pythonpath/superset_config_docker.py
# It ends up being imported by docker/superset_config.py which is loaded by
# superset/config.py
#

APP_NAME = "TREC Dev"

DEFAULT_FEATURE_FLAGS = {
    # allow dashboard to use sub-domains to send chart request
    # you also need ENABLE_CORS and
    # SUPERSET_WEBSERVER_DOMAINS for list of domains
    "ALLOW_DASHBOARD_DOMAIN_SHARDING": True,
    # Experimental feature introducing a client (browser) cache
    "CLIENT_CACHE": False,
    "DISABLE_DATASET_SOURCE_EDIT": False,
    # When using a recent version of Druid that supports JOINs turn this on
    "DRUID_JOINS": False,
    "DYNAMIC_PLUGINS": False,
    # With Superset 2.0, we are updating the default so that the legacy datasource
    # editor no longer shows. Currently this is set to false so that the editor
    # option does show, but we will be depreciating it.
    "DISABLE_LEGACY_DATASOURCE_EDITOR": True,
    # For some security concerns, you may need to enforce CSRF protection on
    # all query request to explore_json endpoint. In Superset, we use
    # `flask-csrf <https://sjl.bitbucket.io/flask-csrf/>`_ add csrf protection
    # for all POST requests, but this protection doesn't apply to GET method.
    # When ENABLE_EXPLORE_JSON_CSRF_PROTECTION is set to true, your users cannot
    # make GET request to explore_json. explore_json accepts both GET and POST request.
    # See `PR 7935 <https://github.com/apache/superset/pull/7935>`_ for more details.
    "ENABLE_EXPLORE_JSON_CSRF_PROTECTION": False,
    "ENABLE_TEMPLATE_PROCESSING": True,
    "ENABLE_TEMPLATE_REMOVE_FILTERS": False,
    # Allow for javascript controls components
    # this enables programmers to customize certain charts (like the
    # geospatial ones) by inputing javascript in controls. This exposes
    # an XSS security vulnerability
    "ENABLE_JAVASCRIPT_CONTROLS": False,
    "KV_STORE": False,
    # When this feature is enabled, nested types in Presto will be
    # expanded into extra columns and/or arrays. This is experimental,
    # and doesn't work with all nested types.
    "PRESTO_EXPAND_DATA": False,
    # Exposes API endpoint to compute thumbnails
    "THUMBNAILS": False,
    "DASHBOARD_CACHE": False,
    "REMOVE_SLICE_LEVEL_LABEL_COLORS": False,
    "SHARE_QUERIES_VIA_KV_STORE": False,
    "TAGGING_SYSTEM": False,
    "SQLLAB_BACKEND_PERSISTENCE": True,
    "LISTVIEWS_DEFAULT_CARD_VIEW": False,
    # When True, this flag allows display of HTML tags in Markdown components
    "DISPLAY_MARKDOWN_HTML": True,
    # When True, this escapes HTML (rather than rendering it) in Markdown components
    "ESCAPE_MARKDOWN_HTML": False,
    "DASHBOARD_NATIVE_FILTERS": True,
    "DASHBOARD_CROSS_FILTERS": False,
    # Feature is under active development and breaking changes are expected
    "DASHBOARD_NATIVE_FILTERS_SET": False,
    "DASHBOARD_FILTERS_EXPERIMENTAL": False,
    "GLOBAL_ASYNC_QUERIES": False,
    "VERSIONED_EXPORT": True,
    "EMBEDDED_SUPERSET": False,
    # Enables Alerts and reports new implementation
    "ALERT_REPORTS": False,
    "DASHBOARD_RBAC": True,
    "ENABLE_EXPLORE_DRAG_AND_DROP": True,
    "ENABLE_FILTER_BOX_MIGRATION": False,
    "ENABLE_ADVANCED_DATA_TYPES": False,
    "ENABLE_DND_WITH_CLICK_UX": True,
    # Enabling ALERTS_ATTACH_REPORTS, the system sends email and slack message
    # with screenshot and link
    # Disables ALERTS_ATTACH_REPORTS, the system DOES NOT generate screenshot
    # for report with type 'alert' and sends email and slack message with only link;
    # for report with type 'report' still send with email and slack message with
    # screenshot and link
    "ALERTS_ATTACH_REPORTS": True,
    # FORCE_DATABASE_CONNECTIONS_SSL is depreciated.
    "FORCE_DATABASE_CONNECTIONS_SSL": False,
    # Enabling ENFORCE_DB_ENCRYPTION_UI forces all database connections to be
    # encrypted before being saved into superset metastore.
    "ENFORCE_DB_ENCRYPTION_UI": False,
    # Allow users to export full CSV of table viz type.
    # This could cause the server to run out of memory or compute.
    "ALLOW_FULL_CSV_EXPORT": False,
    "UX_BETA": False,
    "GENERIC_CHART_AXES": True,
    "ALLOW_ADHOC_SUBQUERY": False,
    "USE_ANALAGOUS_COLORS": True,
    "DASHBOARD_EDIT_CHART_IN_NEW_TAB": False,
    # Apply RLS rules to SQL Lab queries. This requires parsing and manipulating the
    # query, and might break queries and/or allow users to bypass RLS. Use with care!
    "RLS_IN_SQLLAB": False,
    # Enable caching per impersonation key (e.g username) in a datasource where user
    # impersonation is enabled
    "CACHE_IMPERSONATION": False,
}

EXTRA_CATEGORICAL_COLOR_SCHEMES = [
    {
        "id": 'FiscalQuarters',
        "description": '',
        "label": 'Fiscal Quarters',
        "isDefault": True,
        "colors":
         ['blue', 'red', '#00FF00', 'gold']
    },
    {
        "id": 'BestPracticeUse',
        "description": '',
        "label": 'Best Practice Use',
        "isDefault": True,
        "colors":
         ['#FF0000', '#0000FF', '#00FF00']
    },
    {
        "id": '5Barplot',
        "description": '',
        "label": '5Barplot',
        "isDefault": True,
        "colors":
         ['#BFEFFF', '#00BFFF', 'blue', 'red', '#00FF00']
    },
    {
        "id": 'Burnout',
        "description": '',
        "label": 'Burnout',
        "isDefault": True,
        "colors":
         ['#00CD00', '#FFFF00', '#FF0000']
    },
    {
        "id": 'ScatterPlot',
        "description": '',
        "label": 'Scatter Plot',
        "isDefault": True,
        "colors":
         ['#EE0000', '#00CD66']
    },
    {
        "id": '3Barplot',
        "description": '',
        "label": '3Barplot',
        "isDefault": True,
        "colors":
         ['blue', 'red', 'lime']
    },
]

