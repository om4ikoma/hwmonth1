low = 0
mid = 50
high = 100
tries = 0
with open('results.txt', 'w', encoding='UTF-8') as file:
    file.write(f"Попытки: ")
    while True:
        file.write(f"{mid} ")
        otvet = input(f"Загаданное вами число: {mid}?\n> или < или да:  ")
        tries += 1
        if otvet == '>':
            low = mid
            mid = (low + high) // 2
        elif otvet == '<':
            high = mid
            mid = (low + high) // 2
        elif otvet == 'да':
            file.write(f"\nКоличество попыток: {tries}")
            break
        else:
            print(f"Введите строго по инструкции:\nЕсли:\n\tЗагаданное число меньше {mid}, введите '<'"
                  f"\n\tЗагаданное число больше {mid}, введите '>'"
                  f"\n\tЗагаданное число равно {mid}, введите 'да'")

        file.write(f"\nЗагаданное число: {mid}")


