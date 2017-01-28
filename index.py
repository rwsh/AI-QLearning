
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 20:28:45 2017

@author: re
"""

import TQsa

import TMove

Q = TQsa.TQsa()

S = 0

N = 100

for i in range(N):
    Move = TMove.TMove(Q, [1, 1])
    Move.Type()

    for n in range(20000):
        t = Move.Mov()
        Move.Type()
        if t:
            print("Goal! ", n)
            S = S + n
            #input("> ")
            break

print(S / N)


