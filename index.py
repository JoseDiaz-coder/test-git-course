def multiply(a, b):
    result = 0
    positive = b == abs(b)

    for _ in range(abs(b)):
        result = result + a if positive else result - a

    return result

result = multiply(2,3)
print(result)

result_add = lambda a, b: a + b
print(result_add(2,3))

result_subs = lambda a, b: a - b
print(result_subs(2,3))



