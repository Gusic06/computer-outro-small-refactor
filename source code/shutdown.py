
# Packages necessary to run
import time
import subprocess
import os
from pygame import mixer

def shutdown():
    
    # Find and play sound (if in the same folder as this file)
    outroSound = os.path.join(os.getcwd(), 'outro.mp3')
    if os.path.exists(outroSound):
        mixer.init()
        mixer.music.load(outroSound)
        mixer.music.play()
    else:
        raise FileNotFoundError("Couldn't find outro.mp3.")

    time.sleep(0.1)
    
    for loopTime in range(10)[::-1]:
        if loopTime == 0:
            print("Shutting down now!")
            time.sleep(1.25)
        else:
            print(f"Shutting down in: {loopTime} Seconds")
            time.sleep(0.75)

    # Shutdown
    
    try: #Trying this way first and if that doesn't work the except codeblock is executed
        subprocess.call(["shutdown", "/s", "/t", "1"])
    except:
        print("""subprocess.call failed,
trying os.system...""")
        os.system("shutdown /s /t 1")
    
if __name__ == "__main__":
    shutdown()
