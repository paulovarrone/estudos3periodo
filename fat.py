def fat(n):
    if n == 0 or n == 1:
        r = 1
    else:
        r = n * fat(n-1)

    return r

n = int(input('Digite um numero'))

print(fat(n))