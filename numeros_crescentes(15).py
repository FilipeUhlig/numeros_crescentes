"""
Programa: Números crescentes
Descrição: Este programa lê e organiza em ordem crescente os números inseridos.
Autor: Filipe
Data: 06/06/2023
Versão: 0.0.1
"""
#Atribuição de variáveis


#Entrada de dados
n1 = float(input("Qual o primeiro número? "))
n2 = float(input("Qual o segundo número? "))
n3 = float(input("Qual o terceiro número? "))


#Processamento de dados
d = [n1, n2, n3]
r = sorted(d, key=float)

#Saida de dados
print(f"A ordem crescente dos números informados é {r}.")

