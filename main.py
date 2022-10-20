Exercise 03
def isprime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True
num = int(input("Enter a prime number: "))
print(isprime(num))

#Exercise 11
# def cash_register(price, cash):
#     bills = [100_000,50_000,20_000,10_000,5_000,2_000,1_000,500,200,100]
#     money = []
#     change = cash - price
#     x = 0
#     while True:
#         i