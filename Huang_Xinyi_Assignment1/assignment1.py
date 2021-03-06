'''
Xinyi Huang (Nicole)
xhuang78@binghamton.edu
B58 Shehtab Zaman
Assignment #1
'''

'''
ANALYSIS

RESTATEMENT:
  Ask a user how many people in a room and output the total number of handshakes in times

OUTPUT to monitor:
  total_handshakes (int) - total number of handshakes in times

INPUT from keyboard:
  people_count (int)

FORMULAS:
  n * (n - 1) / 2 

GIVENS: 
  PEOPLE_NUMBER (int) >= 0
  N_VALUE(int) - people_count, number of people in a room



'''

# CONSTANTS 
HALF=2

# This program outputs the total number of handshakes that each person shakes hands with every other person once in a room


def main():

  
  # Explain purpose of program to user
  print("This program outputs the total number of handshakes possible," 
        "if each person in a room shakes the hand of every other person in the room once," 
        "given the number of people in the room")

  # Ask user for number of people in a room
  people_count_str = input("How many people are in the room?    ")

  # Convert str data to int
  people_count = int(people_count_str)

  # Put the number of the people into the formula
  total_handshakes = people_count * (people_count - 1) / HALF
 
  # Display labeled and formatted output in times
  print( '%d people can perform %d handshakes' % (people_count, total_handshakes))

main()
