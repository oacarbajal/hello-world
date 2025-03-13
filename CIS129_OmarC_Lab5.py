# Module 5 Lab-3
# Omar Carbajal
# 03/05/2025
# this program calculates total amount per bottles returned.
# Lab 5 The Bottle Return Program

# Declare variables below 
def main():
    keepGoing = 'y'
    while keepGoing =='y':
        totalBottles = getBottles()
        totalPayout = calcPayout(totalBottles)
        printinfo(totalBottles, totalPayout)
        print()
       
        keepGoing = input ('Do you want to end the program? (Enter y or n):')
  
#this function gets the number of bottles returned.
def getBottles():
    totalBottles = 0
    todayBottles = 0
    counter = 1
    while counter <=7:
        todayBottles =  int(input(f"Enter number of bottles for the day #{counter}: "))
        totalBottles = totalBottles + todayBottles
        counter = counter + 1   
    return totalBottles
    

# code to calculate the total payout        
def calcPayout(totalBottles):  
    totalPayout = 0 
    totalPayout = totalBottles*.10
    return totalPayout
   
# code to print the totalPayout
def printinfo(totalBottles, totalPayout):
    print ('the total number of bottles collected is' ,totalBottles)
    print('The total paid out is: $', format(totalPayout, '.2f'))

  
#calls main
main() 