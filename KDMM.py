import argparse, sys
from MISC import list
from Calculators import calc_sci, large_calc, hypot_calc, mLeg_calc
from Converters import length_convert, weight_convert
from Robotics import center_dist

APPS = {
    # comma, then next thing, then colon, then file name dot run
    # Everything in the MISC file
    "list": list.run,

    # Everything in the Calculators folder
    "hypot-calc": hypot_calc.run, 
    "mLeg-calc": mLeg_calc.run,

    # Everything in the Converters folder
    "length-convert": length_convert.run,
    "weight-convert": weight_convert.run,

    # Everything in the Robotics folder
    "center-dist": center_dist.run
}

def main() -> int:
    parser = argparse.ArgumentParser(prog="kdmm")
    parser.add_argument("app", choices=APPS)
    args = parser.parse_args()
    return APPS[args.app]()

if __name__ == "__main__":
    sys.exit(main())
