import random


def create_point(min_limit, max_limit):
    point = {'x': random.randint(min_limit, max_limit),
             'y': random.randint(min_limit, max_limit)}
    return point


def create_triangle(points_name, min_limit, max_limit):
    return {key: create_point(min_limit, max_limit) for key in points_name}


# point_A = create_point()
# point_B = create_point()
# point_C = create_point()

# triangle_ABC = {key: create_point() for key in 'ABC'}

# triangle_ABC = {'A': create_point(),
#                 'B': create_point(),
#                 'C': create_point()}

triangle_ABC = create_triangle('ABC', -10, 10)
triangle_MNK = create_triangle('MNK', -10, 10)

print(triangle_ABC)
print(triangle_MNK)