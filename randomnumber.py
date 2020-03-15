import sys
from random import randint

def get_number(start, end):
    return(randint(int(start), int(end)))

def return_help():
    print("Random Number Help")
    print("This will return a random number between two values inclusively")
    print("\tusage : /spork randomnumber [number 1] [number 2]")
    print("\t\tNote : First value must be smaller than second value")

if (sys.argv[1].lower() == "help"):
    return_help()

else:
    try: print(get_number(sys.argv[1], sys.argv[2]))
    except ValueError: print("Error : Try '/spork randomnumber help' for usage options")
    
