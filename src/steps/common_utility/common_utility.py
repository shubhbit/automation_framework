import ast
import random
import string
import logging
import src.steps.common_utility.helpers as helper
from dli.client import session
from enum import Enum
from datetime import date


class APICommonFunctions(object):
    def __init__(self, context):
        self.context = context

    def _type(self):
        return self.__class__.__name__

    def get_logger(self):
        return logging.getLogger(self.context.logger_name + '.' + self._type())

    def populate_employee_json(self, emp_info):
        try:
            emp_info = {**
            {'name': "auto_employee" + helper.random_word(10),
            'salary': helper.random_number(10000, 20000),
             'age': helper.random_number(20, 30)}, **emp_info}
            return emp_info
        except:
            raise

    def compare_emp_info(self, input_info, output_info):
        try:
            pass
        except:
            raise