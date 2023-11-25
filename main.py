import statistics

members = []
total = 0
with open("test.txt") as outfile:
    for line in outfile:
        line = line.replace("\n", "")
        members.append(int(line))
        total = statistics.mean(members)
        print(members)
print(total)
