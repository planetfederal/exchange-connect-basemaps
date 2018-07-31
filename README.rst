=========================
Exchange Connect Basemaps
=========================

************
Installation
************

.. code-block:: bash

   pip install git+https://github.com/boundlessgeo/exchange-connect-basemaps@master#egg=exchange-connect-basemaps

*************
Configuration
*************

Add the following to the bottom of your django settings.py file

.. code-block:: python

   try:
       from connect_basemaps import get_baselayers
       MAP_BASELAYERS = get_baselayers('add-api-key')
   except ImportError:
       pass

To get a list of available layers open the following url in a browser:

   https://bcs.boundlessgeo.io/basemaps?apikey={add-api-key}&version=0.1

Example response:

.. code-block:: javascript

   [{
       "name": "Planet January-2018",
       "attribution": "Planet 2018",
       "provider": "planet",
       "description": "Planet monthly mosaic from January of 2018",
       "endpoint": "https://bcs.boundlessgeo.io/basemaps/planet/2018_01/{z}/{x}/{y}.png",
       "accessList": ["bcs-basemap-planet"],
       "styleUrl": "NA",
       "standard": "XYZ",
       "tileFormat": "PNG",
       "thumbnail": null,
       "isPermitted": true
   }, {
       "name": "Planet July-2017",
       "attribution": "Planet 2018",
       "provider": "planet",
       "description": "Planet monthly mosaic from July of 2017",
       "endpoint": "https://bcs.boundlessgeo.io/basemaps/planet/2017_07/{z}/{x}/{y}.png",
       "accessList": ["bcs-basemap-planet"],
       "styleUrl": "NA",
       "standard": "XYZ",
       "tileFormat": "PNG",
       "thumbnail": null,
       "isPermitted": true
   }]


Full configuration example

.. code-block:: python

   api_key = 'not-a-real-api-key'
   specific_endpoint = 'https://bcs.boundlessgeo.io' # default
   specific_api_version = '0.1' # default
   maps_to_ignore_comma_separated_string = 'Recent Imagery, Planet August-2017' # default = 'Recent Imagery'
   default_map = 'Mapbox Streets' # default
   ssl_verify = True # default
   MAP_BASELAYERS = get_baselayers(
       api_key,
       endpoint=specific_endpoint,
       version=specific_api_version,
       ignore_maps=maps_to_ignore_comma_separated_string,
       default_map=default_map,
       verify=ssl_verify
   )

**Note:** if the api key is not valid the response will default to the following:

.. code-block:: python

   {
       "source": {"ptype": "gxp_olsource"},
       "type": "OpenLayers.Layer",
       "args": ["No background"],
       "name": "background",
       "visibility": False,
       "fixed": True,
       "group":"background"
   }, {
       "source": {"ptype": "gxp_osmsource"},
       "type": "OpenLayers.Layer.OSM",
       "name": "mapnik",
       "visibility": True,
       "fixed": True,
       "group": "background"
   }]
