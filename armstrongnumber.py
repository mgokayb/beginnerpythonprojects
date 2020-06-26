def arms():
    arNum= int(input("Armstrong mu değil mi için sayınızı giriniz: "))
    cik = 1
    while cik == 1:  
        armsNumsList=[]
        armsTop=0
        for i in range(len(str(arNum))):
            armsNumsList.append(int(str(arNum)[i])**len(str(arNum)))
            armsTop+=int(str(arNum)[i])**len(str(arNum))
        if armsTop == arNum:
            print("girdiğiniz sayı: "+str(arNum)+" bir armstrong sayısıdır")
            cikis = input("Çıkmak için 'q' devam için herhangi bir tuşa basınız.")
        else:
            print("girdiğiniz sayı: "+str(arNum)+" bir armstrong sayısı değildir")
            cikis = input("Çıkmak için 'q' devam için herhangi bir tuşa basınız.")
        if cikis == "q":
            cik = 0
        else:
            arNum= int(input("Armstrong mu değil mi için sayınızı giriniz: "))

