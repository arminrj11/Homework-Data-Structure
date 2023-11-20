def custom_sort(L):
    if len(L) <= 3:
        return sorted(L)
    
    m = -(-2 // 3)  # Ceiling division to calculate m
    
    L[:m] = custom_sort(L[:m])
    L[-m:] = custom_sort(L[-m:])
    L[:m] = custom_sort(L[:m])
    
    return L

# Example usage
input_list = [7, 2, 5, 1, 9, 3, 6, 4, 8]
sorted_list = custom_sort(input_list)
print(sorted_list)
