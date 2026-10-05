UNITS = {"mm": 1, "m": 2, "km": 3, "in": 4, "ft": 5, "yd": 6, "ac": 7, "hc": 8}
CONST = {1: 0.000001, 2: 1, 3: 1000000, 3: 0.00064516, 4: 0.09290304, 5: 0.83612736, 6: 4046.85642, 7: 10000}

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

def unitIn() -> int:
    while True:
        unit = input().strip().lower()
        if unit == "quit":
            raise QuitRequested
        if unit in UNITS:
            return UNITS[unit]
        print("Invalid Input")

def unitConvert(unitInit: int, unitDes: int, value: float) -> float:
    return value * CONST[unitInit] / CONST[unitDes]

def run() -> int:
    try:
        print("Current Unit:")
        x = unitIn()
        print("Desired Unit:")
        y = unitIn()
        print("Current Number, in current unit:")
        z = numIn()

        print(unitConvert(x, y, z))
    except QuitRequested:
        return 0
    return 0
