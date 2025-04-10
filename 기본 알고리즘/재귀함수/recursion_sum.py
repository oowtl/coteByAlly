def sum_function(n: int)-> int:
    if n == 1:
        return 1
    return n + sum_function(n - 1)

s = sum_function(10)
print(s)