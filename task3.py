#Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
#округлённую до трёх знаков после точки.
#Пример:
#Для n = 6 -> 14.072

def sequence(n):
    lst = []
    for x in range (1, n + 1):
        lst.append(((1 + 1 / x)**x))    
    return lst
    

n = int(input('Введите значение n: '))  

print(round(sequence(n)))
print(round(sum(sequence(n))))
