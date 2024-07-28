from random import randint
from time import sleep

numeros = list()


def sortear():
    for c in range(0, 5):
        numeros.append(randint(0, 10))
    print('SORTEANDO NÚMEROS...')
    print('=--' * 20)
    sleep(0.5)
    for n in numeros:
        print(n, end=' ', flush=True)
        sleep(0.4)
    print('números sorteados!')

def somapar():
    soma = 0
    par = list()
    for n in numeros:
        if n % 2 == 0:
            soma += n
            par.append(n)
    print()
    print('---' * 15)
    print(f'resultado de todos os números pares {par} temos: {soma}')


sortear()
somapar()