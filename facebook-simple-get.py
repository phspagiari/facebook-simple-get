#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Pedro H. Spagiari
#
# How to easily get an ACCESS_TOKEN:
# 1) https://developers.facebook.com
# 2) Create new App
# 3) https://developers.facebook.com/tools/accesstoken/
#
#
# Example:
# ID='464959100198059' (Ultra Music Festival Brazil)
# URI_PATH='attending' (See full attending list)


import requests
import json


GRAPH_URL = "https://graph.facebook.com"
ACCESS_TOKEN = ""
ID = ""
URI_PATH = ""


def get_recursively(resource_id, uri_path, access_token, data=[], next_url=None):
    if next_url is None:
        next_url = "%s/%s/%s?access_token=%s" % (GRAPH_URL, resource_id, uri_path, access_token)
    request = requests.get(next_url)
    json_result = request.json()
    data = data + json_result['data']
    if 'next' in json_result['paging'].keys():
        return get_recursively(
            resource_id=resource_id, uri_path=uri_path, access_token=access_token,
            data=data, next_url=json_result['paging']['next']
        )
    else:
        return data

result_data = get_recursively(resource_id=ID, uri_path=URI_PATH, access_token=ACCESS_TOKEN)
print(json.dumps(result_data))
