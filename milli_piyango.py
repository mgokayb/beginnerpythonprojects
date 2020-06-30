#
# Bu uygulamada seçeceğiniz şans oyunlarını istediğiniz sayıda random oluşturan 
# ve bunların tutarını hesap edip ister txt dosyası olarak alabileceğiniz bir
# dosya oluşturur istersenizde direk terminale bu random kolonları sunar.
# input > oyunun kodu ve adet sayısı
# output > oyun_listesi.txt de kolonların listesi ve terminale yazdırılmış hali. Ve son olarakta toplam tutarı.
#


import random
with open("oyun_listesi.txt","w",encoding="utf-8") as file:
    pass

def sayisal_loto():
    all_nums = list(range(1,49))
    lucky_nums = random.sample(all_nums,6)
    lucky_nums.sort()
    with open("oyun_listesi.txt","a",encoding="utf-8") as file:
        file.write(f" sayısal loto için: {lucky_nums}\n")
    

def sans_topu():
    first_nums = list(range(1,34))
    second_nums = list(range(1,14))
    f_lucky_nums = random.sample(first_nums,5)
    s_lucky_nums = random.sample(second_nums,1)
    f_lucky_nums.sort()
    s_lucky_nums.sort()
    with open("oyun_listesi.txt","a",encoding="utf-8") as file:
        file.write(f" şans topu için: {f_lucky_nums} + {s_lucky_nums}\n")


def on_numara():
    all_nums = list(range(1,80))
    lucky_nums = random.sample(all_nums,10)
    lucky_nums.sort()
    with open("oyun_listesi.txt","a",encoding="utf-8") as file:
        file.write(f" on numara için: {lucky_nums}\n")

def super_loto():
    all_nums = list(range(1,54))
    lucky_nums = random.sample(all_nums,6)
    lucky_nums.sort()
    with open("oyun_listesi.txt","a",encoding="utf-8") as file:
        file.write(f" süper loto için: {lucky_nums}\n")
   

def luck_games():
    print("""
        ***************************************************************
        Merhabalar Şans Oyunları için numara üreticisine HOŞGELDİNİZ!!
        Seçeceğiniz şans oyunları için seçeceniz miktarda numara üretip
        Tutar hesaplamasını yapıp terminale yazdıracağım...
        ***************************************************************
    """)
    print("""
        ***************************************************************
        Oynamak istediğiniz oyun/oyunları seçip ardından kaç tane 
        oynamak istediğinizi giriniz. Yapacağınız işlemler bittiğinde
        ekrana istediğiniz kuponlar ve toplam tutar yazdıralacaktır. 
        ***************************************************************
    """)
    
    toplam_tutar=0
    while True:
        print("""
        1 - On Numara 
        2 - Şans Topu
        3 - Sayısal Loto
        4 - Süper Loto
        5 - Bitir
    """)
        oyun = input("Oynamak istediğiniz oyunun başındaki sayıyı yazınız: ")
        if oyun == "5":
            print("Oynadığınız oyunların numaralarını oyun_listesi.txt dosyasında bulabilirsiniz.")
            with open("oyun_listesi.txt","r",encoding="utf-8") as file:
                lines = file.readlines()
                for line in lines:
                    print(line)
                print("Bütün kolonları oynamanız için gereken tutar: ",toplam_tutar," TL")
            break
        adet = int(input("Kaç kolon oynamak istiyorsunuz: "))
        if oyun == "1":
            for _ in range(adet):
                on_numara()
            tutar = adet*1
            toplam_tutar+=tutar
        elif oyun == "2":
            for _ in range(adet):
                sans_topu()
            tutar = adet*1
            toplam_tutar+=tutar
        elif oyun == "3":
            for _ in range(adet):
                sayisal_loto()
            tutar = adet*1.5
            toplam_tutar+=tutar
        elif oyun == "4":
            for _ in range(adet):
                super_loto()
            tutar = adet*2
            toplam_tutar+=tutar
        else:
            print("Hatalı giriş yaptınız!")
            

luck_games()
