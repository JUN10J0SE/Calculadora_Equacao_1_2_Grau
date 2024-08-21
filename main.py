#inport da def
import equacoes as eq

#bloqueio da main
if __name__=='__main__':
    while True:
        eq.mostrar_menu()
        opcoes = input("Opoes desejada: ")
        match opcoes:
            case '1':
                a = float(input('Valor de "a": ').replace(',','.'))
                b = float(input('Valor de "b": ').replace(',','.'))
                print(f'Valor de x: {eq.calcular_grau_1(a,b)}.')
                continue
            case '2':
                a = float(input('Valor de "a": ').replace(',','.'))
                b = float(input('Valor de "b": ').replace(',','.'))
                c = float(input('Valor de "c": ').replace(',','.'))
                result = eq.calcular_grau_2(a,b,c)
                for x in result:
                    print(x)
                continue
            case '3':
                print('[Programa Encerrado]')
                break
            case _:
                print("Comando incorreto, tente novamente")
                continue #caso quisesse encerrar seria o 'break', para retornar o loop, usa o contibue