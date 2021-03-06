'''
Xinyi Huang (Nicole)
xhuang78@binghamton.edu
B58 Jia Yang
Assignment #6
'''

'''
ANALYSIS

RESTATEMENT:
  Ask a user to input the year and output if this year is a leap year or not

OUTPUT to monitor:
 num_year is a leap year or num_year is not a leap year

INPUT from keyboard:
 num_year - give a year

FORMULAS:
num_year % 4 == 0
num_year % 100 == 0
num % 400 == 0






'''




# Explain purpose of program to user
# This program to check if a input year is a leap year or not



import math

#CONSTANTS

FOUR = 4
ZERO = 0
HUNDRED = 100
FOUR_HUNDRED = 400
TEST_EDGE_DATA_LIST = [1599,1600,1601,1602,1603,1604,1605,
                        1799,1800,1801,1802,1803,1804,1805]


#check to see that is only contains digits and >0
def is_positive(num_year_str):
    return num_year_str.isdigit() and int(num_year_str) > 0
        
#check leap year
def is_leap_year(num_year):
    return (num_year % FOUR == 0 )and  ( num_year % HUNDRED != 0 )or\
       ( num_year % FOUR_HUNDRED == 0)
        
    print ()

  
def main():
  

  print("This program determines if a given year is a leap year or not")
    
  num_year_str = input("Enter a year :   ")
   
  while num_year_str:
       
    while not is_positive(num_year_str):
      print("Invalid Input: input only interger")
      num_year_str = input("Enter a year :   ")

    num_year = int(num_year_str)

##    print(is_leap_year(num_year))
    print("%d %s a leap year" % (num_year, \
        "is" if(is_leap_year(num_year)) else "is not"))
    
    num_year_str = input("Enter a year :   ")
 
  print()            

             
main()
  

















