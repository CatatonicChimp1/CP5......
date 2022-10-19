def two(n):
    a = ''
    while n > 0:
        os = n % 2
        a = a + str(os)
        n = n // 2
    a = a[::-1]
    return a

def eight(n):
    a = ''
    while n > 0:
        os = n % 8
        a = a + str(os)
        n = n // 8
    a = a[::-1]
    return a
n = int(input("Введите десятичное число:"))
s = int(input("Введите целевую систему счисления:"))
if s == 2:
    print(two(n))
if s == 8:
    print(eight(n))