for n in range(1000, 10000):
    a = n // 1000
    b = n % 1000 // 100
    c = n % 100 // 10
    d = n % 10
    x = max(a + b, b + c, c + d)
    y = a + b + b + c + c + d - x - min(a + b, b + c, c + d)
    if (x == 6 and y == 13) or (y == 6 and x == 13):
        print(n)
        break
