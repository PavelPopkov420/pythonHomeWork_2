#Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#Найдите произведение элементов на позициях a и b.
#Значения N, a и b вводит пользователь с клавиатуры.

def get_numbers(n):
    arr = []
    count =0 
    for i in range(-n, n + 1):
        arr.append(i)
    return arr
            
num_ = get_numbers(int(input('Введите число: ')))
print(num_)

x = int(input('Введите номер 1 элемента: '))
y = int(input('Введите номер 2 элемента: '))

for i in range(len(num_)):
    mult = num_[x -1] * num_[y - 1]
print(f'Произведение элементов: {num_[x - 1]} * {num_[y - 1]} =', mult)