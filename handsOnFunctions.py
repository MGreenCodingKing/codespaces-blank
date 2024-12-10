# Discuss the anatomy of a function

# A function definition tells the computer
# the instructions on what we want to do with

# data = just means data types

#curly brackets = passing in data
# the unction definition. THis is formally
# called a parameter

#parameter = placeholder

def modifyMyName(name):
    print('Your new modified name is the great'+ name)

    # when we pass data into a function call it is called an
    #arguement
    #argeument = evidence, facts, real data

# modifyMyName('Mr.Green')

# Lesson on conditional Statments



# Lesson on conditional Statements
# conditional statements use the 'If' and 'Else'
# keywards to filter and create specific outcomes
# based on data

def verifyAge(age):
    if age > 17 and age < 20:
        print('congrats! you can buy GTA VI')
    elif age > 20:
        print('sorry youre to old for this game.')
    else:
        verifyAge(69)

def MinutesConverter(hours):
    print(hours* 60)    
     
MinutesConverter(3)

# Conditional statements
#if /else keywords; gives us the abilty to
# control outcomes and make decisions on data

# food expiration software is an example of 
# using conditional statements. if the food expires
# it needs to be thrown away, otherwise or else
# it can be eaten.

def foodExperation(month, date, year):
    experationMonth = 12
    experationDate = 5
    experationYear = 2026
    if date > experationDate and experationMonth and year > experationDate:
        print('thrown food away.')
    else:
        print('food is still good.')

        foodExperation(12, 8, 2024)