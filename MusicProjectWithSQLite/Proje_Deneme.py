# -*- coding: cp1254 -*-
from MusicProjectWithSQLite import *
import time
from pytube import YouTube

print("""
SQLite Veritabanı ile Temel Şarkı Kütüphanesi Programı
İşlem Numaraları:
1-Şarkıları Gösterme
2-Şarkı Sorgulama
3-Şarkı Ekleme
4-Şarkı Sil
5-Sarkı Dinleme
0-Çıkış
""")
sarkısırası=0
sarkıcı=Şarkıcı()
baglantı=sqlite3.connect("sarkılar.db")
cursor=baglantı.cursor()
sorgu="Select * From sarkılar"
cursor.execute(sorgu)
sarkılar=cursor.fetchall()
if len(sarkılar)==0:
    sarkısrası=0
else:
    sarkısırası=sarkılar[0][0]
    sarkısırası+=1
print(sarkısırası)
while True:
    try:
        secim=int(input("İşlem numarası giriniz: "))
    except ValueError:
        print("Lütfen sayısal değerlerden birini giriniz...")

    if secim==1:
        sarkıcı.SarkılarıGöster()
    elif secim==2:
        sarkıadı=input("Aramak istediğiniz şarkının adını giriniz: ")
        sarkıadı=sarkıadı.upper()
        sarkıcı.SarkıSorgu(sarkıadı)
    elif secim==3:
        sarkısırası+=1
        sarkıadı=input("Şarkının Adı: ")
        sarkıadı=sarkıadı.upper()
        vokalist=input("Vokalist: ")
        sarkıyazar=input("Söz yazarı: ")
        müzik=input("Müzik: ")
        albüm=input("Albüm: ")
        try:
            süre=float(input("Süre(Araya nokta giriniz): "))
        except ValueError:
            print("Süre yanlış formatta girildi...")
        try:
            yenimüzik=Şarkılar(sarkısırası,sarkıadı,vokalist,sarkıyazar,müzik,albüm,süre)
            print("Şarkı listeye ekleniyor...")
            sarkıcı.ŞarkıEkle(yenimüzik)
            time.sleep(2)
            print("Şarkı başarıyla eklendi...")
        except:
            print("Bir hata meydana geldi...")
    elif secim==4:
        sarkıadı=input("Silmek istediğiniz şarkının adını giriniz: ")
        sarkıadı=sarkıadı.upper()
        cevap=input("Silmek istediğinizden emin misiniz?(E/H)")
        cevap = cevap.upper()
        if cevap=="E":
            print("Şarkı siliniyor....")
            sarkıcı.ŞarkıSil(sarkıadı)
            time.sleep(2)
            print("Şarkı başarıyla silindi.")
        elif cevap=="H":
            print("Şarkı silme işlemi iptal edildi...")
        else:
            print("Geçersiz bir değer girildi...")
    elif secim==5:
        sarkıcı.SarkılarıGöster()
        try:
            sarkınumara=int(input("Dinlemek istediğiniz şarkı numarasını giriniz: "))
        except:
            print("Lütfen sayısal bir numara giriniz...")
        sarkıcı.SarkıAcma(sarkınumara)
    elif secim==0:
        print("Program sonlandırılıyor....")
        time.sleep(2)
        print("Yine bekleriz...")
        break
    else:
        print("Geçersiz işlem numarası girildi")
