from sympy import pi, sympify

def convt_d2r(degree):
    """
    Convert degrees to radians symbolically
    """
    radians = degree * (pi / 180)
    return radians

# Get input from the user
angle_in_degree = input('Give me an angle in degrees: ')
angle_in_degree = sympify(angle_in_degree)  # Convert input string to a symbolic expression

# Convert degrees to radians
radian = convt_d2r(angle_in_degree)
print(f"{angle_in_degree} degrees is {radian} radians (symbolically).")

