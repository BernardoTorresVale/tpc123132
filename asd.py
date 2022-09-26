def divisores(num):
    zeros = 0
    for n in range(1, num + 1):
        if num % n == 0:
            zeros += 1 # zeros = zeros + 1
    return zeros


if __name__ == '__main__':
    continuar = 's'
    while continuar == 's':
        ini = int(input('insira um numero inicial '))
        fim = int(input('insira um numero final '))
        primos = 0
        for n in range(ini, fim +1):
            if divisores(n) == 2:
                primos += 1
        print(f'entre {ini} e {fim} há {primos} de primos. ')
        continuar = input('Repetir [s, n]? ')
        print(f'Adeus!')