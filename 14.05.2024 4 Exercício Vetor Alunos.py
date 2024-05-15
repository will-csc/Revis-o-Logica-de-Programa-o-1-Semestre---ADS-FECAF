#---------- VETOR E ADIÇÃO ALUNOS ------------
def qnt_alunos():
    return int(input("Digite a quantidade de alunos: "))

qnt = qnt_alunos()
while qnt < 1:
    print("Digite uma quantidade maior que 0")
    qnt = qnt_alunos()

alunos = []
for i in range(qnt):
    aluno = str(input("Escreva o nome do aluno: \n"))
    alunos.append(aluno)

print("Os alunos são: ",alunos)
print("---------------------------")

#------------ EXCLUSÃO -------------
index = int(input("Digite a posição do aluno na lista \n"))
del(alunos[index-1])
print("Os alunos são: ",alunos)
print("---------------------------")