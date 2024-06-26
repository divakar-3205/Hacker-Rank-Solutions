def findDigits(n):
    count = 0
    original_number = n
    
    while n > 0:
        digit = n % 10
        if digit != 0 and original_number % digit == 0:
            count += 1
        n = n // 10
    
    return count
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    
    print(findDigits(n))
