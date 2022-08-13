s = c = 0
while True:
    n = int(input('Digite um número [Digite 999 para parar]: '))
    if n == 999:
        break
    s = s + n
    c = c + 1
print(f'A soma foi {s} e foram digitados {c} números')
