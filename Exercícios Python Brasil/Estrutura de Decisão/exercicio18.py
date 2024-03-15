# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
data = input('Insira uma data no formato dd/mm/yyyy: ')
dia, mes, ano = data.split('/')
dia = int(dia)
mes = int(mes)
ano = int(ano)
mesesCom31dias = [1, 3, 5, 7, 8, 10, 12]
if ano > 1 and mes in range(1, 12) and dia in range(1, 31):
    if mes == 2:
        if ano % 4 == 0 and not str(ano).endswith("00"):
            if dia in range(1, 29):
                print('A data é válida!')
            else:
                pass
        else:
            print('A data é inválida!')
    if mes not in mesesCom31dias and dia > 30:
        print('A data é inválida')
    else:
        print('A data é válida!')
else:
    print('A data é inválida')