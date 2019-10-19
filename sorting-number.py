list_of_some_numbers = []
number = ""
while True:
    number = input("give me some number and i sorted for u. for ending give number type 'end' >>>  ")
    if number == "end":
        break
    else:
        list_of_some_numbers += number

i = len(list_of_some_numbers)
a = 0
while a < i:
    max = list_of_some_numbers[0]
    for number in list_of_some_numbers:
        if number > max:
           max = number
    print(max)
    list_of_some_numbers.remove(max)
    a += 1
