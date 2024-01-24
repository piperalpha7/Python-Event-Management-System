# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 19:51:04 2023

@author: charl
"""

# Importing necessary modules
import random
from datetime import datetime
import os
from abc import ABC, abstractmethod


# Function to check if an event exists. If they do ,then load the details in a list
def event_existence(filename):
    pwd = os.getcwd()
    lst =[]
    for path,dir,files in os.walk(pwd):
        if filename not in files:
            return 'No Event'
        else:
            with open(filename, 'r') as f:
                 event_details = f.readlines()
            for line in event_details:
                lst.append(line.split(',')[1])
            f.close()    
            return lst


# Function to see the details of events
def show_details_of_events(event_existence,filename,no_of_events):
        while True:
            if event_existence(filename) == 'No Event':
                return "There are no events registered at the moment.Please go back to the menu, to add one."
                break
            else:
                lst = event_existence(filename)
   # Display the details of a single event based on the event_id taken        
            if no_of_events == 1:
                while True:
                    try:
                        event_no = int(input("Please input the 5-digit event_id  "))
                    except ValueError:
                        return "Invalid Event_id"
                    if len(str(event_no)) != 5:
                        return "Invalid Event_id"
                    break
            
                if str(event_no) in lst:
                    index = lst.index(str(event_no))
                    lst1 =[]
                    with open('events.csv', 'r') as f:
                         event_details = f.readlines()
                    for line in event_details:
                       lst1.append(list(map(lambda x:x.strip(),line.split(','))))
                    print('The details of the event you requested are : \n\n'+lst1[0][0]+' : ' + lst1[index][0] +'\n' + lst1[0][1]+' : ' + lst1[index][1] +'\n' + lst1[0][2]+' : ' + lst1[index][2] +'\n'+ lst1[0][3]+' : ' + lst1[index][3] +'\n' + lst1[0][4]+' : ' + lst1[index][4] +'\n')
                    return [lst1[index][0],lst1[index][1],lst1[index][2],lst1[index][3],lst1[index][4]]
                else:
                    return'No such event'
                break
 # Displaying the details of all the events at that particular time                  
            else:
                all_events =''    
                lst2 = []
                with open('events.csv', 'r') as f:
                     event_details = f.readlines()
                for line in event_details:
                   lst2.append(list(map(lambda x:x.strip(),line.split(',')))) 
                for i in range(1,len(lst2)):
                    all_events+= lst2[0][0]+' : ' + lst2[i][0] +'\n' + lst2[0][1]+' : ' + lst2[i][1] +'\n' + lst2[0][2]+' : ' + lst2[i][2] +'\n' + lst2[0][3]+' : ' + lst2[i][3] +'\n' + lst2[0][4]+' : ' + lst2[i][4] +'\n\n\n'
                print('The details of all the events are as follows'+'\n\n')
                print(all_events)
                break
                

# Functions to demonstrate the knowledge of Closures and Decorators
# Displays the details of attendees, attending an event
def show_attendee_details(func):
    lst1=[]
    
    def helper_show_attendees():
        a = func()
        all_attendees =''
        if len(str(a))==5:
            with open(str(a)+'.csv', 'r') as f:
                 attendee_details = f.readlines()
            for line in attendee_details:
               lst1.append(list(map(lambda x:x.strip(),line.split(','))))
            for i in range(1,len(lst1)):
                all_attendees+= lst1[0][0]+' : ' + lst1[i][0] +'\n' + lst1[0][1]+' : ' + lst1[i][1] +'\n' + lst1[0][2]+' : ' + lst1[i][2] +'\n\n' 
            if all_attendees!='':
                return 'The details of all the attendees are as follows'+'\n\n'+str(all_attendees)
            else:
                return 'No attendees'
        else:
            return a
    return helper_show_attendees      
   
     
# Decorator function which is passed above as a parameter 
# Function to check whether an event id entered by the user is a valid one or not.   
@show_attendee_details
def validate_event_id():
    try:
        event_id = int(input("Please input your 5-digit event_id "))
    except ValueError:
        return 'event_id invalid'
    if len(str(event_id)) != 5:
        return 'event_id invalid'
    elif len(str(event_id)) == 5:
        for path,dir,files in os.walk(os.getcwd()):
            if str(event_id)+'.csv' not in files:
                return 'No such Event'
            else:
                return event_id

            
# Function to check whether an employee id entered by the user is a valid one or not.   
def validate_employee_id():
    try:
        emp_no = int(input("Please input your 4-digit employee number "))
    except ValueError:
        return 'emp_id invalid'
    if len(str(emp_no)) != 4:
        return 'emp_id invalid'
    elif len(str(emp_no)) == 4:
        return emp_no

def validate_attendee_id(event_id):
    lst =[]
    with open(str(event_id)+'.csv', 'r') as f:
         attendee_details = f.readlines()
    for line in attendee_details:
        lst.append(line.split(',')[0])
    f.close()    
    return lst



