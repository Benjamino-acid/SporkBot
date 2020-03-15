import sys

def echo(user_input):
    print(user_input)
    return()

if sys.argv[1].lower() == ("help"):
    print("Echo Help")
    print("The echo command will simply return your words back to you.")
    print("Kind of like an echo")
    print("\tUsage:  /spork echo [what you want to echo]")

else:
    echo(' '.join(map(str, sys.argv[1:])))
