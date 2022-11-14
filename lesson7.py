 # lambda , try-except
 # lambda , arguments:expression









# try:
#    number = int(2.7)
#    print(number)
# except:
#     print('no')
#
# # try:
# #     print(10/0)
# # except:
# #     print('не делим на нолль')
# #
# #
# # try:
# #     print(name)
# # except:
# #     print('нет такой переменной')
# # finally:
# #     print('проверка завершенна')
# #
# # print([1,3,2[3]])


# #
# #
# #
# #
# #
# #
# #
# # # # def first_word(sentence='Helo world'):
# # # a = {
# # #     'two':2,
# # #     'one':1,
# # #     'three':3,
# # #
# # # }
# # #
# # # print(sorted(a.items(),key=lambda x: x[1]))
# # #
# # #
# # # names = ['samuel','azat','linda']
# # #
# # # names = (sorted(a,key=str.lower))
# # #
# # # print(names)
# # #
# # # #     if type(sentence) != str:
# # # #         return False
# # # #     return False sentence.split()[0]
# # #
# # #
# # # #     # return False if type(sentence) != str else sentence.split()[0]
# # #
# # # # print(first_word(123))
# # #
# # #
# # # # # print(5 for 10>3 else 7)
# # #
# # #
numbers =list(range(1,6))
numbers = list(filter(lambda  x: x > 3,numbers))
numbers = list(map(lambda x: x**3,numbers))
# # # # #
# # # # # print([i ** 3  for i in [1,2,3,4,5]])
# # # # #
# # # # #
print(numbers)