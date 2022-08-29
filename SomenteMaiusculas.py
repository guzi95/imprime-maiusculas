'''
Este programa imprime somente as letras maiúsculas de uma string dada pelo usuário.
'''

def maiusculas(frase):
    '''
    Faz lista de códigos unicode correspondentes a caracteres especiais e números.
    '''
    n = 33
    unicode = []
    while 33 <= n <= 63:
        unicode.append(n)
        n += 1
        
    '''
    Elimina da frase caracteres especiais e números.
    '''
    for i in range(len(unicode)):
        for j in range(len(frase)):
            if unicode[i] == ord(frase[j]):
                frase = frase.replace(frase[j], " ")
            
    frase = frase.replace(" ", "")

    '''
    Compõe uma string.
    '''
    somente_maiusculas = ''          
    for j in range(len(frase)):
        if frase[j] == frase[j].upper():
            somente_maiusculas = somente_maiusculas + frase[j]
        
    return somente_maiusculas
