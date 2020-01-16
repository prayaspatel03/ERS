from util import *
from behave import *
from features.steps.api_driver import *
import os
import json
import unittest


@given(u'I GET Configuration "{configuration}"')
def step_impl(context,configuration):
    endpoint =configuration
    response = GET(endpoint=endpoint)
    context.status_code = response.status_code
    print(context.status_code)
