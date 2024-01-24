# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 20:36:28 2023

@author: charl
"""

import random
from datetime import datetime
import os
from abc import ABC, abstractmethod
from helper_functions_module import *



# Creating a class 'Company' having only the 'company name' variable
class Company(ABC):
    def __init__(self,comp_name):
        self.comp_name = comp_name
 # OOP pillar of 'Abstraction'       
    @abstractmethod 
    def company_intro_display(self):
        pass
        
        
 # Creating a class 'Admin' which derives from Company and gets its own user secutiry attributes              
class Admin(Company):
    def __init__(self,name,emp_no,password):
        super().__init__(name)
        self.__emp_no = emp_no
        self.__password = password
        
# OOP pillar of 'Encapsulation'.  Needs pass word to do any operation to database        
    @property
    def password(self):
        if self.__password== 'admin':
            return 'Login Successful'
        else:
            return 'Incorrect Credentials'

    @password.setter
    def password(self, password):
        if self.__password == 'admin':
            self.__password = password
            print ('Password changed successfully')
        else:
            print ('Existing Password is Incorrect. Try Again!!')

    @property
    def emp_no(self):
        return self.__emp_no
    
    @property
    def password2(self):
        return self.__password
    
# Overriding the abstract method
    def company_intro_display(self):
        print(f"Welcome to the {self.comp_name} Event Management Company")



# Creating a class 'Events' which derived from Admin and gets its own variables peratining to the details of the events
class Events(Admin):
    
    def __init__(self,comp_name,emp_no,password,date,event_id,name,type_of_event,venue):
        super().__init__(comp_name,emp_no,password)
        self.date = date
        self.event_id = event_id
        self.name = name
        self.type_of_event = type_of_event
        self.venue = venue

# Method to add an event to a csv  
# Methods with similar names will be found in the Events class also. Hence showing Polymorphism     
    def add(self):
        event_details = [self.date,self.event_id,self.name,self.type_of_event,self.venue]
        headers = ['Date','Event_ID','Name of the Event','Type of Event','Venue']
        with open("events.csv",mode= "a") as file:
           if os.stat("events.csv").st_size == 0:
               for header in headers:
                   if headers.index(header)!= len(headers) - 1:
                       file.write(header+',')
                   else:
                       file.write(header+'\n')
           for detail in event_details:
               if event_details.index(detail)!= len(event_details) - 1:
                   file.write(str(detail)+',')
               else:
                   file.write(str(detail)+'\n')
        attendee_headers = ['Attendee_ID','Attendee_Name','Age']
        attendee_iter = iter(attendee_headers)
        with open(str(self.event_id)+'.csv', "w") as event_attendee_csv:
            for i in range(0,3):
                if i!=2:
                    event_attendee_csv.write(attendee_iter.__next__()+',')
                else:
                    event_attendee_csv.write(attendee_iter.__next__()+'\n')
  
                    
# Method to edit event details in a csv file  
    def edit(self):
        lst =[]
        lst1 =[]
        with open("events.csv", 'r') as f:
             event_details = f.readlines()
        for line in event_details:
            lst.append(line.split(',')[1])
            lst1.append(list(map(lambda x:x.strip(),line.split(','))))
        f.close()    
        index = lst.index(str(self.event_id))
        date_change_resp = input(f"The date of the event is {self.date}. Would you like to change this Y/N ")
        if date_change_resp == 'Y' or date_change_resp == 'y':
            try:
                date = input("Please enter the new date of the event in yyyy/mm/dd: ") 
                date = datetime.strptime(date, '%Y/%m/%d').date()
                lst1[index][0]= date
            except ValueError:
                return 'Invalid Entry'
        elif date_change_resp == 'N' or date_change_resp == 'n':
            pass
        else:
            return 'Invalid Entry'
    
        
        name_change_resp = input(f"The name of the event is {self.name}. Would you like to change this Y/N ")
        if name_change_resp == 'Y' or name_change_resp == 'y':
            name = input("Please enter the new name of the event ")
            lst1[index][2]= name   
        elif name_change_resp == 'N' or name_change_resp == 'n':
            pass
        else:
            return 'Invalid Entry'
     
        
        type_change_resp = input(f"The type of the event is {self.type_of_event}. Would you like to change this Y/N ")
        if type_change_resp == 'Y' or type_change_resp == 'y':
            type_of_event = input("Please enter the new type of the event eg. Seminar/Concert ")
            lst1[index][3]= type_of_event 
        elif type_change_resp == 'N' or type_change_resp == 'n':
            pass
        else:
            return 'Invalid Entry'
        
        venue_change_resp = input(f"The venue of the event is {self.venue}. Would you like to change this Y/N ")
        if venue_change_resp == 'Y' or venue_change_resp == 'y':
            venue = input("Please enter the new venue for the event ")
            lst1[index][4]= venue
        elif venue_change_resp == 'N' or venue_change_resp == 'n':
            pass
        else:
            return 'Invalid Entry'
           
        
        if os.path.exists('events.csv'):
            os.remove('events.csv')
        for line in lst1:
            for idx in range(0,len(line)):
                with open("events.csv",mode= "a") as file:
                    if idx!= len(line)-1:
                        file.write(str(line[idx])+',')
                    elif idx== len(line)-1:
                        file.write(str(line[idx])+'\n')
           
 
# Method to delete chosen event details from a csv file           
    def delete(self):
        lst =[]
        lst1 =[]
        with open("events.csv", 'r') as f:
             event_details = f.readlines()
        for line in event_details:
            lst.append(line.split(',')[1])
            lst1.append(list(map(lambda x:x.strip(),line.split(','))))
        f.close()    
        index = lst.index(str(self.event_id)) 
        del lst1[index]
        if os.path.exists('events.csv'):
            os.remove('events.csv')
        for line in lst1:
            for idx in range(0,len(line)):
                with open("events.csv",mode= "a") as file:
                    if idx!= len(line)-1:
                        file.write(str(line[idx])+',')
                    elif idx== len(line)-1:
                        file.write(str(line[idx])+'\n')            
    
             

# Creating a class Attendees deriving from 'Events' and having own variables revolving around the attendee details
class Attendees(Events):
    def __init__(self,comp_name,emp_no,password,date,event_id,name,type_of_event,venue,attendee_id,attendee_name,attendee_age):
        super().__init__(comp_name,emp_no,password,date,event_id,name,type_of_event,venue)
        self.attendee_id = attendee_id
        self.attendee_name = attendee_name
        self.attendee_age = attendee_age
    
# Method to add an attendee to an event
    def add(self):
        details = [self.attendee_id,self.attendee_name,self.attendee_age,self.event_id,self.emp_no]
        attendee_details = details[0:3]
        pwd = os.getcwd()
        lst =[]
        for path,dir,files in os.walk(pwd):
            if 'events.csv' not in files:
                return 'No Event'
            else:
                with open(str(self.event_id)+'.csv',mode= "a") as file:
                    for detail in attendee_details:
                        if attendee_details.index(detail)!= len(attendee_details) - 1:
                            file.write(str(detail)+',')
                        else:
                            file.write(str(detail)+'\n')
                    
        
# Method to delete an attendee from an event
    def delete(self):
        lst =[]
        lst1 =[]
        with open(str(self.event_id)+".csv", 'r') as f:
             attendee_details = f.readlines()
        for line in attendee_details:
            lst.append(line.split(',')[0])
            lst1.append(list(map(lambda x:x.strip(),line.split(','))))
        f.close() 
        if str(self.attendee_id) in lst:
            index = lst.index(str(self.attendee_id))
            del lst1[index]
            if os.path.exists(str(self.event_id)+".csv"):
                os.remove(str(self.event_id)+".csv")
            for line in lst1:
                for idx in range(0,len(line)):
                    with open(str(self.event_id)+".csv",mode= "a") as file:
                        if idx!= len(line)-1:
                            file.write(str(line[idx])+',')
                        elif idx== len(line)-1:
                            file.write(str(line[idx])+'\n') 
        else:
            return 'No such attendee'




# Main function which actually runs the sequence of operations and calls functions and class methods when needed
def main():
   # Code Block to ask options and allows to change password or exit 
    while True:
        try:
            log_or_pwd = int(input("Choose an option please(Eg. 1,2 or 3).\n1.Login to the system?\n2.Change your credentials?\n3.Exit? "))
            if log_or_pwd == 1:
                break
            elif log_or_pwd == 2:
                comp_name = 'CD'
                emp_no = validate_employee_id()
                if len(str(emp_no)) == 4:
                    ask_user_pass = input('Enter your existing password ')
                    log_details = Admin(comp_name,emp_no, ask_user_pass)
                    new_pass = input("Please enter your new password")
                    log_details.password = new_pass
                    continue
                elif emp_no == 'emp_id invalid':
                    resp2 = input ('The user_id is invalid. Do you want to try again?(Y/N)' )
                    if resp2 in ('Y','y'):
                        continue
                    elif resp2 in ('N','n'):
                        print('Exiting the system')
                        return
                    else:
                        print('Invalid entry.Enter credentials again')
            elif log_or_pwd ==3:
                print ('Exiting the system')
                return
        except ValueError:
            print("Invalid choice. Redirecting back to the menu")
        
 # Code Block to check credentials and log the user in 
    while True:
           comp_name = 'CD'
           emp_no = validate_employee_id()
           if len(str(emp_no)) == 4:
                password = input("Please input your password ")
                credentials = Admin(comp_name,emp_no, password)
                if credentials.password == 'Login Successful':
                    break
                else:
                    resp = input("Password Incorrect. Do you want to try again? Press Y or N.")
                    if resp in ('Y','y'):
                        continue
                    elif resp in ('N','n'):
                        print ('Exiting the system')
                        return
                    else:
                        print('Invalid entry.Enter credentials again')
                        
                        
   # Code Block to show menu and then options
    credentials.company_intro_display()   
    while True:
        try:
            choice = int(input("Please select the option you need.\n1.Add an event\n2.Edit the details of an event.\n3.Cancel the event.\n4.Show all the events.\n5.Show the details of an event.\n6.Show the attendee list of an event\n7.Add an attendee to an event\n8.Remove an attendee for a particular event\n9.Quit the menu\nYour choice(ex. 1 or 2) : "))
        except ValueError:
            print('\nIncorrect choice.Please make sure your choice is a number.Displaying the options again : ')
            continue
        
        
   # Code block to carry out the operation of adding an event to the system     
        if choice == 1:
            while True:
                try:
                    date = input("Please enter the date of the event in yyyy/mm/dd: ") 
                    date = datetime.strptime(date, '%Y/%m/%d').date()
                    break
                except ValueError:
                    print("The Date entered is invalid.")
                    continue
            event_id = random.randint(10000,99999)
            name = input("Please enter the name of the event: ")
            venue = input("Please enter the venue of this event: ")
            event_entry = Events(comp_name,emp_no,password,date, event_id, name, type_of_event, venue)
            event_entry.add()
            print(f"The event, {event_id} has now been added to the system.")
            
            
 # Code block to edit the details of an event           
        elif choice == 2:
            show_details_of_events(event_existence, 'events.csv', 2)
            print("Please note the event_id of the event you would like to edit. \n\n ")
            event_details  = show_details_of_events(event_existence, 'events.csv', 1)
            if event_details == 'No such event' or event_details=='Invalid Event_id':
                print("Invalid Event_ID.Taking you back to the menu")
            else:
                date,event_id,name,type_of_event,venue = event_details
                event_edit_obj = Events(comp_name,emp_no,password,date, event_id, name, type_of_event, venue)
                event_edit = event_edit_obj.edit()
                print(f"The event,{event_id} has now been edited.")
                if event_edit =='Invalid Entry':
                    print("Invalid Entry. Taking you back to the menu")
                elif event_edit =='Back to menu':
                    print("Taking you back to the menu")
            
                    
 # Code block to cancel an event
        elif choice == 3:
            show_details_of_events(event_existence, 'events.csv', 2)
            print("Please note the event_id of the event you would like to cancel. \n\n ")
            event_details  = show_details_of_events(event_existence, 'events.csv', 1)
            if event_details == 'No such event' or event_details=='Invalid Event_id':
                print("Invalid Event_ID.Taking you back to the menu")
            else:
                date,event_id,name,type_of_event,venue = event_details
                event_del_obj = Events(comp_name,emp_no,password,date, event_id, name, type_of_event, venue)
                event_del = event_del_obj.delete()
                print(f"The event , {event_id} has now been cancelled. ")
                #print(log_file(credentials, 'deleted the event', event_id))
                if os.path.exists(str(event_id) +'.csv'):
                    os.remove(str(event_id) +'.csv')
                    
                    
                    
                    
 # Code block to display all the events                   
        elif choice == 4:
            print(show_details_of_events(event_existence, 'events.csv', 2))
            
            
 # Code block to display the details of a particular event           
        elif choice == 5:
            event_content = show_details_of_events(event_existence, 'events.csv', 1)
            event_content
            if event_content == 'No such event' : 
                print("No such event.Taking you back to the menu")
            elif event_content=='Invalid Event_id':
                print("Invalid Event_ID. Taking you back to the menu")
                
                
 # Code block to display the attendee list of a particular event               
        elif choice == 6:
            val = validate_event_id()
            if val == 'event_id invalid':
                print('The event_id is invalid. Redirecting back to the menu.\n\n')
            elif val == 'No such Event':
                print("There is no such event. Redirecting back to the menu.\n\n")
            elif val == 'No attendees':
                print("There are no attendees registered for this event.\n\n")
            else:
                print(val+'\n')
                
                
         # Code block to add an attendee to an event       
        elif choice == 7:
            attendee_id = random.randint(100000,999999)
            attendee_name = input("Please enter the name of the attendee ")
            try:
                attendee_age = int(input("Please enter the age of the attendee  "))
            except ValueError:
                print("The age entered is invalid. Redirecting to the menu")
                continue
            if attendee_age > 100 or attendee_age < 0:
                print("The age entered appears to be ambiguous. Redirecting to the menu")
                continue
            print("The details of all the events will be listed.Please note the event_id to which you want to add attendees and enter when prompted again")
            show_details_of_events(event_existence, 'events.csv', 2)
            event_details  = show_details_of_events(event_existence, 'events.csv', 1)
            if event_details == 'No such event' or event_details=='Invalid Event_id':
                print("Invalid Event_ID.Taking you back to the menu")
            else:
                date,event_id,name,type_of_event,venue = event_details
                attendee_entry = Attendees(comp_name,emp_no,password,date,event_id,name,type_of_event,venue,attendee_id,attendee_name,attendee_age)
                attendee_entry.add()
                print(f"The attendee({attendee_id}) has now been added to the event,{event_id}")
                
                
    # Code block to delete an attendee from an event                
        elif choice == 8:
            event_details  = show_details_of_events(event_existence, 'events.csv', 1)
            if event_details == 'Invalid Event_id':
                print("The event_id entered is invalid. Redirecting back to the menu")
                continue
            elif event_details == 'No such event':
                print("There is no such event. Redirecting back to the menu")
                continue
            else:
                pass
            date,event_id,name,type_of_event,venue = event_details
            try: 
                attendee_id= int(input("Please enter the 6-digit attendee_id of the attendee you would like to remove."))
            except ValueError:
                print("Invalid attendee_id. Redirecting back to the menu")
                continue
            attendee_obj = Attendees(comp_name, emp_no, password, date, event_id, name, type_of_event, venue, attendee_id, "dummy", "dummy")
            attendee_del = attendee_obj.delete()
            print(f"The attendee({attendee_id} has now been deleted from event,{event_id} \n")
            if attendee_del =='No such attendee':
                print("No such attendee. Redirecting back to the menu")
                continue
 
# Exit the system
               
        elif choice == 9:
            print('Exiting the system')
            break
        
        
if __name__ == '__main__': #keep this in main
   main()