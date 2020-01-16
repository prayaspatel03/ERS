from util import *
from behave import *
from features.steps.api_driver import *
import os
import json
import unittest

tester = unittest.TestCase()
log_id = ""

@given(u'Set Log id-"{logs}"')
def step_impl(context,logs):
    global log_id
    log_id = logs


@when(u'Show all log entries, with all attributes')
def step_impl(context):
    endpoint = log_id
    response = GET(endpoint=endpoint)
    tester.assertEqual(response.status_code, 200)

@when(u'Show only log entries before "{log_date}"')
def step_impl(context,log_date):
    endpoint = log_id
    response = GET(endpoint=endpoint,params = "filter-Before="+log_date)
    tester.assertEqual(response.status_code, 200)


@when(u'Show only log entries which apply to object "{object_id}"')
def step_impl(context,object_id):
    endpoint = log_id
    response = GET(endpoint=endpoint,params = "filter-ObjectID="+object_id)
    tester.assertEqual(response.status_code, 200)
   

@when(u'Show all of "{user}" changes since "{log_date}"')
def step_impl(context,user,log_date):
    endpoint = log_id
    response = GET(endpoint=endpoint,params = "filter-User=PLATO\\"+user+"&filter-After="+log_date)
    tester.assertEqual(response.status_code, 200)

@when(u'Show only user and when attributes')
def step_impl(context):
    endpoint = log_id
    response = GET(endpoint=endpoint,params = "fresult-attribute=User&result-attribute=When")
    tester.assertEqual(response.status_code, 200)


@when(u'Create a new event')
def step_impl(context):
    endpoint = log_id
    data="{\n    \"Action\": \"Logout\"\n}"
    headers = {'Content-type': 'application/json'}
    response = POST(context.api_driver.base_url, endpoint=endpoint, data=data, headers=headers)
    tester.assertEqual(response.status_code, 200)
