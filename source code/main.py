from realBsod import bsod
from fakeBsod import fakeBsod
from installer import installer
from shutdown import shutdown
from divider import divider
import PyInstaller.__main__
import time
import sys
import os

#Note that this file is meant to run as an executable as the main installer of sorts
###################################################################
loop = True

while loop == True: #We need this loop because otherwise it does some wacky ass shit that is driving me insane
    
    installer("https://github.com/Gusic06/computer-outro-small-refactor/raw/main/bsod.bat",
         "https://github.com/Gusic06/computer-outro-small-refactor/raw/main/source%20code/realBsod.py",
         "https://github.com/Gusic06/computer-outro-small-refactor/raw/main/source%20code/shutdown.py",
         "https://github.com/Gusic06/computer-outro-small-refactor/raw/main/source%20code/fakeBsod.py")
    
    loop = False

###################################################################

fakeBsodInit = """import PyInstaller.__main__ 

PyInstaller.__main__.run([
    "fakeBsod.py",
    "--onefile"
])"""
# ^ This is the code that we are executing here
try:
    exec(fakeBsodInit) #Normally using exec() is a pretty terrible idea but here it should be fine as all we are doing is making fakeBsod.py into an executable
except:
    raise Exception("An error occured, maybe try reinstalling?")
    
###################################################################
divider()

shutdownInit = """import PyInstaller.__main__
    
PyInstaller.__main__.run([
    "shutdown.py",
    "--onefile"
])
"""
try:
    exec(shutdownInit)
except:
    raise Exception("An error occured, maybe try reinstalling?")

###################################################################
divider()

realBsodInit = """import PyInstaller.__main__

PyInstaller.__main__.run([
    "realBsod.py",
    "--onefile"
])
"""
try:
    exec(realBsodInit)
except:
    raise Exception("An error occured, maybe try reinstalling?")

###################################################################
divider()

print("Download completed!")

for loopTime in range(6)[::-1]: #Counts down from 5 not 6, don't ask me why because I don't know
    if loopTime == 0:
        time.sleep(1)
        print("Exiting program.")
        sys.exit()
    else:
        time.sleep(1)
        print(f"Exiting program in {loopTime}.")
