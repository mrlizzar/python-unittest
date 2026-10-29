def area(width, height):
    if not isinstance(width, (int, float)) and isinstance(height, (int, float)):
        raise TypeError("width and height must be integers or floats")

    if not(width > 0 and height > 0):
        raise ValueError("width and height must be positive")



    return width * height