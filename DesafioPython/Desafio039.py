import datetime
p = str(input('Qual o sexo? ')).lower()
if p == 'feminino':
    print('Você não precisa fazer o alistamento obrigatório')
if p == 'masculino':
    ano = int(input('Digite o ano de nascimento: '))
    a = str(datetime.date.today())
    b = a.split('-')
    c = int(b[0]) - ano
    if c < 18:
        print('Você tem {} anos, ainda vai se alistar\nFalta {} anos para o alistamento.'.format(c, 18-c))
    elif c == 18:
        print('É a hora de se alistar ao serviço militar, você tem {} anos'.format(c))
    else:
        print('Já passou da hora de se alistar\nJá passaram {} anos do seu alistamento'.format(c-18))
