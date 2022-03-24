#Program to generate output of 2 dices rolled together
import random #Random module generates the random number on each dice roll

#range of the values of a dice
min_val = 1
max_val = 6

#to loop the rolling through user input
roll_again = "yes"
user= input("If you want to roll the dices, please type in Yes.\n")

while roll_again == "yes" or roll_again == "Yes":
    print("Rolling The Dices...")
    print("The Values are :")
    
    first_num = random.randint(min_val, max_val) #Randint function generates the random integer within the specified range
    print(first_num)
    
    second_num = random.randint(min_val, max_val)
    print(second_num)
    
    roll_again = input("Roll the Dices Again?\n") #Asking the user if he/she wants to roll again