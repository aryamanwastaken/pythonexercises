from math import sqrt
def classify(number: int) -> str:
    """A perfect number equals the sum of its positive divisors.
 
    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    divisors = set()
    for i in range(1, int(sqrt(number)) + 1):
        if number % i == 0:
            divisors.add(i)
            divisors.add(number // i)
    if number in divisors:
        divisors.remove(number)
    aliquot_sum = sum(divisors)
    print(number, divisors, aliquot_sum)
    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    else:
        return "deficient"
