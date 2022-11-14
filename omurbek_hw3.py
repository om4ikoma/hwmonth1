glas = "ауоыиэяюёеaeiouy"
while True:
    word = input("Введите слово: ")
    word = word.lower()
    if word == 'exit':
        print("Программа остановлена!!!")
        break
    bukvy, gl, sogl = 0, 0, 0
    gl = 0
    sogl = 0
    for i in word:
        if i.isalpha():
            bukvy += 1
            if i in glas:
                gl += 1
            else:
                sogl += 1

    print(f"Слово: {word}")
    print(f"Количество букв: {bukvy}")
    print(f"Согласных букв: {sogl}")
    print(f"Гласных букв: {gl}")
    print(f"Гласные/Согласные: {round(gl/bukvy * 100, 2)}%/{round(sogl/bukvy * 100, 2)}%")


