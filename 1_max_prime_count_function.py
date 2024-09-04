def is_prime(num):
    if num < 2:
        return  
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_divisors(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            if is_prime(i):
                count += 1
    return count

numbers = []
for _ in range(10):
    num = int(input())
    numbers.append(num)

max_num = 0
max_count = 0
for num in numbers:
    div_count = count_divisors(num)
    if div_count > max_count:
        max_count = div_count
        max_num = num
    elif div_count == max_count and num > max_num:
        max_num = num

print(max_num, max_count)