# download https://github.com/Hamy-os/computer-outro/raw/main/outro.mp3 and save it to the desktop

import requests
import os 

def installer(link1, link2, link3):
    
    outroURL = "https://github.com/Hamy-os/computer-outro/raw/main/outro.mp3"

    print("Downloading the outro.mp3 file...")
    
    response = requests.get(outroURL)
    
    with open("outro.mp3", "wb")as file:
        file.write(response.content)
        
    print("Download complete.")

        
    print("Downloading Fake bsod...")

    response = requests.get(link1)

    with open("bsod.bat", "wb")as file:
        file.write(response.content)

    print("Success!")

    print("Downloading Real bsod...")

    response = requests.get(link2)

    with open("bsod.py", "w")as file:
        file.write(response.content)

    print("Success!")

    print("Downloading Shutdown.exe...")

    response = requests.get(link3)

    with open("shutdown.py", "w")as file:
        file.write(response.content)

    print("Success!")

    print("Installation complete.")
        
if __name__ == "__main__":
    installer()
