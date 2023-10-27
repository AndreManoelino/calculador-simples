#Função soma
def somar(x, y):
    return x + y

#Função subtração
def subtrair(x, y):
    return x - y

#função multiplicação
def multiplicar(x, y):
    return x * y

#Função divisão
def dividir(x, y):
    if y == 0:
        return 'Não e possível dividir por zero'
    return x / y

#Apresentação do menu
print('Selecionar a operação')
print('1_ soma')
print('2_ subtração')
print('3_ multiplicação')
print('4_ Divisão')

#Obtendo a escolha do usuário
escolha = input('Digite o número da operação desejada.')

#Usando método float para obter um número flutuante
num1 = float(input('Digite o primeiro número'))
num2 = float(input('Digite o segundo número .'))

#Realizando a operação escolhida
if escolha == '1':
    print('Resultado:', somar(num1, num2))
elif escolha == '2':
    print('Resultado:', subtrair(num1, num2))
elif escolha == '3':
    print('Resultado:', multiplicar(num1, num2))
elif escolha == '4':
    print('Resultado:', dividir(num1, num2))

else:
    print('Opção inválida') 

        