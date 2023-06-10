def findMax(arr, left, right):
    if left == right:
        return arr[left]

    mid = (left + right) // 2
    max_left = findMax(arr, left, mid)
    max_right = findMax(arr, mid + 1, right)

    return max(max_left, max_right)

arr = [1, 4, 3, -5, -4, 8, 6]
result = findMax(arr, 0, len(arr) - 1)
print(result)  # Output: 8 
