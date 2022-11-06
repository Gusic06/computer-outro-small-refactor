from bsod import bsod
from fakebsod import fakeBsod
from installer import installer
from shutdown import shutdown
from divider import divider
import PyInstaller.__main__
import time
import os

#Note that this file is meant to run as an executable as the main installer of sorts
###################################################################

installer("https://github.com/Gusic06/computer-outro-small-refactor-/blob/main/source%20code/realBsod.py", 
    "https://github.com/Gusic06/computer-outro-small-refactor-/blob/main/source%20code/fakeBsod.py",
    "https://github.com/Gusic06/computer-outro-small-refactor/blob/main/bsod.bat",
    "https://github.com/Gusic06/computer-outro-small-refactor-/blob/main/source%20code/shutdown.py")

###################################################################

fakeBsodInit = """import PyInstaller.__main__ 

PyInstaller.__main__.run([
    "fakeBsod.py",
    "--onefile"
])"""
# ^ This is the code that we are executing here

exec(fakeBsodInit) #Normally using exec() is a pretty terrible idea but here it should be fine as all we are doing is making fakeBsod.py into an executable

###################################################################
divider()

shutdownInit = """import PyInstaller.__main__
    
PyInstaller.__main__.run([
    "shutdown.py",
    "--onefile"
])
"""
    
exec(shutdownInit)

###################################################################
divider()

realBsodInit = """import PyInstaller.__main__

PyInstaller.__main__.run([
    "realBsod.py",
    "--onefile"
])
"""

exec(realBsodInit)
