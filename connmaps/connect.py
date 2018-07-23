# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2018 Boundless Spatial
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

from django.conf import settings
import json
import os
import requests

#  get connect values from os environment variables
CONNECT_ENDPOINT = os.getenv('CONNECT_ENDPOINT', 'https://bcs.boundlessgeo.io/')
CONNECT_APIKEY = os.getenv('CONNECT_APIKEY', 'no-value-for-api-key')
CONNECT_VERSION = os.getenv('CONNECT_VERSION', '0.1')
CONNECT_IGNORE_MAPS = os.getenv('CONNECT_IGNORE_MAPS', None)

ignore_maps = []
if CONNECT_IGNORE_MAPS:
    for i in CONNECT_IGNORE_MAPS.split(','):
        clean_i = i.strip()
        ignore_maps.append(clean_i)

request_url = ('{0}/basemaps?apikey={1}&version={2}').format(
    CONNECT_ENDPOINT.strip('/'), CONNECT_APIKEY, CONNECT_VERSION)

maps = None
response = requests.get(url=request_url)
if response.status_code == 200:
    maps = json.loads(response.text)

if maps:
    for map in maps:
        if map['name'] in ignore_maps:
            continue
        url = '{0}?apikey={1}&version={2}'.format(
            map['endpoint'],
            CONNECT_APIKEY,
            CONNECT_VERSION
        ).replace('{-y}', '{y}') #  hotfix for some of the connect layers having a -y variable name
        # .pbf files are not supported in this ptype
        if '.pbf?apikey=' in url:
            continue
        BASEMAP = {
            'source': {
                'ptype': 'gxp_olsource',
                'url': url,
                'name': '{}'.format(map['name'])
            },
            'type': 'OpenLayers.Layer.XYZ',
            "args": [
                '{}'.format(map['name']),
                [url],
                {
                    'transitionEffect': 'resize',
                    'attribution': '{}'.format(map['attribution'])
                }
            ],
            'name': '{}'.format(map['name']),
            'fixed': True,
            'visibility': True,
            'group': 'background'
        }
        settings.MAP_BASELAYERS.append(BASEMAP)
