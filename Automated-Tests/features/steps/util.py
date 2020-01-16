import configparser
import requests
import json
from behave import *
from requests.auth import HTTPBasicAuth

def POST(base_url=None, data=None, endpoint=None, headers=None, timeout=None, files=None):
    """A method to send an HTTP POST with our headers, and an Auth cookie"""
    print("POST action using URL '%s' and endpoint '%s'" %(base_url, endpoint))
    if endpoint is not None:
        return requests.post(base_url+endpoint, data=data, headers=headers, auth=HTTPBasicAuth("REGRESSION-TESTER",""), timeout=timeout, files=files)
    else:
        return requests.post(base_url, data=data, headers=headers, auth=HTTPBasicAuth("REGRESSION-TESTER",""), timeout=timeout, files=files)

def GET(endpoint,params=None,headers=None):
    """A method to send an http GET with our headers, and auth-cookies."""
    print("GET action using URL '%s' and endpoint '%s'" % (rest_url, endpoint))

    if endpoint is not None:
        response = requests.get(base_url+endpoint, headers=headers, auth=HTTPBasicAuth('REGRESSION-TESTER', ''),params=params)
        return response

def PUT(endpoint, data=None,headers=None):
    print("POST action using URL '%s' and endpoint '%s'" %(base_url, endpoint))
    response = requests.put(base_url + endpoint,data=data, headers=headers)
    return response

def AUTHENTICATE(user, password):
    payload = { "username": user, "password": password }
    response = requests.post(base_url + "/user/signin", headers=headers, data=json.dumps(payload))
    return response.cookies

def DELETE(endpoint,params=None):
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    if endpoint is not None:
        response = requests.delete(base_url + endpoint, headers= headers,auth=HTTPBasicAuth('REGRESSION-TESTER', ''), params=params)
        return response
