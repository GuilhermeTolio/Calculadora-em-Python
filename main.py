#solicitar qual operacao deseja ser feita
operacao = input('''
Digite a operação matemática que deseja concluir:
+ para adição 
- para subtração 
* para multiplicação 
/ para divisão
''')


#solicitar o numero para o usuario
numero_1 = int(input('Coloque seu primeiro numero: '))
numero_2 = int(input('Coloque seu segundo numero: '))

#adicionando operadores
#adicao
if operacao == '+':
    print(numero_1 + numero_2)
elif operacao == '-':
    print(numero_1 - numero_2)
elif operacao == '*':
    print(numero_1 * numero_2)
elif operacao == '/':
    print(numero_1 / numero_2)

# operador nao valido
else:
    print('O operador escolhido nao eh valido, tente novamente')