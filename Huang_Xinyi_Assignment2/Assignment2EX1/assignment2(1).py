'''
Xinyi Huang (Nicole)
xhuang78@binghamton.edu
B58 Jia Yang
Assignment #2
'''

'''
ANALYSIS

RESTATEMENT:
  Ask a user how many side does the polygon have
  and output the total number of diagonals

OUTPUT to monitor:
  total_diagonals (int) - total number of diagonals

INPUT from keyboard:
  sides_count (int) - number of sides of polygon

FORMULAS:
1/2 * n * ( n - 3 )

GIVENS: 
  SIDES_NUMBER (int) >= 0
  N_VALUE(int) - sides_count, sides of polygon



'''

# CONSTANTS 
HALF=1/2


# Explain purpose of program to user
# This program outputs the total number of diagonals that the polygon have


def main():

  print("Computes the number of diagonals in a polygon given  the sides")

  # Ask user for number of sides of polygon
  sides_count_str = input("How many sides does the polygon have?    ")
  
  # Convert str data to int
  sides_count = int(sides_count_str)

  # Put the number of sides into the formula
  total_diagonals = HALF * sides_count *( sides_count - 3 )
 
  # Display labeled and formatted output in diagonals
  print( 'A %d sides polygon has %d diagonals == %d diagonals'
         % (sides_count, total_diagonals, total_diagonals))

main() 
