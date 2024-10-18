lista = []
a = 0
b = 1
lista.append(a)
lista.append(b)

while True:
    soma = a + b
    lista.append(soma)
    a = b
    b = soma
    if len(lista) >= 30:
        break
print(lista)

while True:
    print('*'*10, 'SEQUENCIA DE FIBONACCI', '*'*10)
    number = int(input('Digite um número entre 0 e meio milhão '))
    
    print('=-=' * 20)
    if number in lista:
        print(f'O número {number} faz parte da sequência de Fibonacci.')
    else:
        print(f'Lamento, mas este número {number} não compõe a sequência de Fibonacci.')
    print('=-=' * 20)
    answer = input('Deseja continuar [S/N]: ').strip().upper()
    if answer == 'N':
        break
print('Fim do programa.')
