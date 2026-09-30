import argparse, sys
from MISC import list

APPS = {
    "list": list.run
    # comma, then next thing, then colon, then file name dot run
}

def main() -> int:
    parser = argparse.ArgumentParser(prog="kdmm")
    parser.add_argument("app", choices=APPS)
    args = parser.parse_args()
    return APPS[args.app]()

if __name__ == "__main__":
    sys.exit(main())