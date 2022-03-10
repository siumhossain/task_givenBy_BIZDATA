
from datetime import datetime


def findAge(current_day,current_month,current_year,birth_day,birth_month,birth_year):
    if current_month < birth_month and current_day < birth_day:
        current_month = current_month - 1
        current_day = current_day + 30
        current_year = current_year - 1      
        current_month = current_month + 12
    elif current_day < birth_day:
        current_month = current_month -1
        current_day = current_day + 30
    elif current_month < birth_month:
        current_year = current_year - 1
        current_month = current_month + 12
    
    result_day = current_day - birth_day
    result_year = current_year - birth_year
    result_month = current_month - birth_month
    print(f'Age:{result_year} year | {result_month} month| {result_day} day')


currentDay :int= datetime.now().day
currentMonth :int= datetime.now().month
currentYear :int= datetime.now().year

def checkAge(message):
    
       
    
    while True:
        try:
            birth_day = int(input(message))

        except ValueError:
            print("the input must be in number")
        else:
            if birth_day not in range(1,32):
                print('wrong date [date should be in 1-31]')
            else:
                return birth_day
def checkMonth(message):
    
       
    
    while True:
        try:
            birth_month = int(input(message))

        except ValueError:
            print("the input must be in number")
        else:
            if birth_month not in range(1,13):
                print('wrong date [Month should be in 1-12]')
            else:
                return birth_month
def checkYear(message):
    
       
    
    while True:
        try:
            birth_year = int(input(message))

        except ValueError:
            print("the input must be in number")
        else:
            if len(str(birth_year)) != 4:
                print('wrong year [year should be in 4 digits]')
            else:
                return birth_year
birth_day = checkAge("Day?\n")
birth_month = checkMonth("Month?\n")
birth_year =  checkYear("Year?\n")


findAge(currentDay,currentMonth,currentYear,birth_day,birth_month,birth_year)

