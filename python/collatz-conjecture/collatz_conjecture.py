def steps(number, total=0):
    if number <1:
        raise ValueError("Only positive integers are allowed")
    return total if number==1 else steps(3*number+1 if number %2 else number//2, total+1)