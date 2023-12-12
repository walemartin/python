import csv

student_score = [
    ["Olawale Olasupo", 88],
    ["Tolulope Charles", 75],
    ["Dare Bakare", 54]
]
FILENAME = "student_score.csv"
with open(FILENAME, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(student_score)
    print("record(s) updated")