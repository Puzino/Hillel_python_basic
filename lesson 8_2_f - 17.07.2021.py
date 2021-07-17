import random


def create_point():
    point = {'x': random.randint(-10, 10),
             'y': random.randint(-10, 10)}
    return point


def create_triangle(points_name):
    return {key: create_point() for key in points_name}


# point_A = create_point()
# point_B = create_point()
# point_C = create_point()

# triangle_ABC = {key: create_point() for key in 'ABC'}

# triangle_ABC = {'A': create_point(),
#                 'B': create_point(),
#                 'C': create_point()}

triangle_ABC = create_triangle('ABC')
triangle_MNK = create_triangle('MNK')

print(triangle_ABC)
print(triangle_MNK)