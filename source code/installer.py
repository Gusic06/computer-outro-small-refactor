# download https://github.com/Hamy-os/computer-outro/raw/main/outro.mp3 and save it to the desktop

import requests
import time
import os 

def installer(link1, link2, link3, link4):
    
    loop = True
    
    while loop == True: #We need to use this while loop because without it the program does some wacky ass shit for no reason

        outroURL = "https://github.com/Hamy-os/computer-outro/raw/main/outro.mp3"

        print("Downloading the outro.mp3 file...")

        response = requests.get(outroURL)

        with open("outro.mp3", "wb")as file:
            file.write(response.content)

        print("Download complete.")

        print("Downloading bsod.bat...")

        response = requests.get(link1)

        with open("bsod.bat", "wb")as file:
            file.write(response.content)

        print("Success!")

        print("Downloading Real bsod...")

        response = requests.get(link2)

        with open("bsod.py", "wb")as file:
            file.write(response.content)

        print("Success!")

        print("Downloading Shutdown.exe...")

        response = requests.get(link3)

        with open("shutdown.py", "wb")as file:
            file.write(response.content)

        print("Success!")

        print("Downloading Fake bsod...")

        response = requests.get(link4)

        with open("fakeBsod.py", "wb")as file:
            file.write(response.content)

        print("""Part 1 of installation complete.
    Now beginning 2nd half of installation...""")
        time.sleep(1)
        
        loop = False
        
if __name__ == "__main__":
    installer()
