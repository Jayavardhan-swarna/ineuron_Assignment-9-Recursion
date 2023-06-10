def findNthTerm(a, d, N):
    nth_term = a + (N - 1) * d
    return nth_term

a = 2
d = 1
N = 5
result = findNthTerm(a, d, N)
print(result)  # Output: 6 
