a = int(input('Digite numero'))
b = input('Digite expo')

def exp(a,b):
    if b == '':
       r= a**2
       print(r)
    else:
        r = a**int(b)
        print(r)

exp(a,b)



