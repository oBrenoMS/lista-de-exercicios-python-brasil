"""
Exercício 04 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a
população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o
número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas
de crescimento.

    >>> calcular_ano_ultrapassagem_populacional()
    'População de A, depois de 63 ano(s) será de 515033 pessoas, superando a de B, que será de 510964 pessoas'


"""


def calcular_ano_ultrapassagem_populacional() -> str:
    """Escreva aqui em baixo a sua solução"""
A = 80000
B = 200000
taxa_A = 0.03
taxa_B = 0.015

anos = 0
while A < B:
    A = A + (A * taxa_A)
    B = B + (B * taxa_B)
    anos += 1

print (f"'População de A, depois de {anos} ano(s) será de {int(A)} pessoas, superando a de B, que será de {int(B)} pessoas'")
