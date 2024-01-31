import csv

infile = open('customers.csv', 'r')
outfile = open('customer_country.csv', 'w')

csv_file = csv.reader(infile)
next(csv_file)

counter = 0 
outfile.write('Full Name, Country \n')

for i in csv_file:
    counter +=1
    outfile.write(f"{i[1]} {i[2]},{i[4]}\n")  

print('Total Count:', counter)

outfile.close
infile.close









