import webbrowser , sys, pyperclip

# Defining the arguments to be read.
sys.argv

# Checking if the argument is valid and storing the address in a valid from the input.
if len(sys.argv) > 1:
    address = "".join(sys.argv[1:])
else:
    address = pyperclip.paste()

# Opening the google maps place in the browser from the stored address.
webbrowser.open("https://www.google.com/maps/place/" + address)