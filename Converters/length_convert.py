UNITS = {"mm": 1, "cm": 2, "m": 3, "km": 4, "in": 5, "ft": 6, "yd": 7, "mi": 8}
CONST = {1: 0.001, 2: 0.01, 3: 1.0, 4: 1000.0, 5: 0.0254, 6: 0.3048, 7: 0.9144, 8: 1609.344}

def numIn() -> float:
    while True:
        try:
            return float(input())
        except ValueError:
            print("Invalid Input")

def unitIn() -> int:
    while True:
        unit = input().strip().lower()
        if unit in UNITS:
            return UNITS[unit]
        print("Invalid input.")

def unitConvert(unitInit: int, unitDes: int, value: float) -> float:
    return value * CONST[unitInit] / CONST[unitDes]

def run() -> int:
    print("Current unit:")
    x = unitIn()  
    print("Desired unit:")
    y = unitIn()  
    print("Current number, in current unit:")
    z = numIn()
    
    converted = unitConvert(x, y, z)
    print(converted)

    return 0
