egg-hunt shellcode
egg-hunt shellcode原文：http://www.hick.org/code/skape/papers/egghunt-shellcode.pdf
根据原文的描述，有三种egg-hunt shellcode，分别用access和sigaction两个系统调用来实现
我试了试，通过access系统调用实现的shellcode是可以的，sigaction貌似不行(不排除我写错了)
