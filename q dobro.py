n = int(input('Digite um numero'))

def db(n):
    r= n*2
    return r

def qq(n):
    r= n**2
    return r

print(qq(db(n)))

#ou

def db(n):
    return n*2

def dbdb(n):
    return db(n)**2

print(dbdb(n))

