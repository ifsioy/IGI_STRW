
def validate_x(x):
    if abs(x) > 1:
        raise ValueError("x must be in the range (-1, 1)")