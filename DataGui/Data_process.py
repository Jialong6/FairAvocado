import csv
import tkinter
from tkinter import messagebox

with open('AvocadoPrice.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    head_row = next(csv_reader)
    dic = {}
    for row in csv_reader:
        combo = (row[0], row[1])
        dic[combo] = format(float(row[2]), '.2f')

def compare_price(tuple ,price):
    average = float(dic[tuple])
    root = tkinter.Tk()
    if price >= average:
        root.withdraw()
        messagebox.showinfo("Information", "Unfair")
    elif price < average:
        root.withdraw()
        messagebox.showinfo("Information", "Fair")



def readinuser(region='TotalUS', Type='None', userPrice=None):
    region = str(region)
    Type = str(Type)
    root = tkinter.Tk()
    if type(userPrice) != int and type(userPrice) != float:
        root.withdraw()
        messagebox.showerror("Error", "Please input a valid number for price")
    if userPrice <= 0.00:
        root.withdraw()
        messagebox.showerror("Error", "This only for single avocado price check. Your input is unreasonable :/")
    if userPrice > 5.00:
        root.withdraw()
        messagebox.showerror("Error", "This only for single avocado price check. Your input is unreasonable :/")
    output = {}
    userPrice = round(userPrice, 2)
    keys = (region, Type)
    output[keys] = userPrice
    return region, Type

#Please input a valid number for price
#This only for single avocado price check. Your input is unreasonable :/
#This only for single avocado price check. Your input is unreasonable :/