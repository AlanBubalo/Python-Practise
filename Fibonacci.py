def fibonacci(num):
    f = []
    c = 0
    if num < 1:
        return f
    f.append(1)
    for i in range(num-1):
        f.append(c+f[i])
        c = f[i]
    return f

num = int(input("Enter a number: "))
print(fibonacci(num))