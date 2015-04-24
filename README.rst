Recruitment and Selection
===========================

'Description': Recruitment provides opportunities to departments to align staff 
skill sets to initiatives and goals, and for departmental and individual growth.
Proper planning and evaluation of the need will lead to hiring the right person
for the role and team. The process can lead to frustration, if there are not
proper resources or if the resources are not properly utilized due to the
obsolete methods in the process. This project tries to overcome the problems
in hiring process.

Persona:
=========
John the HR Assistant Manager:
===============================
John Brown is the Assistant Manager of Human resources in a government 
agency. John wants to minimize the duration of selection process.

''Details'':
The HR team is given a target of new hires for different categories. This
project explains recruitment process of one such class of employees (say R)
and the problems encountered in the hiring process. The recruitment for class
R consists of various steps. Examination, Background
checks and negotiation for salary (salary belonging to that class is fixed).
For a candidate to get hired, he must have all the tests cleared in order to be
eligible for the final list. John wants to generate a pool of prescreened
employees on the basis of eligibility criteria before his team gets notified.
Once he has a filtered list of employees, it will be easier for them to achieve
the target from filtered employees at the time of notification.

Goals:
This template will overcome the delays caused in achieving the target in the
deadline provided by preparing the pool of prescreened perspective new hires
before the recruitment starts for the next target.

Problem Scenarios:
===================
HR team is provided a target of 20 new hires for a particular class.  
The process should be completed within a given deadline without any delays

Current Alternatives: 
^^^^^^^^^^^^^^^^^^^^^
After the selecting 20 candidates with passing score (HR does not have
enough time to select and screen extra employees from list as the selection
is started after the notification), candidates passing the background checks 
are moved to next step.  Salary is negotiated with candidates. Five of them
fails background checks and the salary negotiations, the target is short. 
The step one is repeated again, choose 5 employees and move to step 2 and
 step 3 until target is achieved.

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
Given that the date for next target is approaching, when I import the list of
data with names and exam scores, then the candidates with score less than 70
are filtered out.

Scenario: 2
```````````
Background checks and salary negotiations:
``````````````````````````````````````````
When the candidates are filtered out, I would then perform background checks
and salary negotiations. Candidates having passed the background checks and
salary negotiations are added in the final list

 Scenario: 3
````````````
Sorting the final list:
```````````````````````
The final stage is to sort them according to their score so that are ready to
be on board. The employee names with score and an integer 1 are sorted on the
basis of their exam score and a final prescreened list is created.




