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

import json
import requests
from operator import itemgetter


def split_str_by_comma(str):
    """
    create a list from a string by splitting string using commas
    :param str: string
    :return: list
    """
    list = []
    if isinstance(str, basestring):
        for i in str.split(','):
            clean_i = i.strip()
            list.append(clean_i)

    return list


def get_baselayers(apikey, endpoint='https://bcs.boundlessgeo.io/',
                   version='1.0', ignore_maps='Recent Imagery',
                   default_map='Mapbox Streets', verify=True):
    """

    :param apikey: string
    :param endpoint: string (basemaps api endpoint)
    :param version: string (api version)
    :param ignore_maps: string (values of layers to ignore, comma separated)
    :param default_map: string (layer to have listed as first and visible)
    :return: list of geonode baselayer dicts
    """
    baselayers = []
    default = None
    imaps = split_str_by_comma(ignore_maps)
    url = ('{0}/basemaps?version={1}&apikey={2}').format(
        endpoint.strip('/'), version, apikey)
    maps = None
    response = requests.get(url=url, verify=verify)
    if response.status_code == 200:
        maps = json.loads(response.text)

    if maps:
        for map in maps:
            if map['name'] in imaps:
                continue
            url = '{0}?apikey={1}&version={2}'.format(
                map['endpoint'], apikey, version)
            # .pbf files are not currently supported
            if map['tileFormat'] == 'PBF':
                continue
            baselayer = {
                "source": {
                    "ptype": "gxp_olsource",
                },
                "type": "OpenLayers.Layer.XYZ",
                "args": [
                    "{}".format(map['name']),
                    [url],
                    {
                        "transitionEffect": "resize",
                        "attribution": "{}".format(map['attribution'])
                    }
                ],
                "name": "{}".format(map['name']),
                "fixed": True,
                "visibility": True if map['name'] == default_map else False,
                "group": "background"
            }
            if map['name'] == default_map:
                default = baselayer
            else:
                baselayers.append(baselayer)
    if len(baselayers) > 1:
        baselayers = sorted(baselayers, key=itemgetter('name'))
    baselayers[0] = {
        "source": {"ptype": "gxp_olsource"},
        "type": "OpenLayers.Layer",
        "args": ["No background"],
        "name": "background",
        "visibility": False,
        "fixed": True,
        "group": "background"
    }
    if default:
        baselayers[1] = default
    return baselayers
