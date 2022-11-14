#словари, сеты
#[key : value]
#numbers = [1, 2, 3, 4, 5]

menu = {
    "plov": ['meat', 'rice', 'carrot', 180],
    'beshbarmak': ['meat', ['noodles','onion', 200]],
    'fresh salat':['onion', 'tomato', 'cucumber', 100]
}

while True:
    data = []
    chosen_by_client = []
    ingridient = input('введите инридиент')
    for i, k  in menu.items():
        if ingridient in k:
            print(f'{i} - {menu[i][-1]}')
            data.append(f'{i} - {menu[i][-1]}')
    choise = input(f'выберите: {list(enumerate(data))}')
    for i in data:
    chosen_by_client.append(data[])






#beshbarmak = {'мясо', "лапша","лук"}
#plov = {'мясо', "морковь", "рис"}
#print(beshbarmak.difference((plov)))
#print(beshbarmak - plov)

#print(beshbarmak.union(plov))
#print(beshbarmak | plov)

#print(beshbarmak.intersection(plov))
#print(beshbarmak & plov)

#print(beshbarmak.symmetric_difference(plov))
#print(beshbarmak ^ plov)





#new_set = {1, 2, 3, 1, 3, 4}
#print(new_set)







 #example = {

#    'abc':True,
#     2.5: True,
#    (1 , 2 ,3 ):True,
# }

#lst = [[2,'2'],[3,'3/'],[4,'4']]
#new1 = dict(lst)
#print(new1)

#new = dict(one=1, two=2, three=3)

#print(new)

#student = {
   # 'name': 'Danil',
    #'age': 22,
    #'height': 1.78,
    #'hobby': ['chess' , 'english' , 'boxing'],
    #'education':{'AUCA':2019 , 'Geektech':2020}
#}
#print(student)

#for  ai, kol in student.items():
#    print(f'{ai}: {kol}')


#print(student.keys())
#print(student.values())
#print(student.items())



#student['education']['ezone'] = 2021
#student['hobby'].append('python')



# print(student.['name'])
# print(student.get('name , 'хотели получить имя , но его нет!'))




