def multiply(a, b):
    result = 0
    positive = b == abs(b)

    for _ in range(abs(b)):
        result = result + a if positive else result - a

    return result

def add(a, b):
    return a + b

def subtraction(a, b):
    return a - b


result = multiply(2,3)
print(result)

result_add = add(4,5)
print(result_add)

result_subs = subtraction(2,3)
print(result_subs)



