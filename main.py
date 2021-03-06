from api import *

def main():
    while True:
        print('\n'*100)
        print('----------- Cambio ----------')
        opc = int(input('Escolha uma opção \n1 - Real para Dolar\n2 - Dolar para Real\n0 - Sair\n: '))
        if opc == 1:
            real = float(input('Quantos Reais você deseja converter em dolar ? '))
            dolar = realParaDolar(real)
            print(f'R${real} Equivalem a U${dolar}')
            
        elif opc == 2:
            dolar = float(input('Quantos Dolares você deseja converter em Reais ? '))
            real = dolarParaReal(dolar)
            print(f'U${dolar} Equivalem a R${real}')
            
        elif opc == 0:
            break
        else:
            print('Opção Invalida, tente novamente\n')
        input('...')

main()