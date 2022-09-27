if __name__ == '__main__':
    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    frase = input('Insere uma frase: ')
    x = 0
    for c in frase:
        x += 1

    print(f'A frase tem {x} caracters = {len(frase)}')