#!/usr/bin/python3.6
def fibonacci(quantidade):
    resultado = [0, 1]
    for count in range(1, (quantidade - 1)):
        resultado.append(sum(resultado[-2:]))
    return resultado


if __name__ == '__main__':
    for fib in fibonacci(20):
        print(fib, end=',')
    print(' ')
