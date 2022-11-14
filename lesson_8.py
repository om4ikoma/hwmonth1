#open() работа с файлами (текстовыми)
import time
from random import  randint


attempts = int(input('Сколько попыток '))

right,failed = 0,0

while attempts != 0:
    first,second = randint(1, 9), randint(1, 9)
    result = first * second
    answer = int(input(f'{first} * {second} = ?'))
    if answer == result:
     print('верно!')
    right += 1
else:
    print('Неверно!')
    failed += 1
attempts -= 1


















# file = open('file.txt', 'w', encoding='UTF-8')
# file.write('кыргызстан бишкек')
# file.close()

# with open('file.txt', 'a') as file1:
#     file1.write('python geektech')

# with open('file.txt','r') as file:
#     print(file.readline())
#






