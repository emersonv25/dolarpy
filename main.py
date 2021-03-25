# CRIADORES: EMERSON E MATHEU
from api import *

def main():
    while True:
        print('\n'*100)
        print('----------- Cambio ----------')
        print(f'      U${getUSD()} -> R$ 1.00\n') 
        try:
            opc = int(input('Escolha uma opção \n1 - Real para Dolar\n2 - Dolar para Real\n0 - Sair\n: '))
            
            if opc == 1:

                formulario('Quantos Reais você deseja converter em dolar ?\n:', realParaDolar, 'R$ FUNCnum1 equivalem a U$ FUNCnum2')
                
            elif opc == 2:
                formulario('Quantos Dolares você deseja converter em Reais ?\n:', dolarParaReal, 'U$ FUNCnum1 equivalem a R$ FUNCnum2')
                
            elif opc == 0:
                break
            else:
                print('Opção Invalida, tente novamente\n')
        except:
            print("Input invalido!!!\nApenas nÚmeros são aceitos.")
        input('...')


if __name__ == "__main__":
    main()