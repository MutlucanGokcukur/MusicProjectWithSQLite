# -*- coding: cp1254 -*-
from MusicProjectWithSQLite import *
import time

print("""
SQLite Veritaban� ile Temel �ark� K�t�phanesi Program�
��lem Numaralar�:
1-�ark�lar� G�sterme
2-�ark� Sorgulama
3-�ark� Ekleme
4-�ark� Sil
0-��k��
""")
sark�c�=�ark�c�()
sark�s�ras�=0
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
    elif secim==0:
        print("Program sonland�r�l�yor....")
        time.sleep(2)
        print("Yine bekleriz...")
        break
    else:
        print("Ge�ersiz i�lem numaras� girildi")
