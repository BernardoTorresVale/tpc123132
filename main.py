''' Declare uma lista para guardar as vendas do grupo central
Declara uma lista para guardar os nomes das cinco ilhas do grupo central
Peça dados ao utilizador e guarde-os na lista
Após o utilizador ter inserido os 5 valores apresente:
- Total das vendas
- O menor valor inserido
- O maior valor inserido
- A média das vendas '''
# definir variaveis

lista_ilhas = ['graciosa', 'sao jorge', 'terceira', 'pico', 'faial']
Lista_vendas = [0, 0, 0, 0, 0]
# recolha dos valores (loop)
# for i in enumerate(lista_ilhas):
for i in range(0, len(lista_ilhas)):
    valor = print(input('insira um valor das vendas para a ilha ' + lista_ilhas[i]))
    Lista_vendas[i] = valor
for j in range(0, len(Lista_vendas)):
    print(Lista_vendas[j])
