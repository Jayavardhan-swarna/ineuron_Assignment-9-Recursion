def productOfArray(arr):
    product = 1
    for num in arr:
        product *= num
    return product


arr = [1, 2, 3, 4, 5]
result = productOfArray(arr)
print(result)  # Output: 120 
