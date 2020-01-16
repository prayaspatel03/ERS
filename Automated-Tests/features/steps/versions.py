from util import *
from behave import *
from features.steps.api_driver import *
import os
import json

versions_id = ""

@given(u'Set Versions id-"{versions}"')
def step_impl(context,versions):
    global versions_id
    versions_id = versions

@when(u'Show all Versions')
def step_impl(context):
    endpoint = versions_id
    response = GET(endpoint=endpoint)
    tester.assertEqual(response.status_code, 200)