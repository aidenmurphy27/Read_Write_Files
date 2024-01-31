import csv

infile = open('employee_data.csv', 'r')

csv_file = csv.reader(infile)
next(csv_file)

for i in csv_file:
    print(f"Name:  {i[1]}")
    print(f"{'Salary: $'}{i[3]}:>10,.2f")
    #print(f"Bonus:  $")
    #print(f"Pay:    $")
