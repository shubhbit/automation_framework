from behave import *
import os
import logging
import re
import copy

from src.steps.common_utility.common_utility import APICommonFunctions


_module = os.path.basename(__file__)


def get_logger(context, module):
    return logging.getLogger(context.logger_name + '.' + module)


@When('user creates an employee with name as "{name}" salary as "{salary}" and age as "{age}"')
def step_impl(context, name, salary, age):
    """
    Keyword implementation for Employee registration
    :param context: context variable
    :param name: name of the employee to be registered
    :param salary: salary of employee
    :param age: age of employee
    :return: None
    """
    try:
        emp_info = {'name': name,
                    'salary': salary,
                    'age': age}
        print("Employee info: ", emp_info)
        emp_mgmt = APICommonFunctions(context)
        emp_info = emp_mgmt.populate_employee_json(emp_info)
        context.input_emp = emp_info
        response = context.emp_obj.register_employee(emp_info)
        context.output_info = response
        context.emp_obj.compare_emp_info(emp_info, response)
        print("created: ", response)
        get_logger(context, _module).debug('Employee registred: ', response)

    except Exception as e:
        get_logger(context, _module).error('Employee registration failed: ', e)


@Then('user can verify employee is registered')
def step_impl(context):
    """
    Keyword implementation for verification wehther employee was registred successfully with given information
    :param context: context variable
    :return: None
    """
    try:
        emp_mgmt = APICommonFunctions(context)
        response = context.emp_obj.get_employee(context.output_info['id'])
        context.emp_obj.compare_emp_info(context.output_info, response)
        get_logger(context, _module).debug('Employee is fetched and matched: ', response)
        print("macthed: ", response)

    except Exception as e:
        get_logger(context, _module).error('Employee is not fetched or match failed: ', e)





