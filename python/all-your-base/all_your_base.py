def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if not all([True if input_base > digit >= 0 else False for digit in digits]):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    if not digits or set(digits) == {0}:
        return [0]

    data = sum(digit * input_base ** pos for pos, digit in enumerate(reversed(digits)))

    result = []
    while data:
        div, mod = divmod(data, output_base)
        result.append(mod)
        data = div
    return list(reversed(result))