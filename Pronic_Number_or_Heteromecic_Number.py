def is_pronic_number(num):
    for i in range(int(num**0.5) + 1):
        if i * (i + 1) == num:
            return True
    return False

# Example usage
number = int(input())
if is_pronic_number(number):
    print("YES")
else:
    print("NO")