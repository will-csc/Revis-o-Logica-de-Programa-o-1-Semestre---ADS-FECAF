def num_usuario():
    print("Digite um número")
    return float(input())

num = num_usuario()

#--------- ESTRUTURA DE DECISÃO -------------
if num > 0:
    print("O numero ",num," é positivo \n")
elif num < 0:
    print("O numero ",num," é negativo \n")
else:
    print("O numero ",num," é zero \n")

#----------- LOOPING ATÉ SER <> DE 0 -----------
while num != 0:
    print("Digite um número igual a 0")
    num = num_usuario()