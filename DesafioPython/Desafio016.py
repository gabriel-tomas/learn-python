lista_cores = {'a': '\033[30m', 'b': '\033[31m', 'c': '\033[32m',
               'd': '\033[33m', 'e': '\033[34m', 'f': '\033[35m', 'g': '\033[36m', 'h': '\033[37m'}
num = float(input('{}Dig{}ite {}um {}núm{}ero: '.format(lista_cores['a'], lista_cores['b'],
                                                        lista_cores['f'], lista_cores['g'],
                                                        lista_cores['c'])))
print('{}A {}pa{}rte {}inte{}ira {}de {} é {}'.format(lista_cores['h'], lista_cores['e'],
                                                    lista_cores['d'], lista_cores['a'],
                                                    lista_cores['f'], lista_cores['c'],
                                                    num, int(num)))
