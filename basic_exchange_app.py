#
# input > satacağınız ve alacağınız döviz birimi ve miktarı.
# output > ne kadar alabileceğiniz.

import requests
import json

def doviz_exc():
    print("Döviz dönüştürme programına hoşgeldiniz.")

    base = input("Satmak istediğiniz para cinsini(USD, TRY, EUR) belirtiniz: ")
    base = base.upper()
    if base == "USD" or "TRY" or "EUR":
        result = requests.get(f"https://api.exchangeratesapi.io/latest?base={base}")
        result = result.text
        result = json.loads(result)
    else:
        print("Geçerli döviz türü girmediniz.")
        doviz_exc()
    
    buy = input("Hangi döviz türünden(USD, TRY, EUR) alım yapmak istiyorsunuz: ")
    buy = buy.upper()
    if base == buy:
        print("Hata: Almak ve satmak istediğiniz türler aynı.")
        doviz_exc()
    elif buy == "USD" or "TRY" or "EUR":
        oran = result["rates"]["{}".format(buy)]
        miktar = int(input("Kaç {} bozdurmak istiyorsunuz?: ".format(base)))
        if type(miktar) == int:
            print("{} {} {} {} ediyor.".format(miktar,base,oran*miktar,buy))
        else:
            print("Geçerli değer girilmedi. Sayısal değer girmelisiniz.")
            doviz_exc()
    else:
        print("Hata: Geçerli döviz türü girmediniz.")
        doviz_exc()

doviz_exc()
