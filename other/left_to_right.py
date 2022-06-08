def left_to_right(a, b):
    m = bin(b)
    res = 1
    for i in range(2, len(m)):
        if m[i] == '1':
            res = res ** 2 * a
        else:
            res **= 2
    return res
    

def right_to_left(a, b):
    m = bin(b)
    z = a
    res = 1
    for i in range(len(m) - 1, 2, -1):
        if m[i] == '1':
            res *= z
            z **= 2
        else:
            z **= 2
    return res * z

x, y = 2, 64
if left_to_right(x, y) == right_to_left(x, y) == x ** y:
    print("Верно")
else:
    print("Не верно")
