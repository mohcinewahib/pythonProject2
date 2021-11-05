def observed():
    observations = []
    input("Enter number of observations: ")
    for i in range(0, 7):
        valu = (input())
        observations.append(valu)
        return observations


def run():
    print("Counting observations...")
    o = observed()
    e = set()
