robo = int(input('Insira um id do robô de 0 a 11: '))
if robo >= 0 and robo <= 11:
    ids = [
        'rosa - rosa - rosa - verde',
        'verde - rosa - rosa - verde',
        'verde - verde - rosa - verde',
        'rosa - verde - rosa - verde',
        'verde - verde - rosa - verde',
        'rosa - rosa - verde - rosa',
        'verde - rosa - verde - rosa',
        'verde - verde - verde - rosa',
        'verde - verde - rosa - verde',
        'verde - verde - verde - verde',
        'rosa - rosa - rosa - rosa',
        'rosa - rosa - rosa - rosa',
        'rosa - rosa - verde - verde',
        'verde - verde - rosa - rosa'
    ]
    print(f'A sequência correta é: {ids[robo]}')
else:
    print('Opção inválida!')