from requests import request
import logging
import random
import string
import time

create_url = 'http://dummy.restapiexample.com/api/v1/create'
update_url = 'http://dummy.restapiexample.com/api/v1/update/{}'
get_url = 'http://dummy.restapiexample.com/api/v1/employee/{}'
delete_url = 'http://dummy.restapiexample.com/api/v1/delete/{}'

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
        update_url = 'http://dummy.restapiexample.com/api/v1/update/{}'.format(data['id'])
        response = request("PUT", update_url, json=data)
        assert response.status_code == 200
        return response.json()

    def get_employee(self, id):
        """
        method to get an employee record
        :return:
        """
        get_url = 'http://dummy.restapiexample.com/api/v1/employee/{}'.format(id)
        response = request("GET", get_url)
        assert response.status_code == 200
        res = response.json()
        map_d = {'employee_name': 'name', 'employee_salary': 'salary', 'employee_age': 'age'}
        new_dict = {'id': res['id']}
        del res['id']
        del res['profile_image']
        for i in res.keys():
            new_dict[map_d[i]] = res[i]
        return new_dict

    def delete_employee(self, id):
        """
        method to delete an existing record
        :return:
        """
        delete_url = 'http://dummy.restapiexample.com/api/v1/delete/{}'.format(id)
        response = request("DELETE", delete_url)
        assert response.status_code == 200
        return response.json()
