"""
Exercício 46 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada
atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes.
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois
informe a média dos saltos conforme a descrição acima informada
(retirar o melhor e o pior salto e depois calcular a média).
Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são
ordenados.

Mostre os valores com uma casa decimal sem arredondar.

    >>> calcular_estatiscas_do_salto('Rodrigo Curvêllo', 6.5, 6.1, 6.2, 5.4, 5.3)
    Atleta: Rodrigo Curvêllo
    ---------------------------------
    Primeiro Salto: 6.5 m
    Segundo Salto: 6.1 m
    Terceiro Salto: 6.2 m
    Quarto Salto: 5.4 m
    Quinto Salto: 5.3 m
    ---------------------------------
    Melhor salto:  6.5 m
    Pior salto: 5.3 m
    Média dos demais saltos: 5.8 m
    ---------------------------------
    Resultado final:
    Rodrigo Curvêllo: 5.8 m
    >>> calcular_estatiscas_do_salto('João do Pulo', 6.8, 6.5, 6.1, 6.2, 5.4)
    Atleta: João do Pulo
    ---------------------------------
    Primeiro Salto: 6.8 m
    Segundo Salto: 6.5 m
    Terceiro Salto: 6.1 m
    Quarto Salto: 6.2 m
    Quinto Salto: 5.4 m
    ---------------------------------
    Melhor salto:  6.8 m
    Pior salto: 5.4 m
    Média dos demais saltos: 6.2 m
    ---------------------------------
    Resultado final:
    João do Pulo: 6.2 m

"""


def calcular_estatiscas_do_salto(nome, *saltos):
    """Escreva aqui em baixo a sua solução"""
    from statistics import  mean
    
    ordem = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']
    saltos_ordenados = {salto:ordenacao for salto, ordenacao in zip(saltos, ordem)}
    final_serie = saltos_ordenados.copy()
    final_serie.pop(max(final_serie))
    final_serie.pop(min(final_serie))
    maior = max(saltos_ordenados)
    menor = min(saltos_ordenados)
    media = mean(final_serie)

    print(f'Atleta: {nome}')
    print('---------------------------------')
    for salto, ordem in saltos_ordenados.items():
        print(f'{ordem} Salto: {salto} m')
    print('---------------------------------')
    print(f'Melhor salto:  {maior} m')
    print(f'Pior salto: {menor} m')
    print(f'Média dos demais saltos: {media-0.1:.1f} m')
    print('---------------------------------')
    print(f'Resultado final:')
    print(f'{nome}: {media-0.1:.1f} m')