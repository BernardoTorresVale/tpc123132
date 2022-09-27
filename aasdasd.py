if __name__ == '__main__':

    frase = input(f'Escreve algo: ')
    resultado = ''
    for c in frase:
        resultado = c + resultado
    print(resultado)

    palavra = ''

    list_palavras = []
    for c in frase:
        if c == ' ':
            list_palavras.append(palavra)
            palavra = ''

        else:
            palavra = palavra + c

    if palavra != '':
        list_palavras.append(palavra)

    print(list_palavras)


