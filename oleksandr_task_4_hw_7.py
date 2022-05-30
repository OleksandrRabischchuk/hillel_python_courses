#month_number = int(input('insert month please: '))
#def number_month(month_number):
    #if month_number == 1:
        #return 'January'
    #elif month_number == 2:
        #return 'February'
    #elif month_number == 3:
        #return 'March'
   # elif month_number == 4:
        #return 'April'
    #elif month_number == 5:
        #return 'May'
    #elif month_number == 6:
        #return 'June'
    #elif month_number == 7:
        #return 'July'
    #elif month_number == 8:
        #return 'August'
    #elif month_number == 9:
        #return 'September'
    #elif month_number == 10:
        #return 'October'
    #elif month_number == 11:
        #return 'November'
    #elif month_number == 12:
        #return 'December'
#print(number_month(month_number))


numbers_month_of_year = int(input('insert your number month: '))

def season(numbers_month_of_year):
    if numbers_month_of_year == 1 or numbers_month_of_year == 2:
        return 'Winter'
    elif 2 < numbers_month_of_year <= 5:
        return 'Spring'
    elif 5 < numbers_month_of_year <= 8:
        return 'Summer'
    elif 8 < numbers_month_of_year <= 11:
        return 'Autumn'
    elif numbers_month_of_year == 12:
        return 'Winter'

print(season(numbers_month_of_year))

