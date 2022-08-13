sexo = str(input('Digite o sexo [M/F]: ')).upper()
# not in é: "não estiver"
while sexo not in 'M''F':
    sexo = str(input('Digite novamente uma das opções [M/F]: ')).upper()
