GeekTech = {
    'addres':'Toktogula 175',
    'courses':['Android','Backend','Fronted'],
    'bag':{'fails','errors','stack'},
}
numbers = {
    'phone':'+996 507 052 018'
}
instagram = {
    'instagram':'geektech__kg'
}
del GeekTech['bag']

GeekTech.update(numbers)
GeekTech.update(instagram)

GeekTech ['addres'] = 'Imbraimova 103'
GeekTech ['courses'] = {'Android','Backend','Frontend','IOS','Mobile','UX/UI'}
GeekTech_set = ['Android','Backend','Frontend','IOS','Mobile','UX/UI']
print(GeekTech.keys())
print(GeekTech.values())

for key , values in GeekTech.items():
    print(f'{key}: {values}')

print(GeekTech)

