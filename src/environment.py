import logging
import os
import re
import requests
import string
import time
import configparser

import src.steps.Employee_APIs.employees as Employee

def initialise_logger(context, feature):
    print(1)
    folder = context.config.userdata.get('logs_folder')
    print(2)

    log_file = folder + feature.tags[0] + '.log'
    print(3)

    # Create logger
    context.logger_name = 'test_framework'
    context.logger = logging.getLogger(context.logger_name)
    context.logger.setLevel(logging.DEBUG)
    print(4)

    # Create file handler
    context.log_file_handler = logging.FileHandler(log_file)
    context.log_file_handler.setLevel(logging.DEBUG)
    print(5)

    # Create console handler
    context.log_console_handler = logging.StreamHandler()
    context.log_console_handler.setLevel(logging.ERROR)
    print(6)

    # Create formater and add to handlers
    formatter = logging.Formatter(context.config.userdata.get('logs_format'))
    context.log_file_handler.setFormatter(formatter)
    context.log_console_handler.setFormatter(formatter)
    print(7)

    # Add the handlers to the logger.
    context.logger.addHandler(context.log_file_handler)
    context.logger.addHandler(context.log_console_handler)
    context.logger.debug('##### Logger created #####')
    print(8)


def before_feature(context, feature):
    config_parser = configparser.ConfigParser(interpolation=EnvInterpolation())
    config_parser.read(['./configs/config.ini'])
    parsed_configs_list = [dict(config_parser.items(section)) for section in config_parser.sections()]
    custom_configs = {k: v for d in parsed_configs_list for k, v in d.items()}
    context.config.userdata = {**context.config.userdata, **custom_configs}
    initialise_logger(context, feature)
    print(9)
    context.logger.debug(' ######  Feature Started:  %s' % feature.name)
    print(10)
    context.emp_obj = Employee.Employee(context)


def after_feature(context, feature):
    context.logger.debug(' ######  Feature end:  %s' % feature.name)


def before_scenario(context, scenario):
    context.logger.debug(' ######  Scenario start: %s' % scenario.name)

def after_scenario(context, scenario):
    context.logger.debug(' ######  Scenario end: %s' % scenario.name)

class EnvInterpolation(configparser.BasicInterpolation):
    """Interpolation which expands environment variables in values."""
    def before_get(self, parser, section, option, value, defaults):
        return os.path.expandvars(value)
