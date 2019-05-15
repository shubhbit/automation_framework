from requests import request
import logging
import random
import string
import time


class Employee(object):
    """
    Wrapper class to provide functionalities over Employee CRUD operations.
    """
    def __init__(self, context):
        self.context = context

    def register_employee(self, data):
        """
        method to create a new entry for an employee
        :return:
        """
        response = request("POST", create_url, json=data)
        assert response.status_code == 200
        return response.json()

    def update_employee(self, data):
        """
        method to edit existing employee record
        :return:
        """
        response = request("PUT", update_url, json=data)
        assert response.status_code == 200
        return response.json()

    def get_employee(self, id):
        """
        method to get an employee record
        :return:
        """
        response = request("GET", get_url)
        assert response.status_code == 200
        return response.json()

    def delete_employee(self):
        """
        method to delete an existing record
        :return:
        """
        response = request("DELETE", delete_url)
        assert response.status_code == 200
        return response.json()
