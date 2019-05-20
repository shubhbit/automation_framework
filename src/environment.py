import logging
import os
import re
import requests
import string
import time
import configparser

import src.steps.Employee_APIs.employees as Employee

def initialise_logger(context, feature):
    folder = context.config.userdata.get('logs_folder')

    log_file = folder + feature.tags[0] + '.log'

    # Create logger
    context.logger_name = 'test_framework'
    context.logger = logging.getLogger(context.logger_name)
    context.logger.setLevel(logging.DEBUG)

    # Create file handler
    context.log_file_handler = logging.FileHandler(log_file)
    context.log_file_handler.setLevel(logging.DEBUG)

    # Create console handler
    context.log_console_handler = logging.StreamHandler()
    context.log_console_handler.setLevel(logging.ERROR)

    # Create formater and add to handlers
    formatter = logging.Formatter(context.config.userdata.get('logs_format'))
    context.log_file_handler.setFormatter(formatter)
    context.log_console_handler.setFormatter(formatter)

    # Add the handlers to the logger.
    context.logger.addHandler(context.log_file_handler)
    context.logger.addHandler(context.log_console_handler)
    context.logger.debug('##### Logger created #####')


def before_feature(context, feature):
    config_parser = configparser.ConfigParser(interpolation=EnvInterpolation())
    config_parser.read(['./configs/config.ini'])
    parsed_configs_list = [dict(config_parser.items(section)) for section in config_parser.sections()]
    custom_configs = {k: v for d in parsed_configs_list for k, v in d.items()}
    context.config.userdata = {**context.config.userdata, **custom_configs}
    initialise_logger(context, feature)
    context.logger.debug(' ######  Feature Started:  %s' % feature.name)
    context.emp_obj = Employee.Employee(context)


def after_feature(context, feature):
    context.logger.debug(' ######  Feature end:  %s' % feature.name)
    # Deleting created objects if any



def before_scenario(context, scenario):
    context.logger.debug(' ######  Scenario start: %s' % scenario.name)

def after_scenario(context, scenario):
    context.logger.debug(' ######  Scenario end: %s' % scenario.name)
    context.logger.debug(' ######  cleanup ######')

    if len(context.emp_list) != 0:
        for i in context.emp_list:
            context.emp_obj.delete_employee(i['id'])
            context.logger.debug(' ######  deleted:  {}######'.format(i['id']))

class EnvInterpolation(configparser.BasicInterpolation):
    """Interpolation which expands environment variables in values."""
    def before_get(self, parser, section, option, value, defaults):
        return os.path.expandvars(value)


