'''
Para melhor compreensão sobre funções na linguagem Python, vamos criar um programa para cálculo de média de notas.
No programa, o usuário deverá digitar duas notas para o aluno. Na sequência, o programa irá calcular e exibir a média,
informando se o aluno está aprovado (média maior ou igual a 7.0) ou reprovado.
O programa deverá ter uma função para leitura das notas e outra, para cálculo da média.
Para iniciar a programação, crie a nova classe no projeto já criado anteriormente no PyCharm.
Clique com o botão direito sobre a pasta correspondente ao projeto e selecione a opção New - Python File.
Na janela New - Python File adicione o nome Media e pressione a tecla Enter, para finalizar.
Agora, vamos analisar como fica o código do programa proposto:
'''

def lernotas():
    n=float(input("Digite uma nota para o aluno(a): "))
    return n

def resulatdo(n1,n2):
    media=(n1+n2)/2
    print("Nota 1: ", n1)
    print("Nota 2: ", n2)
    print("Média: ", media, "Resultado: ", end="")
    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")

a = lernotas()
b = lernotas()
resulatdo(a,b)
