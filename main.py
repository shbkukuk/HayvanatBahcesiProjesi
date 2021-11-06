import random as rd
import numpy as np
x_max = 500
y_max = 500
alan = (x_max,y_max)

class Avci():
    hareket = 1
    avlanma = 8
    konum = [rd.randrange(1,500,1),rd.randrange(1,500,1)]

class HayvanlarOzellıklerı():
    cıftlesme = 3
    def __init__(self, hareket, erkek, disi):
        self.hareket = hareket
        self.erkek = erkek
        self.disi = disi

class koyun (HayvanlarOzellıklerı):
    konumlar_erkek =[]
    konumlar_disi =[]
    def konumlandırma(self):
        for cinsiyet in "erkek", "disi":
            if cinsiyet == "erkek":
                for i in range(0, (self.erkek)):
                    self.konumlar_erkek.append([i, [rd.randrange(0, 500, 1), rd.randrange(0, 500, 1)]])
            elif cinsiyet == "disi":
                for i in range(0, (self.disi)):
                    self.konumlar_disi.append([i, [rd.randrange(0, 500, 1), rd.randrange(0, 500, 1)]])
class inek (HayvanlarOzellıklerı):
    konumlar_erkek =[]
    konumlar_disi =[]
    def konumlandırma(self):
        for cinsiyet in "erkek", "disi":
            if cinsiyet == "erkek":
                for i in range(0, (self.erkek)):
                    self.konumlar_erkek.append([i, [rd.randrange(0, 500, 1), rd.randrange(0, 500, 1)]])
            elif cinsiyet == "disi":
                for i in range(0, (self.disi)):
                    self.konumlar_disi.append([i, [rd.randrange(0, 500, 1), rd.randrange(0, 500, 1)]])
class aslan (HayvanlarOzellıklerı):
    konumlar_erkek =[]
    konumlar_disi =[]
    def konumlandırma(self):
        for cinsiyet in "erkek", "disi":
            if cinsiyet == "erkek":
                for i in range(0, (self.erkek)):
                    self.konumlar_erkek.append([i, [rd.randrange(0, 500, 1), rd.randrange(0, 500, 1)]])
            elif cinsiyet == "disi":
                for i in range(0, (self.disi)):
                    self.konumlar_disi.append([i, [rd.randrange(0, 500, 1), rd.randrange(0, 500, 1)]])
class kurt (HayvanlarOzellıklerı):
    konumlar_erkek =[]
    konumlar_disi =[]
    def konumlandırma(self):
        for cinsiyet in "erkek", "disi":
            if cinsiyet == "erkek":
                for i in range(0, (self.erkek)):
                    self.konumlar_erkek.append([i, [rd.randrange(0, 500, 1), rd.randrange(0, 500, 1)]])
            elif cinsiyet == "disi":
                for i in range(0, (self.disi)):
                    self.konumlar_disi.append([i, [rd.randrange(0, 500, 1), rd.randrange(0, 500, 1)]])
class tavuk_horoz (HayvanlarOzellıklerı):
    konumlar_erkek =[]
    konumlar_disi =[]
    def konumlandırma(self):
        for cinsiyet in "erkek", "disi":
            if cinsiyet == "erkek":
                for i in range(0, (self.erkek)):
                    self.konumlar_erkek.append([i, [rd.randrange(0, 500, 1), rd.randrange(0, 500, 1)]])
            elif cinsiyet == "disi":
                for i in range(0, (self.disi)):
                    self.konumlar_disi.append([i, [rd.randrange(0, 500, 1), rd.randrange(0, 500, 1)]])

koyun =koyun( hareket=2, disi=15, erkek=15)
inek = inek( hareket=2, disi=5, erkek=5)
kurt = kurt(hareket=3, disi=5, erkek=5)
aslan = aslan( hareket=4, disi=4, erkek=4)
tavuk_horoz = tavuk_horoz(hareket=1, disi=10, erkek=10)
# random belirtilen alanda konumlandırma
koyun.konumlandırma()
inek.konumlandırma()
tavuk_horoz.konumlandırma()
kurt.konumlandırma()
tavuk_horoz.konumlandırma()









