s = input('Введите ваш возраст:')
try:
    float(s)
    s = int(s)
    if s == 1 or s == 21 or s == 31 or s == 41 or s == 51 or s == 61 or s == 71 or s == 81 or s == 91 or s == 101:
        print('Вам ', s, ' год')
    elif 1 < s < 5 or 21 < s < 25 or 31 < s < 35 or 41 < s < 45 or 51 < s < 55 or 61 < s < 65 or 71 < s < 75 or 81 < s < 85 or 91 < s < 95 or 101 < s < 105:
        print('Вам ', s, ' года')
    elif 4 < s < 21 or 24 < s < 31 or 34 < s < 41 or 44 < s < 51 or 54 < s < 61 or 64 < s < 71 or 74 < s < 81 or 84 < s < 91 or 94 < s < 101:
        print('Вам ', s, ' лет')
    else:
        print('Введён неверный возраст')
except ValueError:
    s = 'Введенно не число'
    print(s)
