# -*- coding: utf-8 -*-
"""
AI.Lector.ru

Автор: Р.В. Шамин
"""

import random

class TQsa:
    def __init__(self):
        self.Qsa = {}
        self.S = list()
        random.seed()
       
        for i in range(1, 5):
            for j in range(1, 5):
                self.S.append([i, j])

        self.A = ("u", "d", "r", "l")

    def Can(self, s, a):
        ss, r = self.Move(s, a)

        return ss in self.S

    def Move(self, s, a):
        ss = [s[0], s[1]]
        r = -1

        if a == "u":
            ss[0] = ss[0] - 1

        if a == "d":
            ss[0] = ss[0] + 1

        if a == "r":
            ss[1] = ss[1] + 1

        if a == "l":
            ss[1] = ss[1] - 1

        if ss == [1, 2] or ss == [1, 3]:
            ss = [1, 1]
            r = -100

        return (ss, r)
        
    def R(self, s, a):
        ss, r = self.Move(s, a)
        
        return r

    def Max(self, s):
        m = -100
        
        for a in self.A:
            if self.Can(s, a):
                r = self.R(s, a)
                if r > m:
                    m = r
        return m
    
    def Q(self, s, a):
        if (s[0], s[1], a) in self.Qsa:
            return self.Qsa[(s[0], s[1], a)]
        else:
            return 0

    def setQ(self, s, a, value):
        self.Qsa[(s[0], s[1], a)] = value

    def getA(self, s, eps = 0.2):
        aa = list()
        for a in self.A:
            if self.Can(s, a):
                aa.append(a)
        
        if random.random() < eps:
            return random.choice(aa)
        else:
            m = -1000
            a_max = None
            for a in aa:
                Qsa = self.Q(s, a)
                if Qsa > m:
                    m = Qsa
                    a_max = a
            return a_max
                
            
        
            










        