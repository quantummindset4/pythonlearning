# Print numbers from 1 to 10, skipping multiples of 3
num = 1

while num <= 10:
    if num % 3 == 0:
        num += 1
        continue
    
    print(num, end=" ")
    num += 1
