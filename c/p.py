import os
p_secreta = 'cu'
chute = ''
c = True

while c:
    
    letra = input('Digite letra: ')

    if len(letra) > 1:
        print('Digite apenas uma letra!')
    
    if letra in p_secreta:
        chute += letra

    certo = ''
    for letra_d in p_secreta:
        if letra_d in chute:
            certo+= letra_d             
        else:
            certo += '*'
            
    print(certo)

    if certo == p_secreta:
        c = False

os.system('cls')  
print(f'parabens a palavra é {p_secreta}')