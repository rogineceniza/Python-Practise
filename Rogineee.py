# print("Yohoo")
#
# # #Input displaying length of characters
# # name = input("Hello! Tell me your name and I will tell you how many characters there is: ")
# # print("Hello " + name + "!" + " There are " + str(len(name)) + " characters in your name.")
# or
# print("You have " + str(len(input("What is your name? :"))) + " characters")
#
# #Interchanging inputs
# num1 = input("Enter random number for a: ")
# num2 = input("Enter another random number for b: ")
# num3 = num1
# num1 = num2
# num2 = num3
# print("a: " + num1)
# print("b: " + num2)
#
# print("\tRandom name Generator")
# name = input("Spell your name backwards: ")
# color = input("Current color of your shirt: ")
# food = input("Most recent food you ate: ")
# fear = input("What is your biggest fear: ")
# print(name + ", hoarder of " + color + " " + food + " with a sprinkle of " + fear)
#
# #adding 2 digits
# number = input("Enter 2 digits: ")
# num1 = number[0]
# num2 = number[1]
# sum = int(num1) + int(num2)
# print(str(num1) + " + " + str(num2) + " = " + str(sum))
#
# #BMI
# weight = input("Enter your weight in kg: ")
# height = input("Enter your height in m: ")
# weight1 = int(weight)
# height1 = float(height)
# bmi = weight1 / (height1 ** 2)
# print("%0.2f" % bmi)
#
# #Rounding numbers
# print(round(8/3,2))
# remainder = (3/10)
# print("%0.3f" % remainder)
#
# #f-String
# score = 0
# height = 1.8
# isWinning = True
# #print("Your score is " + score) // needs type casting which is hasol na
# print(f"Your score is {score}, your height is {height}. But are you winning tho? : {isWinning}" )
#
# #Days, months, years
# age = input("Enter your age: ")
# ageToInt = int(age)
# yearsRemaining = 90 - ageToInt
# months = yearsRemaining * 12
# weeks = yearsRemaining * 52
# days =yearsRemaining * 365
# print(f"You are {age}.\nYears remaining: {yearsRemaining}.\nMonths remaining: {months}\nDays remaining: {days}")
#
# #Tip Calculator
# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill?: "))
# percentage = int(input("What percentage would you like to give? 10, 12, 15: "))
# people = int(input("How many people to split the bill: "))
# perc = percentage / 100
# tip = bill * perc
# add = bill + tip
# eachPerson = add / people
# print(f"Total bill: {bill}\nPercentage: {percentage}\nHow many people to split the bill: {people}")
# rounded = round(eachPerson,2)
# print(f"Each person should pay: {eachPerson}")
#
#  # Else if
# print("Hello, Welcome to DisneyLand!")
# wannaRide = input("Wanna Ride?\nPress 1 to ride\nPress 2 to watch\n: ")
# if wannaRide == "1":
#     print("Press 1 to ride the ROLLER COASTER\nPress 2 to ride the FERRIS WHEEL")
#     ride = input(": ")
#     if ride == "1":
#         height = int(input("Enter height: "))
#         if height >= 120:
#             print("You are allowed to ride on the Roller Coaster!")
#         else:
#             print("Uh-oh, you're too short I'm afraid, maybe later...")
#     elif ride == "2":
#         height = int(input("Enter height: "))
#         if height >= 120:
#             print("You are allowed to ride on the Ferris Wheel!")
#         else:
#             print("Uh-oh, you're too short I'm afraid, maybe later...")
#     else:
#         print("Taronga sad nag type ara noh")
# else:
#     print("Sit back, relax and enjoy the show!")
#
#
# #IF ELSE BMI
# print("BMI CLACULATOR")
# height = float(input("Enter your height in meters(m): "))
# weight = int(input("Enter your weight in kilograms(kg): "))
#
# bmi = weight / height ** 2
# roundedBmi = round(bmi,2)
# print(f"Your BMI is: {roundedBmi}")
# if bmi <= 18.5:
#     print("Your are Underweight")
# elif bmi >= 18.5 and bmi <= 25:
#     print("You are Normal")
# elif bmi >= 25 and bmi <= 29.9:
#     print("You are Overweight")
# elif bmi >= 30:
#     print("You are Obese")
# else:
#     print("I'm sorry, this does not fall under BMI classification")
#
# #LEAP YEAR
# print("Leap Year")
# YesNo = "1"
# while YesNo == "1":
#     isLeapYear = int(input("Enter a year: "))
#     if isLeapYear % 4 == 0:
#         if isLeapYear % 100 == 0:
#             if isLeapYear % 400 == 0:
#                 print("LEAP YEAR!\n")
#             else:
#                 print("Not a Leap Year\n")
#         else:
#             print("LEAP YEAR!\n")
#     else:
#         print("Not a Leap Year\n")
#
#     YesNo = input("Press 1 to ENTER\nPress 2 to EXIT\n:")
#
#     if YesNo == "2":
#         break
#
# #Bills for kids, youth and adults
# print("Roller Coaster Ride")
# height = int(input("Enter height in cm: "))
# bill = 0;
#
# if height >= 120:
#     print("You are allowed to ride the rollercoaster!")
#
#     age = int(input("Enter Age: "))
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7.")
#     elif 45 <= age <= 55:
#         print("The rides are free. Enjoy!")
#     else:
#         bill = 12
#         print("Adult tickets are $12.")
#
#     wantsPhotos = input("Do you want a photo op? Y/N: ")
#     if wantsPhotos == 'Y' or 'y':
#         bill += 3
#         wantsBracelets = input("Want bracelets? Y/N: ")
#         if wantsBracelets == 'Y' or 'y':
#             bill += 2
#             wantsDrinks = input("Want Drinks? Y/N: ")
#             if wantsDrinks == 'Y' or 'y':
#                 bill += 4
#                 print(f"Total Bills: ${bill}")
#             else:
#                 print(f"Total Bill: ${bill}")
#         else:
#             print(f"Total Bill: ${bill}")
#     else:
#         print(f"Total Bill: ${bill}")
# else:
#     print("Oh, maybe the kiddie table would be a perfect place for such tiny creature like you sweetie BWAHAHHA")
#
# #Using count() funstion // is very case sensitive
# print("Welcome To L Calculator\n")
# name1 = input("Enter your name: ")
# name2 = input("Enter the other person's name: ")
# names = name1 + name2
# names.lower()
# t = names.count("t")
# r = names.count("r")
# u = names.count("u")
# e = names.count("e")
# true = str(t+r+u+e)
# l = names.count("l")
# o = names.count("o")
# v = names.count("v")
# e = names.count("e")
# love = str(l+o+v+e)
# score = int(true + love)
# if  1 <= score <= 20:
#     print(f"Your score is {score}. Couldn't say it's a match tho :<")
# elif 20 <= score <=30:
#     print(f"Your score is {score}. Hohohoho, I sense tingling hearts.")
# elif 30 <= score <= 50:
#     print(f"Your score is {score}. Oh boy!, could this be a match?")
# elif 50 <= score <= 70:
#     print(f"Your score is {score}. Sheeesh! get a room <3")
# elif 70 <= score <= 90:
#     print(f"Your score is {score}. GeeWizz! Is this destiny? Your fates are intertwined like braids.")
# elif score >= 90:
#     print(f"Your sore is {score}. I'll be throwing the bouquet okay? Hmmph! I'm getting a reservation on this.")
# elif score == 0:
#     print(f"Your score is {score}. Ummm...okay, maybe you guys aren't meant to be together. Cheers!")
# else:
#     print(f"WHOAHH!!! You just won the love lottery. Your score is {score}. CONGRATULATIONS!!!")

# #Ascii Art
# print('''
#    ___             __ _     _
#   | _ \    ___    / _` |   (_)    _ _      ___
#   |   /   / _ \   \__, |   | |   | ' \    / -_)
#   |_|_\   \___/   |___/   _|_|_  |_||_|   \___|
# _|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|
# "`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'
# ''')

import random

myRandom = random.random() # 0.10000 - 0.90000
print(myRandom)

myRandomInt = random.randint(0, 10) # from 0 - 10
print(myRandomInt)

myRandomFloat = random.random() * 5 # from 0.1000 - 5.000
rounded = round(myRandomFloat, 2)
print(rounded)

score = random.randint(1,100) # random number from 1 - 100
print(f"Your calculus score is {score}")


