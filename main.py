def multiply_one_iteration(n, m):
    """
    Multiply two numbers using a single iteration method.
    
    Args:
    n (int): First number
    m (int): Second number
    
    Returns:
    int: Product of n and m
    """
    return n * m

def multiply_n_iterations(n, m):
    """
    Multiply two numbers using N iterations (adding n to itself m times).
    
    Args:
    n (int): First number (multiplicand)
    m (int): Second number (multiplier)
    
    Returns:
    int: Product of n and m
    """
    # Handle special cases
    if m == 0:
        return 0
    
    # Initialize result
    result = 0
    
    # Absolute value of m to handle negative numbers
    iterations = abs(m)
    
    # Add n to result m times
    for _ in range(iterations):
        result += n
    
    # Handle sign based on original m
    return result if m >= 0 else -result

def main():
    # Test cases
    test_cases = [
        (5, 3),    # Positive numbers
        (7, 0),    # Multiplication by zero
        (4, -2),   # Multiplication by negative number
        (-6, 3),   # Negative first number
        (-4, -5)   # Both numbers negative
    ]
    
    print("Multiplication Method Comparison:")
    print("-" * 40)
    
    for n, m in test_cases:
        # Method 1: Single iteration (built-in multiplication)
        result1 = multiply_one_iteration(n, m)
        
        # Method 2: N iterations
        result2 = multiply_n_iterations(n, m)
        
        # Print results
        print(f"\nMultiplying {n} × {m}:")
        print(f"One Iteration Method:  {result1}")
        print(f"N Iterations Method:   {result2}")
        print(f"Results Match:         {result1 == result2}")

if __name__ == "__main__":
    main()