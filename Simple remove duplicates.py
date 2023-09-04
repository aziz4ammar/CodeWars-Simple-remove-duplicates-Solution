def solve(arr):
    unique_elements = []
    for item in reversed(arr):
        if item not in unique_elements:
            unique_elements.append(item)
    return list(reversed(unique_elements))