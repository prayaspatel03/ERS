from steps.util import *
from behave import *
from steps.api_driver import ApiDriver
import time
def before_all(context):
    # ON INIT context object gets initialized
    context.api_driver = ApiDriver(context=context)
    # Setting test mode is "true" using POST
    response = POST(context.api_driver.base_url, endpoint="/api/v1/Configuration/TestMode", data="true")
    context.status_code = response.status_code
    time.sleep(1)

def after_all(context):
    # Setting test mode is "false" using POST
    response = POST(context.api_driver.base_url, endpoint="/api/v1/Configuration/TestMode", data="false")
    context.status_code = response.status_code
