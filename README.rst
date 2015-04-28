Recruitment and Selection
===========================
Recruitment provides opportunities to departments to align staff skill sets for
departmental growth. Proper planning and evaluation will lead to hiring the
right person for the team. The process can lead to frustration, if there are not
proper resources or if the resources are not properly utilized due to the
obsolete methods in the process. 

Persona:
=========
John the HR Assistant Manager:
===============================
John Brown is the Assistant Manager of Human resources in a government 
agency. John wants to minimize the duration of selection process.

''Details'':
This project explains recruitment process of a class of employees (say R)
and the problems encountered in the hiring process. The recruitment for class
R consists of Examination, Background checks and salary negotiations. For a
candidate to get hired, he must clear all phases in order to be eligible for
the final list. John wants to generate a pool of prescreened employees on the
basis of eligibility criteria before his team gets notified.

Goals:
This template will overcome delays in achieving target at deadline by preparing
pool of prescreened perspective new hires before recruitment starts for next
target.

Problem Scenarios:
===================
HR team is provided a target of 20 new hires for a particular class.  
The process should be completed within a given deadline without any delays

Current Alternatives: 
^^^^^^^^^^^^^^^^^^^^^
20 candidates are selected with passing score (HR does not have enough time to
select and screen extra employees from list as the selection is started after
the notification), candidates passing the background checks and salary
negotiations are moved to next step. Five of them fails phase 2. The choose 5
employees and move to step 2 and step 3 until target is achieved

Value Proposition:
^^^^^^^^^^^^^^^^^^
A software that will help to filter and sort the employees on the basis of their 
exam scores after performing the background checks and salary negotiations.
While the whole process is performed electronically, it will save the time and 
there is less possibility of errors.

User Stories:
=============
As John the HR assistant manager, I would like to select extra candidates from
the list of candidates by their minimum passing score of 70 before notification.

I would like to perform the background checks, and perform the salary
negotiations and move them into next step.

I would like to sort the candidates after clearing all the phases in the order
of their exam scores, thus creating a final list of prescreened prospective
new hires.

Acceptance Stories
^^^^^^^^^^^^^^^^^^
Scenario: 1
```````````
Filtering the candidates with passing score:
````````````````````````````````````````````    
Given that the date for next target is approaching,

When I click filter button

Then the list with names and exam scores is imported, and candidates with score
less than 70 are filtered out

Scenario: 2
```````````
Background Checks and Salary:
`````````````````````````````
Given that the candidates are filtered out,

When I  perform background checks and salary negotiations,

Then the candidates having passed the background checks and salary negotiations
are added to list for next step.

Scenario: 3
````````````
Sorting the final list:
```````````````````````
Given that the candidates are selected for final stage,

When I  would click the sort button,

Then they will be  sorted into the final list with their exam scores.
