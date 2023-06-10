def isPowerOfTwo(n):
    if n <= 0:
        return False

    # Count the number of bits set to 1
    count = 0
    while n > 0:
        if n & 1 == 1:
            count += 1
        n >>= 1

    return count == 1

# Example usage:
n = 16
result = isPowerOfTwo(n)
print(result)  # Output: True 
