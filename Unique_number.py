def has_unique_digits(num):
    digits = str(num)
    unique_digits = set(digits)
    return len(digits) == len(unique_digits)

# Example usage
number = int(input())
if has_unique_digits(number):
    print("Unique Number")
else:
    print("Not Unique Number")