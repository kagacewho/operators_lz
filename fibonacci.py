print('Введите число:')
n = (int(input()))
fib = ['0']
per1 = 0
per2 = 1 
for i in range (2, n + 2):
    if i % 2 == 1: 
        per1 = per1 + per2
        fib.append(str(per1))
    else: 
        per2 = per1 + per2
        fib.append(str(per2))
ans = '' 
for i in range(len(fib)):
    ans += fib[i] + ", " 
ans = ans[:-2] 
print('Вот ряд Фибоначи из', n, 'не равных нулю чисел:')
print(ans)