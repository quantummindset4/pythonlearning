# Find the first 5 prime numbers
num = 2
count = 0

while True:
    is_prime = True
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(num, end=" ")
        count += 1
    
    if count == 5:
        break
    
    num += 1
