# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 10:00:13 2023

@author: cdsouza
"""
from unittest.mock import patch
from unittest import TestCase
from helper_functions_module import *
from Python_Assessment_CD import *



class Time(TestCase):
# At the time this function was tested...we had 2 attendees(888591 and 514427) for the event 16179
# This function gets those attendee id's in a list. The oth index is the column name which is
# omitted during program execution
    def test_validate_attendee_id(self):
        event_id = 16179    
        self.assertEqual(validate_attendee_id(event_id),['Attendee_ID', '888591', '514427'])
 
# Since the functions, need a user input to function @patch is used to supply the test functions with the input
# This test method tests if user has given a valid employee_id. The employee_id is a 4-digit integer
# In this case the functions return 'emp_id invalid' since user inputs a string 'hello'         
    @patch('helper_functions_module.input', return_value = 'hello')       
    def test_validate_employee_id(self,patched_input):
        actual = validate_employee_id()
        expected = 'emp_id invalid'
        self.assertEqual(actual,expected)
        
 # In this case the functions return 'emp_id invalid' since user inputs a 5 digit integer    
    @patch('helper_functions_module.input', return_value = 123354)       
    def test_validate_employee_id2(self,patched_input):
        actual = validate_employee_id()
        expected = 'emp_id invalid'
        self.assertEqual(actual,expected)

# In this case the functions return the emp_id itself since user inputs a valid 4 digit integer
# The use of the function is therefore to validate the emp_id given is a valid one.          
    @patch('helper_functions_module.input', return_value = 4536)       
    def test_validate_employee_id3(self,patched_input):
        actual = validate_employee_id()
        expected = 4536
        self.assertEqual(actual,expected)
        
# This test function tests if the event_id inputted by the user is a valid one.
# Event_ID in our case in a 5 digit integer.
# Here the test function has returned 'event_id_invalid' as user entered a string 'hello'    
    @patch('helper_functions_module.input', return_value = 'hello')       
    def test_validate_event_id(self,patched_input):
        actual = validate_event_id()
        expected = 'event_id invalid'
        self.assertEqual(actual,expected)    
        
# Here the test function has returned 'event_id_invalid' as user entered a 4 digit integer            
    @patch('helper_functions_module.input', return_value = 5875)       
    def test_validate_event_id2(self,patched_input):
        actual = validate_event_id()
        expected = 'event_id invalid'
        self.assertEqual(actual,expected)
        
# Here the test function has returned 'No such Event' because although the user entered a 5 digit
# integer. The event_id wasnt present in the 'Events' Database which means there is no such event 
# registered on our system.         
    @patch('helper_functions_module.input', return_value = 58675)       
    def test_validate_event_id3(self,patched_input):
        actual = validate_event_id()
        expected = 'No such Event'
        self.assertEqual(actual,expected)
        
# Here when the user input matched an actual event. This method returned back the event_id.
# Hence assuring that the event_id existed in the system       
    @patch('helper_functions_module.input', return_value = 56457)       
    def test_validate_event_id3(self,patched_input):
        actual = validate_event_id()
        expected = 56457
        self.assertEqual(actual,expected)  
        
 # This test method tests if the UDF 'event_existence' extracts all the event_ids and 
# loads them in a list       
    def test_event_existence(self):
        actual = event_existence("events.csv")
        expected = ['Event_ID', '16179', '56457']
        self.assertEqual(actual, expected)