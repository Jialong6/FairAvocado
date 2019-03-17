import csv

with open('AvocadoPrice.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    head_row = next(csv_reader)
    dic = {}
    for row in csv_reader:
        combo = (row[0], row[1])
        dic[combo] = format(float(row[2]), '.2f')

def compare_price(tuple ,price):
    average = dic[tuple]
    if price >= average:
        return 'Fair'
    else:
        return 'Unfair'



def readinuser(region='TotalUS', Type='None', userPrice=None):
    region = str(region)
    Type = str(Type)
    if type(userPrice) != int and type(userPrice) != float:
        return("Please input a valid number for price")
    if userPrice <= 0.00:
        return("This only for single avocado price check. Your input is unreasonable :/")
    if userPrice > 5.00:
        return("This only for single avocado price check. Your input is unreasonable :/")
    output = {}
    userPrice = round(userPrice, 2)
    keys = (region, Type)
    output[keys] = userPrice
    return output