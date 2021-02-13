def multiply(a, b):
    result = 0
    positive = b == abs(b)

    for _ in range(abs(b)):
        result = result + a if positive else result - a

    return result

result_add = lambda a, b: a + b

result_subs = lambda a, b: a - b



