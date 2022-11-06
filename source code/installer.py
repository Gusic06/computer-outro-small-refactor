# download https://github.com/Hamy-os/computer-outro/raw/main/outro.mp3 and save it to the desktop

import requests
import os 

def installer(link1, link2, link3):
    
    outroURL = "https://github.com/Hamy-os/computer-outro/raw/main/outro.mp3"

    print("Downloading the outro.mp3 file...")
    
    response = requests.get(outroURL)
    open("outro.mp3", "wb").write(response.content)
    print("Download complete.")

    print("Please pick one.")
    choice = input("""There are 3 options: 
Option 1: Fake bsod (fakebsod.exe) 
Option 2: Real bsod (bsod.exe)  
Option 3: Shutdown (shutdown.exe)""")

    if choice == "1":
        
        print("Downloading Fake bsod...")
        
        response = requests.get(link1)
        
        with open("bsod.bat", "wb")as file:
            file.write(response.content)
            
        print("Success!")
        
        userChoice = input("Do you want to start fakebsod.exe? (Y/N) -> ").title()
        
        if userChoice == "Y":
            print("Starting fakebsod.exe...")
            os.system("start fakebsod.exe")
            
        elif userChoice == "N":
            print("fakebsod.exe was not executed.")
            
    elif choice == "2":
        
        print("Downloading Real bsod...")
        
        response = requests.get(link2)
        
        with open("bsod.exe", "wb")as file:
            file.write(response.content)
            
        print("Success!")
        
        userChoice = input("Do you want to start bsod.exe? (Y/N) -> ").title()
        
        if userChoice == "Y":
            print("Starting bsod.exe...")
            os.system("start bsod.exe")
            
        elif userChoice == "N":
            print("bsod.exe was not executed.")
            
        continue

    elif choice == "3":
        
        print("Downloading Shutdown.exe...")
        
        response = requests.get(link3)
        
        with open("shutdown.exe", "wb")as file:
            file.write(response.content)
            
        print("Success!")
        
        userChoice = input("Do you want to start shutdown.exe? (Y/N) -> ").title()
        
        if userChoice == "Y":
            print("Starting shutdown.exe...")
            os.system("start shutdown.exe")
            
        elif userChoice == "N":
            print("shutdown.exe was not executed.")
        
if __name__ == "__main__":
    installer()
