def check_digits(num):
    even_count = 0
    odd_count = 0

    while num != 0:
        digit = num % 10
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        num //= 10

    if even_count > 0 and odd_count > 0:
        return 0  # Mixed numbers
    elif even_count > 0:
        return 1  # Even numbers only
    else:
        return 2  # Odd numbers only

number = int(input())
result = check_digits(number)

if result == 0:
    print("Mixed")
elif result == 1:
    print("Even")
else:
    print("Odd")
