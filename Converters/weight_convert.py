UNITS = {"mg": 1, "g": 2, "kg": 3, "metricton": 4, "oz": 5, "lb": 6, "uston": 7}
CONST = {1: 0.001, 2: 1, 3: 1000, 4: 1000000, 5: 28.349523125, 6: 453.59237, 7: 907184.74}

# Supported Units
    # MilliGrams
    # Grams
    # Kilograms
    # Metric Tons
    # Ounces
    # Pounds
    # US Ton

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
        unit = input().strip("s ").lower()
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
