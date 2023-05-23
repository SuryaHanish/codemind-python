def reverse_integer(num):
    # Check if the number is negative
    is_negative = False
    if num < 0:
        is_negative = True
        num = abs(num)

    # Convert the number to a string and reverse it
    num_str = str(num)
    reversed_str = num_str[::-1]

    # Convert the reversed string back to an integer
    reversed_num = int(reversed_str)

    # Restore the sign if the number was originally negative
    if is_negative:
        reversed_num *= -1

    return reversed_num

# Example usage
number = int(input())
reversed_number = reverse_integer(number)
print(f"{reversed_number}")