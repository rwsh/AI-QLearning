# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 18:14:24 2017

@author: re
"""

import TQsa

class TMove:
    def __init__(self, Qsa, s):
        self.Qsa = Qsa
        self.s = s
        
    def Mov(self):
        a = self.Qsa.getA(self.s)
        s2, r = self.Qsa.Move(self.s, a)
        
        q = self.Qsa.Q(self.s, a) + 0.2 * (r + 0.9 * self.Qsa.Max(s2) - self.Qsa.Q(self.s, a))
        
        self.Qsa.setQ(self.s, a, q)
        self.s = s2
        
        if self.s == [1, 4]:
            return True
        else:
            return False
        
    def Type(self):
        print(self.s)
        
        