import csv


with open("frukt.csv", "r") as file:
     reader = csv.reader(file)
     for row in reader:
         print(row)