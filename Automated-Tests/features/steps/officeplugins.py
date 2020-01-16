from util import *
from behave import *
from features.steps.api_driver import *
import os
import json

officeplugin_id = ""

@given(u'Set OfficePlugin id-"{officeplugin}"')
def step_impl(context,officeplugin):
    global officeplugin_id
    officeplugin_id = officeplugin
    print(officeplugin_id)

@when(u'Show all OfficePlugin versions')
def step_impl(context):
    endpoint = officeplugin_id
    response = GET(endpoint=endpoint)
    context.status_code = response.status_code
    print(context.status_code)

@when(u'Show the OfficePlugin versions which are greater-than "{plugin_var}"')
def step_impl(context,plugin_var):
    endpoint = officeplugin_id
    response = GET(endpoint=endpoint,params="VERSION-Greater-Than="+plugin_var)
    context.status_code = response.status_code
    print(context.status_code)

@when(u'Post the new OfficePlugin version "{plugin_var}"')
def step_impl(context,plugin_var):
    endpoint = officeplugin_id
    data="{\"VERSION\": \""+plugin_var+"\",\n    \"Release-Notes\": \"not much changed\"}"
    print(data)
    response = POST(context.api_driver.base_url, endpoint=endpoint, data=data)
    context.status_code = response.status_code
    print(context.status_code)

@when(u'Delete the OfficePlugin version "{plugin_var}"')
def step_impl(context,plugin_var):
    endpoint = officeplugin_id+'/'+plugin_var
    print(endpoint)
    response = DELETE(endpoint=endpoint)
    context.status_code = response.status_code
    print(context.status_code)