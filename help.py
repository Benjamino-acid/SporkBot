import sys

def return_help():
    print("Help Menu")
    print("\tdecide => helps you to choose between many options")
    print("\tdefine => finds definitions to a word to help you understand")
    print("\techo => will simply echo back to you what you say")
    print("\thealth => returns usage statistics for SporkBot")
    print("\thelp => prints the commands available (this menu)")
    print("\tmytodo => helps you manage personal todo lists so you won't forget anything")
    print("\trandomnumber => will return a random number between two values, inclusively")
    print("\trandomword => returns a random word defaulting between 5 and 15 characters")
    print("\tsaxophone => TOP SECRET command")
    print("\ttodo => helps you manage todo lists over the whole channel")
    print("\tweather => can give you information on the current weather as well as forecasts")
    print("\t\tAdditional Help : type '/spork [command] help' to get usage help on a specific command")
    

if (len(sys.argv) == 0) or (sys.argv[1].lower() == "help"):
    return_help()

