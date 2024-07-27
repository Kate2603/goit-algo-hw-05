def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0

    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return (iterations, arr[mid])
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    if left < len(arr):
        return (iterations, arr[left])
    return (iterations, None)

# Приклад використання
arr = [1.1, 2.5, 3.6, 4.8, 5.9]
target = 3.5
print(binary_search(arr, target))
target = 6.0  # Елемент не існує в масиві
print(binary_search(arr, target))  # Виведе: (3, None)