# Event Management System


## Introduction

The interim project task was to create an Event Management System(EMS) using Python. In general the EMS is used to plan and execute events by event management companies. The EMS created here is aimed to have the following features :-

👉 Adding an event in the system.

👉 Editing the details of an event.

👉 Cancelling an event

👉 Display all the events in the system

👉 Display the details of an event

👉 Display the attendee list of an event

👉 Adding an attendee to an event

👉 Delete an attendee from an event.

👉 Console displaying the menu


## Python Tools

To achieve the final results, a host of Python concepts were used. Some of them are listed below:

👉 Object Oriented Programming

👉 Functional Programming

👉 Exception and File Handling

👉 Closures and Decorators

👉 Unittest/TDD



## Code Structure

The underlying code structure opted here is that of Object Oriented Programming(OOP). User Defined Functions have also been used in order to aid the functionalities where necessary. In total, 3 python files were created : -

👉 Classes, Objects and ‘main’ function(Python_Assessement_CD.py)

👉 User defined functions(helper_functions_module.py)

👉 Test or TDD methods(test_cases.py)


![image](https://github.com/piperalpha7/Python-Event-Management-System/assets/94968239/57ceb6ad-d01d-4900-a5dd-daa0fb16c660)


I defined 4 classes i.e. Company, Admin, Events and Attendees. The diagram above shows the Multilevel Inheritance approach used in order to create this project. Every class shows the attributes local to itself. But on inheritance, it derived the features from its parent class. Hence, the class Attendees was able to derive attributes from all the parent classes while having some of its own.

The project requirements stated that ‘Events’ and ‘Attendees’ are the 2 things users would keep manipulating. Since every attendee was linked to an event, it was necessary that the attributes under ‘class Events’ needed to be derived by ‘class Attendees’. Now, to do any kind of manipulation with data, the users needed to be authorized and hence for this purpose ‘class Admin’ was created. This is the reason why class Events and class Attendees needed to derive from class ’Admin'. 



![image](https://github.com/piperalpha7/Python-Event-Management-System/assets/94968239/78699309-fd8d-4300-aa84-0b8f8dd17319)
 



Class Company was just created to hold the name of the company, which would be needed to displayed at a certain stage in the console. This is the reason why this class was converted to an ‘abstract class’.

Apart from this the user defined functions aided our project in tasks like validating employee_id, event_id etc. so that users do not enter the incorrect data.



## Software Functionalities

As stated in the introduction above we are now aware of what our project aims to achieve. Let us list a little more detail about each functionality.

### 👉 Adding an event in the system

  The user would be asked to enter the date in yyyy/mm/dd format only. The event_id is a 5 digit integer that                  would be system generated. Apart from this, the user would be free to enter the name of the event, type of the event and venue. All these details were then added to an “events.csv” file, alongwith the headers. Once the event was created, simultaneously another blank csv file would be created which can save the attendee details for that particular event.   



![image](https://github.com/piperalpha7/Python-Event-Management-System/assets/94968239/b44ce95d-75f1-4a06-80de-2c5a0f77af1c)




### 👉 Editing the details of an event

  When the user chose to edit the details of a registered event, the system would show them the details of all the registered events for them to refer and obtain the correct event_id. Incase, they still get it wrong, as a failsafe the system will redirect them back to the menu. But, when they enter the correct event_id , the system will ask them yes/no questions about the details they would like to edit. They will then enter the information they wish to change. This information would then be overwritten on the “events.csv” file, thereby now containing the updated information.  

      



![image](https://github.com/piperalpha7/Python-Event-Management-System/assets/94968239/009f7f8e-f518-4e1a-98e6-085d8f09c2dd)




### 👉 Cancelling an event

The user will be first shown all the events registered in the system to get the correct event_id of the event they wish to cancel. Once they feed it in, all the details of the csv file would be transferred to a ‘list’ , the appropriate event details would be deleted and then the list contents will again be written back to the csv.





![image](https://github.com/piperalpha7/Python-Event-Management-System/assets/94968239/c2c84283-34a2-4fd5-88da-104976960836)


                                                     

### 👉 Display all the events in the system

The user would just be shown all the events registered on the system as follows:


![image](https://github.com/piperalpha7/Python-Event-Management-System/assets/94968239/caba06e0-81d6-4924-8e1c-b9ef58ad5d74)





### 👉 Display the details of an event

The user will be prompted to enter the event_id , they wish to see details of . The interface would look like:



![image](https://github.com/piperalpha7/Python-Event-Management-System/assets/94968239/1b5731bb-6051-4f5d-84b9-21b39d83e512)




### 👉 Display the attendee list of an event

The user is prompted to enter the event_id of the event they wish to see the attendees of. The interface would be like :



![image](https://github.com/piperalpha7/Python-Event-Management-System/assets/94968239/2061a964-83ab-47c4-8e7a-eaf2aaa4cc36)






### 👉 Adding an attendee to an event

  The user is prompted to enter the ‘Name’ and ’Age' of an attendee. The list of all the registered events is then displayed so they know the evnt_id of the event they wish to add the attendee to. Once the right input is obtained, the attendee is added to the event.

![image](https://github.com/piperalpha7/Python-Event-Management-System/assets/94968239/c074aa83-8728-4127-81c4-71a83e120735)




### 👉 Delete an attendee from an event

The user is requested the event_id and the attendee_id that they want deleted. 



![image](https://github.com/piperalpha7/Python-Event-Management-System/assets/94968239/6c8647d9-1fdb-4cb1-9914-924bf1786281)




### 👉 Console displaying the menu

The console id run by the ‘main function’ which after verifying the login details, logs the user in and displays a plethora of options. The system then takes user input of thee action they need to perform



![image](https://github.com/piperalpha7/Python-Event-Management-System/assets/94968239/d7f6c3be-fbc1-430f-83ec-974b598283a1)




## Timeline

The project was performed in custom sprints each lasting around a day. Totally 5 sprints were needed. Some of the screenshots of the sprint tasks are listed below:-



![image](https://github.com/piperalpha7/Python-Event-Management-System/assets/94968239/c442b8b7-4b35-4852-a6c3-a765ade63d89)




![image](https://github.com/piperalpha7/Python-Event-Management-System/assets/94968239/02986fd7-89bf-44e5-b41c-c89277cd34dd)


                            



![image](https://github.com/piperalpha7/Python-Event-Management-System/assets/94968239/476c71b2-e41f-4dab-b228-608f28d0a0d5)




## Conclusion

The project was a great example of how core python concepts could still be used without needing the libraries like numpy or pandas, as is common belief. One of the hallmarks of this project was to think about the various ways a user could enter the data incorrectly and hence having fail safes like not doing any action and redirecting back to the menu needed to be designed at various points in the code.

