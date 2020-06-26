sayi1 = 1
sayi2 = 1
i=1
numbers = [sayi1,sayi2]
adet = 10
for i in range(adet-2): 
    sayi1,sayi2 = sayi2,sayi1+sayi2
    numbers.append(sayi2) 
print(numbers)
