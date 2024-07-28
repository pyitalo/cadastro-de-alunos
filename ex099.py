from time import sleep


def valor(*num):
    print('analisando os valores informados...')
    sleep(0.5)
    for n in num:
        print(n, end=' ', flush=True)
        sleep(0.5) 
    if len(num) > 1:
        print(f'\no maior valor digitado foi {max(num)}.')
        print(f'foram digitados {len(num)} números ao total.')
    elif len(num) == 1:
        print(f'\no maior valor digitado foi {max(num)}.')
        print('apenas um número foi digitado.')
    else:
        print('nenhum valor foi digitado.')
    print('-=' * 20)

  
valor(2, 9, 4, 5, 7, 1)
valor(4, 7, 0)
valor(1, 2)
valor(6)
valor()