def tabuada(multiplicacao):
    for cont in range(1, 11):
        print('{0} x {1} = {2}'.format(multiplicacao, cont, multiplicacao * cont))

if __name__ == '__main__':
    num = int(input('Digite um número: '))
    tabuada(num)
