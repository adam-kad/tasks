#Символ Лежандра

def legandra(a, p):
    if a == 1:
        return 1
    elif a % 2 == 0:
        return legandra(a // 2, p) * (-1) ** ((p ** 2 - 1) // 8)
    elif a % 2 != 0 and a != 1:
        return legandra(p % a, a) * (-1) ** (((a - 1) * (p - 1)) // 4)


#a = int(input('a: '))
#p = int(input('p: '))
#print(legandra(a, p))


#Символ Якоби
def Jacobi(a, n):
        assert(n > a > 0 and n%2 == 1)
        t = 1
        while a != 0:
            while a % 2 == 0:
                a /= 2
                r = n % 8
                if r == 3 or r == 5:
                    t = -t
            a, n = n, a
            if a % 4 == n % 4 == 3:
                t = -t
            a %= n
        if n == 1:
            return t
        else:
            return 0
            
a = int(input('a: '))
n = int(input('n: '))
print(Jacobi(a, n))


