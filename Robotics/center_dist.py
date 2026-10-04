import math

class QuitRequested(Exception):
    pass

def numIn() -> int:
    while True:
        s = input().strip()
        if s.lower() == "quit":
            raise QuitRequested
        try:
            return int(s)
        except ValueError:
            print("Invalid Input")

def belt() -> float:
    print("Belt Pitch (in millimeters):")
    beltP = numIn()
    print("Belt Teeth:")
    beltT = numIn()
    print("Pulley One Teeth:")
    pOneTeeth = numIn()
    print("Pulley Two Teeth:")
    pTwoTeeth = numIn()

    pitchLength = beltP * beltT
    pOneDia = (pOneTeeth * beltP)/math.pi
    pTwoDia = (pTwoTeeth * beltP)/math.pi
    K = pitchLength - (math.pi/2) * (pOneDia + pTwoDia)

    if (pTwoDia > pOneDia):
        temp = pOneDia
        pOneDia = pTwoDia
        pTwoDia = temp
    
    centerD = (K + math.sqrt(K ** 2 - (8 * (pOneDia - pTwoDia) ** 2))) / 8
    return centerD

def run() -> int:
    try:
        print(belt())
    except QuitRequested:
        return 0
    
    return 0
