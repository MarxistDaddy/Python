#!/usr/bin/python3.10

#	exeception block
#	
#

import dis

def ex():

    print("hello worls its me mariooo!")

    try:
       x = 1 / 0
    except:
       print("loser try harder!")


ex()
dis.dis(ex)
