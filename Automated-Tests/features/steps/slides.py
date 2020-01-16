from util import *
from behave import *
from features.steps.api_driver import *
import os
import json
import unittest

tester = unittest.TestCase()
ProjectID = ""
SlideID = ""

@given(u'I POST project using')
def step_impl(context):
    print("---------------------1")
    print(context.api_driver.userdata('test'))
    print("username=",context.api_driver.username)
    print("base_url=",context.api_driver.base_url)
    print("---------------------2")
    for row in context.table:
        headers = {'Content-type': 'application/json'}
        global ProjectID
        sample_project_path = os.path.join(os.path.abspath('.'), "sample_files\SimpleProject1.json")
        print(sample_project_path)
        with open(sample_project_path, 'r+') as file:
            data = json.load(file)
            jfile=json.dumps(data)
            response = POST(context.api_driver.base_url, endpoint=row['endpoint'], data=jfile,headers=headers)
            ProjectID = response.text
            print(response.status_code)
            #tester.assertEqual(response.status_code, 200)

@when(u'I POST sample slide with same project ID that created using')
def step_impl(context):
    global SlideID
    for row in context.table:
        headers = {'Content-type': 'application/json'}
        sample_slide_path = os.path.join(os.path.abspath('.'), "sample_files\SimpleSlide1.json")
        with open(sample_slide_path, 'r+') as jsonFile:
            data = json.load(jsonFile)
            tmp = data["ProjectID"]
            data["ProjectID"] = ProjectID
            jsonFile.seek(0)  # rewind
            json.dump(data, jsonFile)
            jsonFile.truncate()
            jfile=json.dumps(data)
            response = POST(context.api_driver.base_url, endpoint=row['endpoint'], data=jfile,headers=headers )
            SlideID = response.text
            tester.assertEqual(response.status_code, 200)

@when(u'I GET newly added slide using end point GET "{slide}" and Slide ID')
def step_impl(context, slide):
    endpoint = slide + SlideID
    headers = {'Content-type': 'application/json'}
    response = GET(endpoint=endpoint,headers=headers)
    tester.assertEqual(response.status_code, 200)

