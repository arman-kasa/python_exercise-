def is_valid_triangle(sides):
    """Check that all sides are positive and satisfy the triangle inequality."""
    a, b, c = sorted(sides)
    return a > 0 and a + b >= c


def equilateral(sides):
    return is_valid_triangle(sides) and len(set(sides)) == 1


def isosceles(sides):
    return is_valid_triangle(sides) and len(set(sides)) <= 2


def scalene(sides):
    return is_valid_triangle(sides) and len(set(sides)) == 3
