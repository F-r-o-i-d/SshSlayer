import random
import socket
import struct
import sys
import colorama
import threading

from core import engine
from core import BruteForce
from core import Style
import itertools
import time

instancesList = list()

colorama.init()

done = False

def animate():

    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')

def main():
    """animation = "▁▂▃▄▅▆▇█▇▆▅▄▃▁"

    for i in range(14):
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
        time.sleep(0.05)
"""


    print("Launch multiple instance")
    for x in range(21):
        instancesList.append(engine.Engine(True))
    time.sleep(1)
    print("Start all instance")
    for e in instancesList:
        threading.Thread(target=e.Run).start()

def Brute():
    sshFile = open("sshList", "r")
    sshFileLine = sshFile.read().split("\n")
    parts = []
    delimiters = len(sshFileLine)/6
    buf = []
    counter = 0
    print("Chunking ssh list")
    for x in range(len(sshFileLine)):
        counter += 1
        buf.append(sshFileLine[x])
        if counter > delimiters:
            counter = 0
            parts.append(buf)
            buf = []
    print(f"{len(parts) }chunks")
    print("Initalise Instances")
    for x in range(5):
        instancesList.append(BruteForce.Instances(parts[x]))
    time.sleep(1)
    for i in instancesList:
        threading.Thread(target=i.Run).start()
 

if __name__ == "__main__":
    Style.ShowBanner()
    if len(sys.argv) ==1:
        print("args :")
        print("\t--findIP start finding ip with port 22 open")
        print("\t--BruteForce try to bruteforce found ip")
        if Style.ShowMenu(["Search IP","Bruteforce IP"]) == 1:
            main()
        else:
            Brute()
    if sys.argv[1] == "--findIP":
        main()
    elif sys.argv[1]  == "--BruteForce":
        Brute()
    else:
        Style.ShowBanner()
        print("args :")
        print("\t--findIP start finding ip with port 22 open")
        print("\t--BruteForce try to bruteforce found ip")
