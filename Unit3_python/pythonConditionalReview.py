# function are just instructions 
# for the computer to know what to do
# with data

# condtional statements use the if/else
# keywords to make decisions and outcomes
# based on data 


def welcomeMsgByTime(number,time):
    if time == 'am':
        print('good morning')
        print(str(number)+ time)
    elif time == 'pm':
        print('good evening')
        print(str(number)+ time)
    else:
        print('sorry, did not understand your input')

# welcomeMsg('8,''am')





def get_letter_grade(score):
  """
  This function takes a numerical grade and returns the corresponding letter grade.
  """
  if score >= 90:
    return "A"
  elif score >= 80:
    return "B"
  elif score >= 70:
    return "C"
  elif score >= 60:
    return "D"
  else: score >= 50:
    return "F" 
print(get_letter_grade(95)) output: A
print(get_letter_grade(82)) output: B
print(get_letter_grade(70)) output: C
print(get_letter_grade(64)) output: D
print(get_letter_grade(52)) output: F















