import secrets
import math

def uniform(a: float = 0.0, b: float = 1.0) -> float:
    "Cryptographically secure uniform sample."
    # 53 random bits gives 53 bit precision double
    u = secrets.randbits(53)/ (1<<53) # in [0,1)
    return a + (b-a) * u

def exponentialdist(lambdaa: float) -> float:
    y = uniform() # call previous function that gives [0,1]
    if y == 0:
        y = uniform() # reroll 0s (The odds of two zeros back to back are very low)
    x = -(1/lambdaa)*math.log(y) # this cant take U=0 as an input
    return x

def poissondist(lambdaa):
    y = uniform()

    x = 0
    p = math.exp(-lambdaa)
    s = p
    while y > s:
        x += 1
        p = p*lambdaa/x
        s = s+p
    return x


