def armstrong(n):
    num = n

    string = len(str(num))
    total = 0
    while num > 0:
        last = num % 10
        total = total + last ** string
        num = num // 10

    return n == total

print(armstrong(1634))