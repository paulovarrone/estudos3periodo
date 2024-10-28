cu = [1,2,3,4,5,6,7,8,9,10]

i = list(map(lambda x: 'par' if x % 2 == 0 else "impar",cu))
c = ', '.join(i)
print(c)

capi = {
    'Brasil' : 'Brasilia',
    'Africa' : "Uganda"
}

inp = input()

if inp in capi:
     print(f'{inp}-{capi[inp]}')
else:
     print('nao')


for p,cap in capi.items():
    if inp == p:
        print(f'{p}=={cap}')
        break
else:
        print('nao')
        