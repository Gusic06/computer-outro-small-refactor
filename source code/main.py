from bsod import bsod
from fakebsod import fakeBsod
from installer import installer
from shutdown import shutdown
from divider import divider
import time
import os

###################################################################

installer("https://github.com/Gusic06/computer-outro-small-refactor-/blob/main/source%20code/realBsod.py", 
    "https://github.com/Gusic06/computer-outro-small-refactor-/blob/main/source%20code/fakebsod.py",
    "https://github.com/Gusic06/computer-outro-small-refactor/blob/main/bsod.bat",
    "https://github.com/Gusic06/computer-outro-small-refactor-/blob/main/source%20code/shutdown.py")

###################################################################

fakeBsodInit = """import PyInstaller.__main__

PyInstaller.__main__.run([
    "fakebsod.py",
    "--onefile"
])"""
    
exec(fakeBsodInit)

###################################################################
divider()

shutdownInit = """import PyInstaller.__main__
    
PyInstaller.__main__.run([
    "shutdown.py",
    "--onefile"
])
"""
    
exec(shutdownInit)
