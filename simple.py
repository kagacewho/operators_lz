input_data = open('input.txt', 'r') # Открыть файлы
data = input_data.read()
output = open('output.txt', 'w')  
data = data.split() # Разбиваем строку на список
n = int(data[0]) 
if n == 1: # Проверка на ввод единицы
    output.write(str('1 ne prostoe i ne sostavnoe')) # Единица не является ни простым, ни составным
for i in range(2,25001): # Задаем i из списка, числа от 2 до 25001 (не включая 25001)
    if n%i == 0 and i !=n: # Задаем условие для определения вида числа
        output.write(str('N')) # Выводим N, если число составное
        break # Завершить цикл, если условие получено
    elif i == n: # При невыполнении прошлого условия задаем условие, при котором i равно заданному числу
        output.write(str('Y')) # Выводим Y, если число простое  
input_data.close() # Закрываем файлы
output.close()
