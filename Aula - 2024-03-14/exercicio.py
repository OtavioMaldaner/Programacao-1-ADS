user = input('Digite seu login: ')
password = input('Digite sua senha: ')
match user:
    case 'otaviomaldaner571@gmail.com':
        if password == '123':
            print('Bem vindo admiro')
        else:
            print('Tente novamente')
    case _:
        print('Tente novamente')