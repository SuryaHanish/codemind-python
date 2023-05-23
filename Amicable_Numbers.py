def sum_proper_divisors(num):
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    return divisors_sum

def are_amicable_numbers(num1, num2):
    sum1 = sum_proper_divisors(num1)
    sum2 = sum_proper_divisors(num2)
    if sum1 == num2 and sum2 == num1:
        return True
    return False

# Example usage
number1 = int(input())
number2 = int(input())
if are_amicable_numbers(number1, number2):
    print("Amicable")
else:
    print("Not Amicable")