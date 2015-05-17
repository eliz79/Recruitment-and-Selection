#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""Recruitment and Selection"""

from data import *
import pprint


def passed_exam(intial_list):
   """Function filter out the list of candidates with score greater than 70.
   Args:
      Intial_list(list): list of candidate names and scores stored as tuples.
                        The list contains 40 candidates with their names and
                        their scores stored as a tuple in the list
   Return:
      returns a list of tuples with score greater than 70.
   Examples:
   >>> passed_exam([('Nick', 82), ('Anthony', 95), ('Jack', 85), ('Tim', 67)])
   [('Nick', 82), ('Anthony', 95), ('Jack', 85)]
   """
  
   fil_candidates = []
   for item in intial_list:
       if item[1] > 70:
           fil_candidates.append(item)
   return fil_candidates


                     
if __name__ == '__main__':
   import doctest
   doctest.testmod()
   

def fil_list(candidates):
   """Function filters the candidates clearing step 2 of tyhe hirimng process.
      Candidates who clear background check and salary negotiations are
      considered to be the ones clearing step 2 of the process.
   Args:
      candidates(list): this is the list of filtered candidates from function
                        passed_exam the candidates with exam score greater than
                        70 are included.
   Return:
      retrurns a list of candidates who passed the step 2 (backgrounfd check and
      salary negotiations) in hiring process.
   Examples:
      >>> fil_list(intial_list)
      Is step2 cleared by Nick with score 82 (enter n for no, y for yes: )y
      Is step2 cleared by Anthony with score 95 (enter n for no, y for yes: )y
      Is step2 cleared by Jack with score 85 (enter n for no, y for yes: )y
      Is step2 cleared by Tim with score 87 (enter n for no, y for yes: )n
      Is step2 cleared by Chris with score 91 (enter n for no, y for yes: )n
      Is step2 cleared by Tom with score 77 (enter n for no, y for yes: )y
      Is step2 cleared by Albert with score 88 (enter n for no, y for yes: )y
      Is step2 cleared by John with score 89 (enter n for no, y for yes: )y
      Is step2 cleared by Sunny with score 73 (enter n for no, y for yes: )y
      Is step2 cleared by Mark with score 81 (enter n for no, y for yes: )n
      Is step2 cleared by Dave with score 83 (enter n for no, y for yes: )y
      Is step2 cleared by David with score 97 (enter n for no, y for yes: )y
      Is step2 cleared by James with score 93 (enter n for no, y for yes: )y
      Is step2 cleared by Joseph with score 72 (enter n for no, y for yes: )n
      Is step2 cleared by Luke with score 98 (enter n for no, y for yes: )y
      Is step2 cleared by Smith with score 79 (enter n for no, y for yes: )y
      Is step2 cleared by William with score 84 (enter n for no, y for yes: )y
      Is step2 cleared by Carlos with score 86 (enter n for no, y for yes: )n
      Is step2 cleared by Pat with score 90 (enter n for no, y for yes: )n
      Is step2 cleared by Rick with score 94 (enter n for no, y for yes: )y
      Is step2 cleared by Gary with score 92 (enter n for no, y for yes: )y
      Is step2 cleared by Greg with score 80 (enter n for no, y for yes: )y
      Is step2 cleared by Kevin with score 74 (enter n for no, y for yes: )y
      Is step2 cleared by Will with score 99 (enter n for no, y for yes: )y
      Is step2 cleared by Sid with score 96 (enter n for no, y for yes: )y
      Is step2 cleared by Bob with score 87 (enter n for no, y for yes: )y
      Here is the list of Candidates sorted in increasing order of their score: 
      [('Kevin', 74),
      ('Sunny', 73),
      ('Tom', 77),
      ('Smith', 79),
      ('Greg', 80),
      ('Nick', 82),
      ('Dave', 83),
      ('William', 84),
      ('Jack', 85),
      ('Bob', 87),
      ('Albert', 88),
      ('John', 89)
      ('Gary', 92),
      ('James', 93),
      ('Rick', 94),
      ('Anthony', 95),
      ('Sid', 96),
      ('David', 97),
      ('Luke', 98),
      ('Will', 99)]
   """
   candidates = passed_exam(intial_list)
   bgdCheck=[]

   for d in candidates:
      check=raw_input('Is step2 cleared by '+str(d[0])+' with score '
                  +str(d[1])+' (enter n for no, y for yes: )')
      bgdCheck.append(check)


  
   filteredData=[]
   for i in range(0,len(bgdCheck)):
       if bgdCheck[i]=='y':
           filteredData.append(candidates[i])


   filteredData.sort(key=lambda tup: tup[1])

   print('list of Candidates sorted in increasing order of their score: ')
   filteredData.insert(0, filteredData)
   pprint.pprint(filteredData)
   
