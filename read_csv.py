import csv

customers = open('customers.csv', 'r')

csv_file = csv.reader(customers)

#to skip the header
next(csv_file)

for rec in csv_file:
    print(f" First Name: {rec[1]} Last Name: {rec[2]}")
    input()

print('Hello')
