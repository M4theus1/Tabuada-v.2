n = c = m =0
while True:
    n = int(input('Quer ver a tabuada de qual número? '))
    if n < 0:
        print('Programa da Tabuada encerrado. Volte sempre!')
        break
    for c in range (0, 11):
        m = n * c
        print(f'{n} x {c} = {m}')
        c += 1
