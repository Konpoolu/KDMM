import math

class QuitRequested(Exception):
    pass

def numIn() -> float:
    while True:
        s = input().strip()
        if s.lower() == "quit":
            raise QuitRequested
        try:
            return float(s)
        except ValueError:
            print("Invalid Input")
    

def mLeg() -> float:
    while True:
        print("Hypotenuse:")
        hypot = numIn()
        print("Given Leg:")
        givenLeg = numIn()
        
        if hypot <= 0 or givenLeg <= 0:
            print("Side(s) must be positive")
            continue

        hypotSq = hypot ** 2
        legSq = givenLeg ** 2

        if ((hypotSq-legSq)>0):
            legFinal = math.sqrt(hypotSq - legSq)
            return legFinal
        else:
            print("Hypotenuse does not exist for given triangle")


def run() -> int:
    try:
        print(mLeg())
    except QuitRequested:
        return 0
    return 0
