import csv
with open('employee1.csv','r')as file1:
    reader1=csv.reader(file1)
    for row in reader1:
        print(row)
