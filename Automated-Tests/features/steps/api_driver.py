import configparser
from features.steps.util import *
import unittest
import json

tester = unittest.TestCase()

class ApiDriver(object):
    @staticmethod
    def userdata(parameter, configfile="behave.ini", section="behave.userdata"):
        userdata = configparser.ConfigParser()
        userdata.read(configfile)
        return userdata[section][parameter]

    def __init__(self, context=None, username="", password=""):
        if context:
            print("running ", context.config.userdata['env'] , "environment")
            environment = context.config.userdata['env']
            userdata = json.loads(context.config.userdata[environment])
            self.base_url =  userdata["base_url"]
            self.username = userdata["username"]


