import time
def dados():
    while True:
         try:
            opcao=str(input('Aceita ter seus dados coletados? [S/N]: ')).strip().upper()
            if opcao in 'SN':
                 break
            else:
                 raise ValueError
         except ValueError:
            print('Opção inválida!')
    if opcao=='S':
        analise=dict()
        while True:
            try:
                analise['nome']=str(input('Digite seu nome: ')).strip().title()
                if not analise['nome'].replace(' ', '').isalpha():
                    raise ValueError
                break
            except ValueError:
                print('Isso não é um nome válido!')
        while True:
            try:
                analise['idade']=int(input('Digite sua idade: '))
                if analise['idade'] < 0:
                    raise ValueError
                break
            except ValueError:
                print('Isso não é uma idade válida!')
        if analise['idade']>=18:
            print(f'{analise["nome"]} é maior de idade.')
        else:
            print(f'{analise["nome"]} é menor de idade.')
        while True:
            try:
                analise['sexo']=str(input('Digite seu sexo [M/F]: ')).strip().upper()
                if analise['sexo'] in 'MF':
                    break
                else:
                    raise ValueError
            except ValueError:
                print('Isso não é um sexo!')
        print('Gerando seus dados...')  
        for c in range(0,5):
            print('.', end='', flush=True)
            time.sleep(1)
        print('Aqui estão seus dados:')
        for k, v in analise.items():
            print(f'{k} ==> {v}')      
    elif opcao=='N':
        print('Você não quis ter seus dados coletados. Volte sempre!')
    print('Lembre-se sempre do L')
dados()
