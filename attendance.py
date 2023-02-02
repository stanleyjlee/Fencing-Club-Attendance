import numpy as np
import math
import glob
import os
from pathlib import Path

def load_read_data(file):
    file_open = open(file,'r')
    vari_name = file_open.readline().split(",")
    data_read = file_open.readlines()

    variables = []
    data_temp = []
    first = []
    last = []
    uin = []

    length = len(vari_name)
    

    #splitting and appending multiple lists to make one list comprised of the variable and its units
    for i in range(length):
        temp = vari_name[i].replace('\n','')
        variables.append(temp)

    for i in data_read:
        temp = []
        data_list = i.split(',')
        for j in data_list:
            temp2 = j.replace('\n','')
            temp2 = temp2
            temp.append(temp2)
        data_temp.append(temp)

    #print(variables)
    #print(data_read)
    #print(data_temp)
    count = 0

    for i in data_temp:
        first.append(i[0])
        last.append(i[1])
        uin.append(int(i[2]))
         

    #print(uin)

            
    #closing the file
    file_open.close()

    return first, last, uin

def total_check(first_total, last_total, uin_total):
    unique_uin = set(uin_total)
    for i in unique_uin:
        print(first_total[uin_total.index(i)], last_total[uin_total.index(i)], ":", uin_total.count(i))

def not_paid(first_total, last_total, uin_total):
    unique_uin = list(set(uin_total))
    
    data = load_read_data("paid.csv")
    #print(data)

    uin_not_paid = []

    uin_not_paid = [i for i in unique_uin if i not in data[2]]

    #print(uin_not_paid)

    for i in uin_not_paid:
        if uin_total.count(i) >= 3:
            print(first_total[uin_total.index(i)], last_total[uin_total.index(i)], ":",uin_total.count(i))

def paid():
    data = load_read_data("paid.csv")

    first_temp = []
    last_temp = []
    uin_temp = []

    for i in data[0]:
        first_temp.append(i)
    for i in data[1]:
        last_temp.append(i)
    for i in data[2]:
        uin_temp.append(i)
    
    for i in range(len(first_temp)):
        print(first_temp[i], last_temp[i], uin_temp[i])


#total being read
first_total = []
last_total = []
uin_total = []

#folder variable and location (and file type)
file_list = Path('./attendance-list').glob('*.csv')

#reading folder data and organizing the data into their respective variables
for file_path in file_list:
    data = load_read_data(file_path) #loading the data
    for i in data[0]:
        first_total.append(i) #appending to first name list
    for i in data[1]:
        last_total.append(i)
    for i in data[2]:
        uin_total.append(i)

print("Welcome to the fencing attendance script\n Please select an option: \n\n  Total Attendance -- 1 \n  Unpaid Dues ------- 2 \n  Paid Dues --------- 3 \n",)

running = True
user_input = input("Enter: ")

while(running):
    user_input = input("Enter: ")


    if user_input == '1':
        total_check(first_total, last_total, uin_total)
    elif user_input == '2':
        not_paid(first_total, last_total, uin_total)
    elif user_input == '3':
        paid()
    else:
        running = False

    print("Press Enter key to exit")
