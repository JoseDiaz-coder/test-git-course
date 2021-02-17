from index import multiply, result_add, result_subs
from modules import rosario

def prints():
    result = multiply(1,2)
    print(result)

    result = result_add(1,2)
    print(result)

    result = result_subs(1,2)
    print(result)

prints()

resar = rosario()

print("se resa el rosario en familia") if resar else print("se resa solo")
