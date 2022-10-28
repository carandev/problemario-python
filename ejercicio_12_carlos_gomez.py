def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return (fib(num - 2) + fib(num - 1))


for i in range(1,1000):
    print(f'Fibonacci de {i} es: {fib(i)}')
