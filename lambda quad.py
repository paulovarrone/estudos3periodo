n = int(input())
nn = int(input())

f = lambda x: x **2
print(f(n))

k = lambda x,y : x*y
print(k(n,nn))

j = lambda x: "par" if x % 2 == 0 else "impar"
print(j(n))