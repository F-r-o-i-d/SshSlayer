import random
import socket
import struct
import paramiko
import threading

class Engine(object):

    def __init__(self, verbose=False):
        self.verbose = verbose
        self.client = paramiko.client.SSHClient()
        self.primarySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.primarySocket.settimeout(1)
        self.socketPool = []
        self.statue = "idle"
        self.running = True
        self.ipPool = []
        self.sshIp = []

    def __GenerateIp(self):
        #return "46.105.237.29"
        ip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))

        return ip

    def __CheckSSH(self, ip):
        sock = socket.socket()
        sock.settimeout(1) # 1000ms max before timeout
        return sock.connect_ex((ip, 22)) == 0

    
    def sshCheckRuntime(self):
        coef = self.sshCheckRuntime / 4
        for x in range(coef):
            buf = []
            self.ipPool.remove()

    def SaveSSH(self):
        with open("sshList", "a+") as f:
            for ip in self.sshIp:
                f.writelines(ip)
            f.close()

        pass
    def Run(self):
        print("new instance running")
        while(self.running):
            self.sshIp = []
            self.ipPool = []
            self.statue = "generate-ipPool"
            for x in range(10):
                ip= self.__GenerateIp()
                if ip in self.ipPool:
                    pass
                else:
                    self.ipPool.append(ip)
            for ip in self.ipPool:
                if self.__CheckSSH(ip):
                    open("sshList", "a").write(ip+"\n")
                    self.sshIp.append(ip)
                    if self.verbose:
                        print(f"{ip}:22 y")
                else:
                    pass
            if( len(self.sshIp) - len(self.ipPool)):
                pass #print("No ip with ssh found, rescanning don't worry senpai were are going to found them ")
            else:
                self.SaveSSH()
def run():
    engine = Engine(verbose = True)
    threading.Thread(target=engine.Run).start()

def GetStats():
    return "none"


