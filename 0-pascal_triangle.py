def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.
    
    Args:
        n (int): The number of rows of Pascal's triangle to generate.
        
    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        # Create a new row with 1s at the edges
        row = [1] * (i + 1)
        
        # Each triangle element (except the first and last) is the sum of the two above it
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        
        triangle.append(row)

    return triangle
