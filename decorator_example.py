#
#this codes prints multiplication table
#
def deco(func):
    def wrapper(num):
        if num == 1:
            print("#####################")
        func(num)
        
        print("#####################")

    return wrapper

@deco
def multi(num):
    for i in range(1,10):
        print(num," * ",i," = ",num*i)

for i in range(1,10):
    multi(i)
