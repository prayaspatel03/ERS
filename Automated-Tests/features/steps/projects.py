from util import *
from behave import *
from features.steps.api_driver import *
import os
import json
import time

projects_id = ""
ProjectID = ""

@given(u'Set Projects id-"{projects}"')
def step_impl(context,projects):
    global projects_id
    projects_id = projects


@when(u'Show all stored Projects')
def step_impl(context):
    endpoint = projects_id
    response = GET(endpoint=endpoint)
    tester.assertEqual(response.status_code, 200)

@when(u'Show all Projects via If-None-Match')
def step_impl(context):
    endpoint = projects_id
    headers = {'If-None-Match': "FD7441CAB90E00A1E1A5B5AB5AF02024976F23411834C9D056506FD19B622A3C"}
    response = GET(endpoint=endpoint,headers=headers)
    tester.assertEqual(response.status_code, 200)

@when(u'Show all Projects via If-None-Match and X-Long-Polling')
def step_impl(context):
    endpoint = projects_id
    headers = {'If-None-Match': "FD7441CAB90E00A1E1A5B5AB5AF02024976F23411834C9D056506FD19B622A3C",
        'X-Long-Polling': "100"}
    response = GET(endpoint=endpoint,headers=headers)
    tester.assertEqual(response.status_code, 200)

@when(u'POST project using "{sample_project_path}"')
def step_impl(context,sample_project_path):
    global ProjectID
    endpoint = projects_id
    sample_project_path = os.path.join(os.path.abspath('.'), sample_project_path)
    print(os.path.abspath('.'))
    headers = {'Content-type': 'application/json'}

    with open(sample_project_path, 'r+') as file:
        data = json.load(file)
        jfile=json.dumps(data)
        response = POST(context.api_driver.base_url, endpoint=endpoint,headers=headers,data=jfile)
        ProjectID = response.text
        #tester.assertEqual(response.status_code, 201)
        tester.assertIn(response.status_code, [200,201])



@when(u'Show new project using ID')
def step_impl(context):
    endpoint = projects_id +'/'+ProjectID
    response = GET(endpoint=endpoint)
    tester.assertEqual(response.status_code, 200)

@when(u'Show new project via If-None-Match')
def step_impl(context):
    endpoint = projects_id +'/'+ProjectID
    headers = {'If-None-Match': "FD7441CAB90E00A1E1A5B5AB5AF02024976F23411834C9D056506FD19B622A3C"}
    response = GET(endpoint=endpoint,headers=headers)
    #tester.assertEqual(response.status_code, 200)
    tester.assertIn(response.status_code, [200,201])

@when(u'Delete new project using ID')
def step_impl(context):
    endpoint = projects_id +'/'+ProjectID
    response = DELETE(endpoint=endpoint)
    tester.assertEqual(response.status_code, 200)