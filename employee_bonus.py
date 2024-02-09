import csv

infile = open('employee_data.csv', 'r')
reader = csv.reader(infile)
next(reader)  

for row in reader:
    emp_id = row[0]
    name = row[1]
    age = row[2]
    salary = float(row[3])
    bonus = float(row[7])
    
    calc_bonus = salary * (1 + bonus)
    calc_pay = calc_bonus + salary

    print(f"Name:  {name}")
    print(f"Salary: $ {salary:>10,.2f}")
    print(f"Bonus:  $ {calc_bonus:>10,.2f}")
    print(f"Pay:    $ {calc_pay:>10,.2f}")
    print()
    
infile.close