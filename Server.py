#!/usr/bin/python3
 
# The FTPNetwork server as a whole. Proxy + FTPserver together.

import subprocess
import sys
import atexit
import os
import platform

def clean_exit():
    if FTPs.poll() == None:
        FTPs.terminate()
    if Proxy.poll() == None:
        Proxy.terminate()


if __name__ == '__main__':
    with open(os.devnull,"w") as FNULL:
        FTPs = subprocess.Popen(["./FTPserver.py"],stdout=FNULL,stderr=subprocess.STDOUT)
    Proxy = subprocess.Popen(["./Proxy.py"],stdout=sys.stdout)
    atexit.register(clean_exit)
    os.wait()
