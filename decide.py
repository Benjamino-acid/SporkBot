import sys
from random import randint

def get_decision():
    sentence = (' '.join(map(str, sys.argv[1:])))
    parts = sentence.split(' or ')
    value = randint(0, (len(parts) - 1))
    return(parts[value])

def get_response(decision):
    responses = ["Hmmm... I think that " + str(decision) + " is an excellent choice!",
                 "Lets go with " + str(decision) + ".",
                 "That's an easy one: " + str(decision) + "!",
                 "The spork has decided: " + str(decision) + "."]
    return(responses[randint(0, len(responses) - 1)])

def return_help():
    print("Decide Help")
    print("The Decide command can help you make decisions between multiple options")
    print("\tUsage:  /spork decide [option 1] or [option 2] or ...")
    print("\t\tNote: Separate each option with 'or'")

if(sys.argv[1].lower() == "help"): return_help()

else:
    try:
        print(get_response(get_decision()))
    except ValueError:
        print("Error : try /spork decide help for usage information")

 

    
    
