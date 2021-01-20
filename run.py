#CALCULATOR WITH EMON VAW BY PYTHON

import os
os.system("clear")

print("CALCULATE ANY SIMPLE NUMBER IN NUMERIC")
print("""
  ______    ______   __        ______   __    __  __         ______  ________   ______   _______  
 /      \  /      \ |  \      /      \ |  \  |  \|  \       /      \|        \ /      \ |       \ 
|  $$$$$$\|  $$$$$$\| $$     |  $$$$$$\| $$  | $$| $$      |  $$$$$$\\$$$$$$$$|  $$$$$$\| $$$$$$$\
| $$   \$$| $$__| $$| $$     | $$   \$$| $$  | $$| $$      | $$__| $$  | $$   | $$  | $$| $$__| $$
| $$      | $$    $$| $$     | $$      | $$  | $$| $$      | $$    $$  | $$   | $$  | $$| $$    $$
| $$   __ | $$$$$$$$| $$     | $$   __ | $$  | $$| $$      | $$$$$$$$  | $$   | $$  | $$| $$$$$$$\
| $$__/  \| $$  | $$| $$_____| $$__/  \| $$__/ $$| $$_____ | $$  | $$  | $$   | $$__/ $$| $$  | $$
 \$$    $$| $$  | $$| $$     \\$$    $$ \$$    $$| $$     \| $$  | $$  | $$    \$$    $$| $$  | $$
  \$$$$$$  \$$   \$$ \$$$$$$$$ \$$$$$$   \$$$$$$  \$$$$$$$$ \$$   \$$   \$$     \$$$$$$  \$$   \$$
                                                                                                  
                                                                                                  
                         ================== Version 1==============""")

print("\033[96m  :::::::::::::: CALCULATOR BY EMON VAW.:::::::::::::\n")

def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
Type + for addition
Type - for subtraction
Type * for multiplication
Type / for division
''')

    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print("\033[1;31;40m You have not typed a valid operator, please run the program again\n.")

    # Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
      print("\033[2;37;40m THANKS FOR USING THIS CALCULATOR SEE YOU LATER, FOLLOW ME ON TWITTER: @AnonyminHack5\n")
    else:
        again()

calculate()
