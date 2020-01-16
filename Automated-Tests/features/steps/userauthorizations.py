from util import *
from behave import *
from features.steps.api_driver import *
import os
import json


userauthorizations_id = ""

@given(u'Set UserAuthorizations id-"{userauthorizations}"')
def step_impl(context,userauthorizations):
    global userauthorizations_id
    userauthorizations_id = userauthorizations


@when(u'Show all stored UserAuthorizations')
def step_impl(context):
    endpoint = userauthorizations_id
    response = GET(endpoint=endpoint)
    tester.assertEqual(response.status_code, 200)

@when(u'Show current authentication information, including username and privileges')
def step_impl(context):
    endpoint = userauthorizations_id+'/self'
    response = GET(endpoint=endpoint)
    tester.assertEqual(response.status_code, 200)

@when(u'Post the new user "{user_id}"')
def step_impl(context,user_id):
    endpoint = userauthorizations_id
    headers = {'Content-type': 'application/json'}
    data="{\n    \"UserName\": \""+user_id+"\",\n    \"AuthorizationLevel\": \"Admin\"\n}"
    response = POST(context.api_driver.base_url, endpoint=endpoint, headers=headers, data=data)
    tester.assertEqual(response.status_code, 201)

@when(u'Delete the user "{user_id}"')
def step_impl(context,user_id):
    endpoint = userauthorizations_id
    response = DELETE(endpoint=endpoint,params = "userId="+user_id)
    tester.assertEqual(response.status_code, 200)