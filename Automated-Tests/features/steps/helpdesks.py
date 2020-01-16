from util import *
from behave import *
from features.steps.api_driver import *
import os
import json

helpdesks_id = ""

@given(u'Set helpdesks id-"{helpdesks}"')
def step_impl(context,helpdesks):
    global helpdesks_id
    helpdesks_id = helpdesks
    print(helpdesks_id)

@when(u'Show all helpdesks versions')
def step_impl(context):
    endpoint = helpdesks_id
    response = GET(endpoint=endpoint)
    context.status_code = response.status_code
    print(context.status_code)

@when(u'Show the helpdesks versions which are greater-than "{helpdesk_var}"')
def step_impl(context,helpdesk_var):
    endpoint = helpdesks_id
    response = GET(endpoint=endpoint,params="VERSION-Greater-Than="+helpdesk_var)
    context.status_code = response.status_code
    print(context.status_code)

@when(u'Post the new helpdesks version "{helpdesk_var}"')
def step_impl(context,helpdesk_var):
    endpoint = helpdesks_id
    data="{\"VERSION\": \""+helpdesk_var+"\",\n    \"Release-Notes\": \"not much changed\"}"
    print(data)
    response = POST(context.api_driver.base_url, endpoint=endpoint, data=data)
    context.status_code = response.status_code
    print(context.status_code)

@when(u'Delete the helpdesks version "{helpdesk_var}"')
def step_impl(context,helpdesk_var):
    endpoint = helpdesks_id+'/'+helpdesk_var
    print(endpoint)
    response = DELETE(endpoint=endpoint)
    context.status_code = response.status_code
    print(context.status_code)