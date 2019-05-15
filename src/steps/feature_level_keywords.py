from behave import *
import os
import logging
import re
import copy
from requests import request

_module = os.path.basename(__file__)


def get_logger(context, module):
    return logging.getLogger(context.logger_name + '.' + module)


@given("the employee system is up and running")
def step_impl(context):
    response = request("GET", "http://dummy.restapiexample.com/api/v1/employees")
    assert response.status_code == 200

@Given('user is logged in')
def step_impl(context):
    pass