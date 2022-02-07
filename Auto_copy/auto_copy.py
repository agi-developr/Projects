# Auto Copy clipboard
# This program writes everything you copied to a file
# How to use it:
# Run, clt+c, to reed open Notes.txt
import os
import sys
import time
import pyperclip

sys.path.append(os.path.abspath("SO_site-packages"))

recent_value = ""

D = time.strftime("%D")

while True:
    tmp_value = pyperclip.paste()
    if tmp_value != recent_value:
        recent_value = tmp_value
        print("Value changed: %s" % str(recent_value)[:20])
        with open("Notes.txt", "+a") as output:
            output.write(D + "\n\n")
            output.write("%s\n\n" % str(tmp_value))
            output.write("-------------------------\n\n\n")
    try:
        time.sleep(0.1)
    except KeyboardInterrupt:
        break
