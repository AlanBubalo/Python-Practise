num = int(input("Enter a number: "))

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(num, "is a prime number." if isPrime(num) else "is not a prime number.")
