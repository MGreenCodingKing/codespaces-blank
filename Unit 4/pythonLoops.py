# create a function that will determine what 
# level of education a college student is in
# based on the number of years they've been in
# school.

# undergrad 1 freshman, 2 sophmore, etc...
# 5> masters degree, doctorate degree, etc...

def gradeToTitle():
    year = int(input ('what grade are you in.'))
    if year == 1: 
        print('you are a freshman in undergrad.')
    elif year == 2:
        print('you are a sophmore in undergrad.')
    elif year == 3:
        print('you are a junior in undergrad.')
    elif year == 4:
        print('you are a senior in undergrad.')
    elif year == 5 or year == 6:
        print('you are in a masters program and in grad school')
    elif year >= 7  and year <= 10:
        print('you are in doctorates program and in grad school')
    elif year > 11:
        print('yo u need to go get a job. you been in school to long.')
    else:
        print('Err: something went wrong. please check your imput.')
    

gradeToTitle()