def multiply(a, b):
    result = 0
    positive = b == abs(b)

    for _ in range(abs(b)):
        result = result + a if positive else result - a

    return result

def add(a, b):
    return a + b


result = multiply(1,2)
print(result)

result_add = add(1,2)
print(result_add)



