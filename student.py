import csv

with open("student_score.csv", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print("(" + str(row[1]) + ")")
