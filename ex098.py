jogador = dict()
jogadores = list()
cont = 0
while True:
    jogador['nome'] = str(input('digite o nome do jogador: '))
    jogador['partidas'] = int(input(f'quantas partidas o {jogador["nome"]} jogou? '))
    gols = list()
    tot = 0
    for c in range(jogador['partidas']):
        gol = int(input(f'quantos gols fez na partida {c + 1}? '))
        gols.append(gol)
        tot += gol
    jogador['gols'] = gols[:]
    jogador['total'] = tot
    tot = 0
    jogadores.append(jogador.copy())
    gols.clear()
    jogador.clear()
    while True:
        res = str(input('quer continuar?[S/N] ')).upper().strip()[0]
        if res in 'SN':
            break
        print('tente de novo! reposta inválida.')
    if res in 'N':
        break
print('=-=' * 15)
print(f'{"cod":<7}', end='   ')
print(f'{"nome":<5}', end='   ')
print(f'{"gols":^10}', end='   ')
print(f'{"total":>7}')
print('---' * 15)
for j in jogadores:
    print(f'{cont:<7}', end='   ')
    print(f'{j["nome"]:<5}', end='     ')
    print(f'{j["gols"]}', end='      ')
    print(f'{j["total"]:>7}', end='')
    cont += 1
    print()
print('---' * 15)
while True:
    while True:
        esc = int(input('mostrar os dados de qual jogador?(digite "999" para parar.)  '))
        if -1 < esc <= len(jogadores) or esc == 999:
            break
        print(f'Jogador inválido! não existe jogador com o código {esc}')
    if esc != 999:
        print(f'=> Levantamento do jogador {jogadores[esc]["nome"]}:')
        cont = 0
        for j in range(jogadores[esc]['partidas']):
            print(f'no jogo {cont + 1}, ele fez {jogadores[esc]["gols"][cont]}')
            cont += 1
    print('---' * 15)
    if esc == 999:
        break
print('FIM DO PROGRAMA')