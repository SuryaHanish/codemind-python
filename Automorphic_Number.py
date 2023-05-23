def is_automorphic_number(num):
    square = num ** 2
    num_str = str(num)
    square_str = str(square)
    if square_str.endswith(num_str):
        return True
    return False

# Example usage
number = int(input())
if is_automorphic_number(number):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")