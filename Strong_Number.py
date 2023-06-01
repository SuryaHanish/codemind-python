def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def is_strong_number(num):
    digit_sum = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        digit_sum += factorial(digit)
        temp //= 10

    return digit_sum == num

# Example usage
number = int(input())
if is_strong_number(number):
    print(f"The number {number} is a strong number")
else:
    print(f"The number {number} is not a strong number")
