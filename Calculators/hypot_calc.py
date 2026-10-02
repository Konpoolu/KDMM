import math

def numIn() -> float:
    while True:
        try:
            return float(input())
        except ValueError:
            print("Invalid Input")

def hypot() -> float:
    while True:
        print("Leg One:")
        legOne = numIn()
        print("Leg Two:")
        legTwo = numIn()
        
        legOneSq = legOne ** 2
        legTwoSq = legTwo ** 2

        legFinal = math.sqrt(legOneSq + legTwoSq) 
        return legFinal

def run() -> int:
    print(hypot())
