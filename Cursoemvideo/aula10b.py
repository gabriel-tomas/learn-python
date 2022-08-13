n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
mediastr = str(media)
print('Sua media foi '+mediastr)
print('Boa nota ' if media >= 6 else 'Esforçe-se mais')
