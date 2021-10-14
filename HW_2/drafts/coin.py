import random

def weighted_choice(seq, weights):

    rnd = random.random()
    j = 0
    print(rnd)
    while j < len(seq):
        if rnd <= weights[j]:
            return seq[j]
        else:
            rnd += weights[j]
            j += 1


print(weighted_choice("Bvi", [0.4, 0.1, 0.5]))
