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
       from connect_basemaps import get_basemaps
       MAP_BASELAYERS = get_basemaps('add-api-key')
   except ImportError:
       pass
