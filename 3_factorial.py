def factorial(N):
    if N == 0 or N == 1:
        return 1

    result = 1
    for i in range(2, N + 1):
        result *= i

    return result


N = 5
result = factorial(N)
print(result)  # Output: 120 
