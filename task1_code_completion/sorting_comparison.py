# task1_code_completion/sorting_comparison.py
def manual_sort_dicts(data, key):
    """
    Manual implementation of dictionary sorting using bubble sort algorithm.
    This demonstrates a basic approach without using built-in sorting functions.
    Time complexity: O(n²)
    """
    arr = data.copy()
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j][key] > arr[j+1][key]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def efficient_sort_dicts(data, key):
    """
    Efficient implementation using Python's built-in sorted function.
    Utilizes Timsort algorithm which is optimized and implemented in C.
    Time complexity: O(n log n)
    """
    return sorted(data, key=lambda x: x[key])

def generate_test_data(size):
    """Generate sample list of dictionaries for testing"""
    import random
    
    test_data = []
    for i in range(size):
        test_data.append({
            'id': i,
            'priority': random.randint(1, 10),
            'value': random.uniform(1.0, 100.0),
            'name': f'item_{i}'
        })
    return test_data

# Example usage and comparison
if __name__ == "__main__":
    # Test with different sizes
    sizes = [10, 50, 100]
    
    for size in sizes:
        data = generate_test_data(size)
        
        # Manual sorting
        import time
        start_time = time.time()
        manual_result = manual_sort_dicts(data, 'priority')
        manual_time = time.time() - start_time
        
        # Efficient sorting
        start_time = time.time()
        efficient_result = efficient_sort_dicts(data, 'priority')
        efficient_time = time.time() - start_time
        
        print(f"Size {size}: Manual={manual_time:.6f}s, Efficient={efficient_time:.6f}s")
