import statistics


def read_numbers():
    members = []
    with open("test.txt") as outfile:
        for line in outfile:
            line = line.replace("\n", "")
            members.append(int(line))
    return members


def compute_mean(mean):
    total = statistics.mean(mean)
    print(round(total, 2))


compute_mean(read_numbers())