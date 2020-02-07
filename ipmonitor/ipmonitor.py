import os

def getIp():
    return os.popen('curl https://ipinfo.io/ip')

print(getIp())
