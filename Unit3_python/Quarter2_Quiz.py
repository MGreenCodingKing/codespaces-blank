# A function is a block of code which only runs when it is called.

# You can pass data, known as parameters, into a function.

# A function can return data as a result.
# A function parameter is a variable name listed within 
# A function definition that acts as a placeholder for data,
# while a function argument is the actual value passed to that
# parameter when the function is called.

# An "if/else" conditional statement in programming 
# is a decision-making structure that allows a program to execute
# different blocks of code depending on whether a 
# specified condition is true or false


# integer data type stores numbers.

# a boolean data type that can only hold two values: "true" or "false"

def verifyAge(age):
    if age > 17 and age < 20:
        print('congrats! you can buy GTA VI')
    elif age > 20:
        print('sorry youre to old for this game.')
    else:
        verifyAge(69)


# numbers or special characters that you put in your password

def check_password_length(password):
    """
    Checks if a given password is between 4 and 10 characters long. 
    
    Args:
        password (str): The password to check.
        
    Returns:
        str: A message indicating whether the password meets length criteria. 
    """
    
    if len(password) < 4:
        return "Password is too short. Please enter a password with at least 4 characters."
    elif len(password) > 10:
        return "Password is too long. Please enter a password with a maximum of 10 characters."
    else:
        return "Password created successfully!" 
    
# Example usage: 
check_password_length = input("Enter your password: ")
print(check_password_length(dumb))





def moneytotaxes(tax)
   
# If a user makes between 0.00 and 12000.00 per year, they will be taxed 10%, 
   plus an additional 3% for the state.

# If a user makes between 12001.00 and 50000.00 per year, they will be taxed 12%, 
# plus an additional 3% for the state.

 #If a user makes between 50001.00 and 103000.00, they will be taxed 22%, 
# plus and additional 3% for the state.

# If a user makes between 103001.00 and 198000.00, they will be taxed 23%, 
# plus and additional 3% for the state.



# i can go to cheney
# i can  not go to penn state
# i can go to temple
# i can go to university of Pennsylvania.







