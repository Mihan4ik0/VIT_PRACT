s = input('Введите число:')
try:
    float(s)
    s = int(s)
    x = s*2
    print(x)
except ValueError:
    s = 'Введенно не число'
    print(s)
