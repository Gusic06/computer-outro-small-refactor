
# Packages necessary to run
import time
import subprocess
import os
from pygame import mixer

def fakeBsod():
    # Find and play sound (if in the same folder as this file)
    outroSound = os.path.join(os.getcwd(), 'outro.mp3')
    if os.path.exists(outroSound):
        mixer.init()
        mixer.music.load(outroSound)
        mixer.music.play()
    else:
        raise FileNotFoundError("Couldn't find outro.mp3.")

    time.sleep(0.1)
    for loopTime in range(10)[::-1]: #[::-1] <- Reverses the for loop countdown | A normal loop countdown would be "1, 2, 3, 4" but a reversed one would be "4, 3, 2, 1"
        if loopTime == 0:
            print("Shutting down now!")
            time.sleep(1.25)
        else:
            print(f"Shutting down in: {loopTime} Seconds")
            time.sleep(0.75)

    batFilePath = str(f"{os.path.dirname(__file__)}\\bsod.bat")
    
    try:
        subprocess.call([batFilePath])
    except:
        os.system(batFilePath)

if __name__ == "__main__":
    fakeBsod()
