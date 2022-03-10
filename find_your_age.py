
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


while True:
    try:
        
        birth_day = int(input("birth_day? ex:1-31 \n"))
        if birth_day not in range(1,32):
            print('wrong date [date should be in 1-31]')
            birth_day = int(input("birth_day? ex:1-31 \n"))
        
        birth_month = int(input("birth_month? ex:1-12 \n"))
        if birth_month not in range(1,13):
            print('wrong month [date should be in 1-12]')
            birth_month = int(input("birth_month? ex:1-12 \n"))
        birth_year = int(input("birth_year? ex:1950\n"))
        findAge(currentDay,currentMonth,currentYear,birth_day,birth_month,birth_year)
        break
    except ValueError:
        print("the input must be in number")

