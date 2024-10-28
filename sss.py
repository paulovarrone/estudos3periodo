# ent = input()

# if ent.isnumeric():
#     ent = int(ent)
#     g = ent % 2 == 0
#     p = 'impar'

#     if g:
#         p = 'par'

#     print(p)
# else:
#     print("erro")



# try:
#     n = input('Digite nome: ')
#     tam = len(n)
#     g = tam > 6
#     m = tam >= 5
#     if tam > 0:
#         if n.isnumeric():
#             print('erro')
#         else:    
#             if g:
#                 print('seu nome grande')
#             elif m:
#                 print('nome normal')
#             else:
#                 print('nome curto')
#     else:
#         print('voce nao digitou o nome')

# except (ZeroDivisionError, IndexError, FileNotFoundError):
#     print('Usuario parou o programa')
# except Exception as e:
#     print(f'erro {e}')

# nome = 'çççççpwwwwwaaaaaaaaaaaaaaaaaaulo alberto                                                                           '
# cont = 0
# g = ''

# for letra in nome:
     
#     if letra == ' ':
#         continue

#     cont_l = nome.count(letra)

#     if cont < cont_l:
#         cont = cont_l
#         g = letra

#     print(f'*{letra}', end='')
 
# print()
# print(g,cont)

# for i in range(1,11):
#     if i == 2:
#         print('i é 2, pulando...')
#         continue

#     if i == 8:
#         print('i é 8, seu else não executará')
#         break

#     for j in range(1,3):
#         print(i, j)
# else:
#     print('For completo com sucesso!')

secreta = 'cuzinho'
chute = []
c = True
cont = 0
for i in secreta:
       chute.append('*')

while c:
    
    tamanho_secreta = len(secreta)
    print()
    letra = input('Digite uma letra: ')
    print()

    cont += 1

    if len(letra) > 1:
        print('Digite apenas uma letra')

    if letra in chute:
         print('Ja chutou essa')
    
    
    for i in range(tamanho_secreta):         
        if secreta[i] == letra:
            chute[i] = letra
       

    certo = ''.join(chute)

    print(certo)   

    if certo == secreta:
        c = False


print(f'PARABENS A PALAVRA É {secreta} ---- {cont}tentativa')   

