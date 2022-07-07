Feature: Login to todolist webportal

    Scenario: Login to todolist app, create 10 random strings and logout
        When I open todolist app
        And I login with username "abc@xyz.com" and password "Test@123"
        And I create 10 to do list with random strings
        Then I verify that I successfully logged out.

    Scenario: Login to todolist app, delete from 5-10 lists and logout
        When I open todolist app
        And I login with username "abc@xyz.com" and password "Test@123"
        And I listed created to-do lists
        And I try delete the list from 5 - 10
        Then I verify that I successfully logged out.
