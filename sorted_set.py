def observed():
    observations = []
    while i <= 5:
        val = input("enter an observation: ")
        observations.append(val)
        i += 1
    return observation


def remove_observations(o):
    o = observed()
    cho = input("Do you wish to remove an observation (yes/no)? ")
    if cho == "yes":
        ob = input("What observation do you wish to remove?")
        o.remove(ob)


def run():
    fi = observed()

