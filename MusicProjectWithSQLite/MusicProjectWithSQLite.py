# -*- coding: cp1254 -*-
import sqlite3
import time

class �ark�lar():
    def __init__(self,numara,isim,vokalist,s�zyazar�,m�zik,alb�m,s�re):
        self.isim=isim
        self.numara=numara
        self.s�zyazar�=s�zyazar�
        self.m�zik=m�zik
        self.alb�m=alb�m
        self.s�re=s�re
        self.vokalist=vokalist

    def __str__(self):
        return "\n{}-�ark� Ad�: {}\nVokalist: {}\nS�z Yazar�: {}\nM�zik: {}\nAlb�m: {}\n�ark� S�resi: {}\n".format(self.numara,self.isim,self.vokalist,self.s�zyazar�,self.m�zik,self.alb�m,self.s�re)

class �ark�c�():
    def __init__(self):
        self.Baglant�()
    
    def Baglant�(self):
        self.baglant�=sqlite3.connect("sark�lar.db")
        self.cursor=self.baglant�.cursor()
        sorgu="Create table If not exists sark�lar (Numara INT,Sark�_Ad� TEXT,Vokalist TEXT,S�z Yazar� TEXT,M�zik TEXT,Alb�m TEXT,Sark� S�resi INT)"
        self.cursor.execute(sorgu)
        self.baglant�.commit()

    def Baglant�Kes(self):
        self.baglant�.close()

    def Sark�lar�G�ster(self):
        sorgu="Select * From sark�lar"
        self.cursor.execute(sorgu)
        sark�lar=self.cursor.fetchall()
        if len(sark�lar)==0:
            print("Kay�tl� �ark� bulunamad�...")
        else:
            for i in sark�lar:
                sark�=�ark�lar(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
                print(sark�)

    def Sark�Sorgu(self,isim):
        sorgu="Select * From sark�lar Where Sark�_Ad�=?"
        self.cursor.execute(sorgu,(isim,))
        sark�lar=self.cursor.fetchall()
        if len(sark�lar)==0:
            print("Girilen �ark� par�as� bulunamad�...")
        else:
            sark�=�ark�lar(sark�lar[0][0],sark�lar[0][1],sark�lar[0][2],sark�lar[0][3],sark�lar[0][4],sark�lar[0][5],sark�lar[0][6])
            print(sark�)

    def �ark�Ekle(self,sark�):
        sorgu="Insert into sark�lar VALUES(?,?,?,?,?,?,?)"
        self.cursor.execute(sorgu,(sark�.numara,sark�.isim,sark�.vokalist,sark�.s�zyazar�,sark�.m�zik,sark�.alb�m,sark�.s�re))
        self.baglant�.commit()

    def �ark�Sil(self,isim):
        sorgu="Delete From sark�lar where Sark�_Ad�=?"
        self.cursor.execute(sorgu,(isim,))
        self.baglant�.commit()

    

            











