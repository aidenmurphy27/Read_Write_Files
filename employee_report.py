import csv  

infile = open('employee_data.csv', 'r')
reader = csv.reader(infile)
next(reader)  

data = list(reader)

print('Highly Efficient Individuals:')

for row in data:
    name = row[1]
    age = (row[2])
    hours_worked = float(row[4])
    productivity = float(row[5])

    efficiency = productivity/hours_worked

    if efficiency > 2:
        print(name)

print()
print()
print('Low Efficiency Individuals:')

for row in data:
    name = row[1]
    age = float(row[2])
    hours_worked = float(row[4])
    productivity = float(row[5]) 

    efficiency = productivity/hours_worked

    if efficiency < 1:
        print(name)

print()
print()

print('Employees in their 40s:')
i = 0 
for row in data:
    name = row[1]
    age = float(row[2])

    if age >= 40:
        print(name)
        i += 1

print(f"Total number of employees in their 40s: {i}")    

print()
print()

print('Employees in their 30s:')
i = 0 
for row in data:
    name = row[1]
    age = float(row[2])

    if age >= 30 and age < 40:
        print(name)
        i += 1

print(f"Total number of employees in their 30s: {i}")

print()
print()

print('Employees in their 20s:')
i = 0 
for row in data:
    name = row[1]
    age = float(row[2])

    if age >= 20 and age < 30:
        print(name)
        i += 1

print(f"Total number of employees in their 40s: {i}")