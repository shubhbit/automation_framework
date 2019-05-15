@employee_api
Feature: Employee CRUD
  this is a feature file of an employee record life-cycle in an organization

  Background: Make sure employee system is up and running
    Given the employee system is up and running

  @TC-1 @regression
  Scenario: Create an record for new employee
      Given user is logged in
       When user creates an employee with name as "name" salary as "111111" and age as "25"
       Then user can verify employee is registered

  @TC-2 @smoke_ci
  Scenario: Update an existing employee record
      Given some other condition
       When some action is taken
       Then some other result is expected.

  @TC-3 @regression
  Scenario: Get an existing employee record
      Given some other condition
       When some action is taken
       Then some other result is expected.

  @TC-4
  Scenario: Delete an existing employee record
      Given some other condition
       When some action is taken
       Then some other result is expected.