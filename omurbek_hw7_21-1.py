ten = list(range(1,11))
evens = list(filter(lambda x: x % 2 == 0, ten))
evens =list(map(lambda x: x * x , evens))
print(evens)
print(ten)


while True:
    index = input('Введите индекс')
    if index.lower() == 'exit':
        break
    try:
       print(ten[int(index)])
    except:
        print('неверный индекс или данного индекса не сущетсвует')