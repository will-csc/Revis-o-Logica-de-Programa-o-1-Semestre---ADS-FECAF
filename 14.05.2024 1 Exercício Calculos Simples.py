def opcao_calculo():
    print("Selecione a opção desejada abaixo \n"
          "Digite 1 --> Soma \n"
          "Digite 2 --> Subtração \n"
          "Digite 3 --> Multiplicação \n"
          "Digite 4 --> Divisão \n")
    return int(input())
def quantidade_operações():
    print("Digite a quantidade de números nas operações: ")
    return int(input())

def calculo(opção,qnt):
    lista = {"1:+","2:-","3:*","4:/"}
    lista_str = {1:"soma", 2:"subtração", 3:"multiplicação", 4:"divisão"}

    for i in range(qnt):
        print(f"Digite um número para {lista_str[opcao]}: ")
        num = float(input())
        if i == 0:
            result = num
        else:
            if opcao == 1:
                result += num
            elif opcao == 2:
                result -= num
            elif opcao == 3:
                result *= num
            elif opcao == 4:
                if num != 0:
                    result /= num
                else:
                    print("Erro: Divisão por zero!")
                    return

    print(f"O resultado da {lista_str[opcao]} é: {result}")

#---------- OPÇÃO DE CALCULO ---------
opcao = opcao_calculo()
while opcao not in range(1,5):
    print("Digite um numero entre 1 e 4 nas opções abaixo")
    opcao = opcao_calculo()

#----------- QNT DE OPERAÇÕES -----------
qnt = quantidade_operações()
while qnt < 2:
    print("Digite a quantidade acima de 1")
    qnt = quantidade_operações()

#-------- ESTRUTURA DE DECISÃO ----------
if opcao == 1: #Soma
    calculo(opcao,qnt)
elif opcao == 2: #Subtração
    calculo(opcao,qnt)
elif opcao == 3: #Multiplicação
    calculo(opcao,qnt)
else:
    calculo(opcao,qnt)



