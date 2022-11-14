def Hello_world(str):
    str = 'Hello world'
    string = input()
    if type(string) == str:
        return string.split()[0]
    elif type(string) != str:
        return False


print(Hello_world(str))



def root(*args):
    return sum(args)/len(args)
print(root())



ask = input('Введите пароль - ')
def password(ask):
    if len(ask) >= 6:
        print('Пароль подходит')
        return True
    else:
        print('Ненадежный пароль')
        return False


    print(password(ask))



