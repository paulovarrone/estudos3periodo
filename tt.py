lo = ['pam', 'momaco','banana', 'paudim', 'sacola', 'lolapaloza']

f = [g for g in lo if 'm' in g]

a = ', '.join(map(str,f))

print(a)


vec = [[1,2,3], [4,5,6], [7,8,9]]
v=list(zip(*vec))
print(v)


z = {x for x in 'abracadabra' if x not in 'abc'}
print(z)

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

intersection = {x for x in set2 if x not in set1}

print(intersection)

c = [x*10 for x in range(6)]
xx=', '.join(map(str,c))
print(xx)


# numeros = [x*11000 for x in range(100000000)]
# print(getsizeof(numeros))
# numeros = (x*11000 for x in range(100000000))
# print(getsizeof(numeros))

m = set1 | set2 #uniao
b = set1 - set2 #diferença
c = set1 ^ set2 #valores unicos sem duplicados
d = set1 & set2 #interseçao
print(m,b,c,d)


