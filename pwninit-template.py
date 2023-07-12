#!/usr/bin/env python3

from pwn import *

{bindings}
ADDR = ""
#PORT

context.binary = {bin_name}


def conn():
    if args.LOCAL:
        r = process({proc_args})
        if args.DBG:
            gdb.attach(r)
    else:
        r = remote(ADDR, PORT)

    return r


def main():
    p = conn()

    # good luck pwning :)

    p.interactive()


if __name__ == "__main__":
    main()