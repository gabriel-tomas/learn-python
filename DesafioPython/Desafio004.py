p1 = input('\033[45;7m\033[1mDigite algo: ')
print(type(p1), '\033[m')
print('\033[45;7mis alpha numeric:', p1.isalnum(), '\033[m')
print('\033[45;7mis numeric:', p1.isnumeric(), '\033[m')
print('\033[45;7mis 001001:', p1.isascii(), '\033[m')
print('\033[45;7mis digit:', p1.isdigit(), '\033[m')
print('\033[45;7mis lower:', p1.islower(), '\033[m')
print('\033[45;7mis decimal:', p1.isdecimal(), '\033[m')
print('\033[45;7mis supper:', p1.isupper(), '\033[m')
print('\033[45;7mis space:', p1.isspace(), '\033[m')
print('\033[45;7mis printable:', p1.isprintable(), '\033[m')
print('\033[45;7mis identifier:', p1.isidentifier(), '\033[m')