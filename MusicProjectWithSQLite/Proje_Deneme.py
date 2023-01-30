# -*- coding: cp1254 -*-
from MusicProjectWithSQLite import *
import time
from pytube import YouTube

print("""
SQLite Veritaban� ile Temel �ark� K�t�phanesi Program�
��lem Numaralar�:
1-�ark�lar� G�sterme
2-�ark� Sorgulama
3-�ark� Ekleme
4-�ark� Sil
5-Sark� Dinleme
0-��k��
""")
sark�s�ras�=0
sark�c�=�ark�c�()
baglant�=sqlite3.connect("sark�lar.db")
cursor=baglant�.cursor()
sorgu="Select * From sark�lar"
cursor.execute(sorgu)
sark�lar=cursor.fetchall()
if len(sark�lar)==0:
    sark�sras�=0
else:
    sark�s�ras�=sark�lar[0][0]
    sark�s�ras�+=1
print(sark�s�ras�)
while True:
    try:
        secim=int(input("��lem numaras� giriniz: "))
    except ValueError:
        print("L�tfen say�sal de�erlerden birini giriniz...")

    if secim==1:
        sark�c�.Sark�lar�G�ster()
    elif secim==2:
        sark�ad�=input("Aramak istedi�iniz �ark�n�n ad�n� giriniz: ")
        sark�ad�=sark�ad�.upper()
        sark�c�.Sark�Sorgu(sark�ad�)
    elif secim==3:
        sark�s�ras�+=1
        sark�ad�=input("�ark�n�n Ad�: ")
        sark�ad�=sark�ad�.upper()
        vokalist=input("Vokalist: ")
        sark�yazar=input("S�z yazar�: ")
        m�zik=input("M�zik: ")
        alb�m=input("Alb�m: ")
        try:
            s�re=float(input("S�re(Araya nokta giriniz): "))
        except ValueError:
            print("S�re yanl�� formatta girildi...")
        try:
            yenim�zik=�ark�lar(sark�s�ras�,sark�ad�,vokalist,sark�yazar,m�zik,alb�m,s�re)
            print("�ark� listeye ekleniyor...")
            sark�c�.�ark�Ekle(yenim�zik)
            time.sleep(2)
            print("�ark� ba�ar�yla eklendi...")
        except:
            print("Bir hata meydana geldi...")
    elif secim==4:
        sark�ad�=input("Silmek istedi�iniz �ark�n�n ad�n� giriniz: ")
        sark�ad�=sark�ad�.upper()
        cevap=input("Silmek istedi�inizden emin misiniz?(E/H)")
        cevap = cevap.upper()
        if cevap=="E":
            print("�ark� siliniyor....")
            sark�c�.�ark�Sil(sark�ad�)
            time.sleep(2)
            print("�ark� ba�ar�yla silindi.")
        elif cevap=="H":
            print("�ark� silme i�lemi iptal edildi...")
        else:
            print("Ge�ersiz bir de�er girildi...")
    elif secim==5:
        sark�c�.Sark�lar�G�ster()
        try:
            sark�numara=int(input("Dinlemek istedi�iniz �ark� numaras�n� giriniz: "))
        except:
            print("L�tfen say�sal bir numara giriniz...")
        sark�c�.Sark�Acma(sark�numara)
    elif secim==0:
        print("Program sonland�r�l�yor....")
        time.sleep(2)
        print("Yine bekleriz...")
        break
    else:
        print("Ge�ersiz i�lem numaras� girildi")
