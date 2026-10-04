class QuitRequested(Exception):
    pass

def floatIn() -> float:
    while True:
        s = input().strip()
        if s.lower() == "quit":
            raise QuitRequested
        try:
            return float(s)
        except ValueError:
            print("Invalid Input")

def intIn() -> float:
    while True:
        s = input().strip()
        if s.lower() == "quit":
            raise QuitRequested
        try:
            return int(s)
        except ValueError:
            print("Invalid Input")

def subDivision():
    print("Interior Width:")
    insideWidth = floatIn()
    print("Number of Subdivisions (pockets) wanted:")
    pockets = intIn()
    print("Divider Thickness:")
    divider = floatIn()

    pocketWidth = (insideWidth - (pockets - 1) * divider) / pockets
    pocketCenter = pocketWidth + divider
    pocketOutsideWidth = pocketWidth + 2 * divider

    print("Pocket Width, interior to interior:")
    print(pocketWidth)
    
    print("Pocket Width, center to center:")
    print(pocketCenter)

    print("Pocket Width, exterior to exterior:")
    print(pocketOutsideWidth)

def run() -> int:
    try:
        subDivision()
    except QuitRequested:
        return 0
    return 0
