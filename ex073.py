lista = list()
alunos = list()
cont = 0
while True:
    lista.append(str(input('digite o nome do aluno: ')))
    lista.append(float(input('digite a nota 1: ')))
    lista.append(float(input('digite a nota 2: ')))
    alunos.append(lista[:])
    lista.clear()
    while True:
        res = str(input('quer continuar?[S/N] ')).upper().strip()[0]
        if res in 'SN':
            break
        print('reposta inválida')
    if res in 'N':
        break
print('=-=' * 8)
print('No. ', ' NOME ', ' Média ')
print('-' * 25)
for al in alunos:
    print(f'{cont}   ', end='')
    print(f'  {al[0]}   ', end='')
    print(f'  {(al[1] + al[2]) / 2:.1f}')
    cont += 1
print('-' * 25)
while True:
    esc = int(input('mostrar as informações de qual aluno?, digite o No. (Digite "999" para parar) '))
    if '999' in str(esc):
        break
    print('---' * 10)
    print(f'nome:  {alunos[esc][0]}')
    print(f'nota1: {alunos[esc][1]}')
    print(f'nota2: {alunos[esc][2]}')
    print('---' * 10)
