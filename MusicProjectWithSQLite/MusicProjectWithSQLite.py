# -*- coding: cp1254 -*-
import sqlite3
import time

class Şarkılar():
    def __init__(self,numara,isim,vokalist,sözyazarı,müzik,albüm,süre):
        self.isim=isim
        self.numara=numara
        self.sözyazarı=sözyazarı
        self.müzik=müzik
        self.albüm=albüm
        self.süre=süre
        self.vokalist=vokalist

    def __str__(self):
        return "\n{}-Şarkı Adı: {}\nVokalist: {}\nSöz Yazarı: {}\nMüzik: {}\nAlbüm: {}\nŞarkı Süresi: {}\n".format(self.numara,self.isim,self.vokalist,self.sözyazarı,self.müzik,self.albüm,self.süre)

class Şarkıcı():
    def __init__(self):
        self.Baglantı()
    
    def Baglantı(self):
        self.baglantı=sqlite3.connect("sarkılar.db")
        self.cursor=self.baglantı.cursor()
        sorgu="Create table If not exists sarkılar (Numara INT,Sarkı_Adı TEXT,Vokalist TEXT,Söz Yazarı TEXT,Müzik TEXT,Albüm TEXT,Sarkı Süresi INT)"
        self.cursor.execute(sorgu)
        self.baglantı.commit()

    def BaglantıKes(self):
        self.baglantı.close()

    def SarkılarıGöster(self):
        sorgu="Select * From sarkılar"
        self.cursor.execute(sorgu)
        sarkılar=self.cursor.fetchall()
        if len(sarkılar)==0:
            print("Kayıtlı şarkı bulunamadı...")
        else:
            for i in sarkılar:
                sarkı=Şarkılar(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
                print(sarkı)

    def SarkıSorgu(self,isim):
        sorgu="Select * From sarkılar Where Sarkı_Adı=?"
        self.cursor.execute(sorgu,(isim,))
        sarkılar=self.cursor.fetchall()
        if len(sarkılar)==0:
            print("Girilen şarkı parçası bulunamadı...")
        else:
            sarkı=Şarkılar(sarkılar[0][0],sarkılar[0][1],sarkılar[0][2],sarkılar[0][3],sarkılar[0][4],sarkılar[0][5],sarkılar[0][6])
            print(sarkı)

    def ŞarkıEkle(self,sarkı):
        sorgu="Insert into sarkılar VALUES(?,?,?,?,?,?,?)"
        self.cursor.execute(sorgu,(sarkı.numara,sarkı.isim,sarkı.vokalist,sarkı.sözyazarı,sarkı.müzik,sarkı.albüm,sarkı.süre))
        self.baglantı.commit()

    def ŞarkıSil(self,isim):
        sorgu="Delete From sarkılar where Sarkı_Adı=?"
        self.cursor.execute(sorgu,(isim,))
        self.baglantı.commit()

    

            











