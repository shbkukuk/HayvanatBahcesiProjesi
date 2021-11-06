import random as rd

x_max = 500
y_max = 500
alan = (x_max,y_max)

class Avci():
    hareket = 1
    avlanma = 8
    konum = [[rd.randrange(1,500,1),rd.randrange(1,500,1)]]

class HayvanlarOzellıklerı():
    cıftlesme = 3
    def __init__(self, erkek, disi):
        self.erkek = erkek
        self.disi = disi
#hareketlerin fonsiyonlarının tanımlanması
def sagsol(konumlar ,hareket) :
    for index in range(konumlar.__len__()):
        if konumlar[index][0] <= alan[0]:
            konumlar[index][0] += hareket
        else :
            konumlar[index][0] -= hareket
    return  konumlar
def ileriasagi(konumlar ,hareket) :
    for index in range(konumlar.__len__()):
        if konumlar[index][1] <= alan[0]:
            konumlar[index][1] += hareket
        else :
            konumlar[index][1] -= hareket
    return  konumlar

class koyun (HayvanlarOzellıklerı):
    konumlar_erkek =[]
    konumlar_disi =[]
    def konumlandırma(self):
        for cinsiyet in "erkek", "disi":
            if cinsiyet == "erkek":
                for i in range(0, (self.erkek)):
                    self.konumlar_erkek.append( [rd.randrange(0, 500, 1), rd.randrange(0, 500, 1)])
            elif cinsiyet == "disi":
                for i in range(0, (self.disi)):
                    self.konumlar_disi.append( [rd.randrange(0, 500, 1), rd.randrange(0, 500, 1)])
class inek (HayvanlarOzellıklerı):
    konumlar_erkek =[]
    konumlar_disi =[]
    def konumlandırma(self):
        for cinsiyet in "erkek", "disi":
            if cinsiyet == "erkek":
                for i in range(0, (self.erkek)):
                    self.konumlar_erkek.append( [rd.randrange(0, 500, 1), rd.randrange(0, 500, 1)])
            elif cinsiyet == "disi":
                for i in range(0, (self.disi)):
                    self.konumlar_disi.append( [rd.randrange(0, 500, 1), rd.randrange(0, 500, 1)])
class aslan (HayvanlarOzellıklerı):
    konumlar_erkek =[]
    konumlar_disi =[]
    def konumlandırma(self):
        for cinsiyet in "erkek", "disi":
            if cinsiyet == "erkek":
                for i in range(0, (self.erkek)):
                    self.konumlar_erkek.append( [rd.randrange(0, 500, 1), rd.randrange(0, 500, 1)])
            elif cinsiyet == "disi":
                for i in range(0, (self.disi)):
                    self.konumlar_disi.append( [rd.randrange(0, 500, 1), rd.randrange(0, 500, 1)])
class kurt (HayvanlarOzellıklerı):
    konumlar_erkek =[]
    konumlar_disi =[]
    def konumlandırma(self):
        for cinsiyet in "erkek", "disi":
            if cinsiyet == "erkek":
                for i in range(0, (self.erkek)):
                    self.konumlar_erkek.append( [rd.randrange(0, 500, 1), rd.randrange(0, 500, 1)])
            elif cinsiyet == "disi":
                for i in range(0, (self.disi)):
                    self.konumlar_disi.append( [rd.randrange(0, 500, 1), rd.randrange(0, 500, 1)])
class tavuk_horoz (HayvanlarOzellıklerı):
    konumlar_erkek =[]
    konumlar_disi =[]
    def konumlandırma(self):
        for cinsiyet in "erkek", "disi":
            if cinsiyet == "erkek":
                for i in range(0, (self.erkek)):
                    self.konumlar_erkek.append( [rd.randrange(0, 500, 1), rd.randrange(0, 500, 1)])
            elif cinsiyet == "disi":
                for i in range(0, (self.disi)):
                    self.konumlar_disi.append( [rd.randrange(0, 500, 1), rd.randrange(0, 500, 1)])
avci = Avci()
koyun =koyun( disi=15, erkek=15)
inek = inek(  disi=5, erkek=5)
kurt = kurt( disi=5, erkek=5)
aslan = aslan(  disi=4, erkek=4)
tavuk_horoz = tavuk_horoz( disi=10, erkek=10)
# random belirtilen alanda konumlandırma
koyun.konumlandırma()
inek.konumlandırma()
tavuk_horoz.konumlandırma()
kurt.konumlandırma()
tavuk_horoz.konumlandırma()
#hareketler
sagsol(konumlar=avci.konum,hareket=avci.hareket)
sagsol(konumlar=koyun.konumlar_erkek,hareket=2)
sagsol(konumlar=koyun.konumlar_disi,hareket=2)
sagsol(konumlar=inek.konumlar_erkek,hareket=2)
sagsol(konumlar=inek.konumlar_disi,hareket=2)
sagsol(konumlar=kurt.konumlar_erkek,hareket=3)
sagsol(konumlar=kurt.konumlar_disi,hareket=3)
sagsol(konumlar=aslan.konumlar_erkek,hareket=4)
sagsol(konumlar=aslan.konumlar_disi,hareket=4)
sagsol(konumlar=tavuk_horoz.konumlar_erkek,hareket=1)
sagsol(konumlar=tavuk_horoz.konumlar_disi,hareket=1)

ileriasagi(konumlar=avci.konum,hareket=avci.hareket)
ileriasagi(konumlar=koyun.konumlar_erkek,hareket=2)
ileriasagi(konumlar=koyun.konumlar_disi,hareket=2)
ileriasagi(konumlar=inek.konumlar_erkek,hareket=2)
ileriasagi(konumlar=inek.konumlar_disi,hareket=2)
ileriasagi(konumlar=kurt.konumlar_erkek,hareket=3)
ileriasagi(konumlar=kurt.konumlar_disi,hareket=3)
ileriasagi(konumlar=aslan.konumlar_erkek,hareket=4)
ileriasagi(konumlar=aslan.konumlar_disi,hareket=4)
ileriasagi(konumlar=tavuk_horoz.konumlar_erkek,hareket=1)
ileriasagi(konumlar=tavuk_horoz.konumlar_disi,hareket=1)


