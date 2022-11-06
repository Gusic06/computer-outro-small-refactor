#PyInstaller initialiser
import PyInstaller.__main__

PyInstaller.__main__.run([
    'main.py', #Name of file
    '--onefile' #Making it so only one executable is made
])
