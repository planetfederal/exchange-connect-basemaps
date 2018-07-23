========================
GeoNode Connect Basemaps
========================

*****************
OS Variables Used
*****************

- CONNECT_ENDPOINT: defaults to 'https://bcs.boundlessgeo.io'
- CONNECT_APIKEY: add your specific key
- CONNECT_VERSION: defaults to '0.1'
- CONNECT_IGNORE_MAPS: defaults to None

**Note:** CONNECT_IGNORE_MAPS needs to be a comma separated string

Example:

.. code-block:: bash

   export CONNECT_IGNORE_MAPS='Planet May-2018, Planet August-2017'

************
Installation
************

.. code-block:: bash

   pip install git+https://github.com/boundlessgeo/geonode-connect-basemaps@master#egg=geonode-connect-basemaps

*****************
Enable in Geonode
*****************

.. code-block:: bash

   export CONNECT_APIKEY=${ADD_API_KEY}
   export ADDITIONAL_APPS='connmaps,'