import random

MIN_LIMIT = -10
MAX_LIMIT = 10


def create_point(min_limit=MIN_LIMIT, max_limit=MAX_LIMIT):
    point = {'x': random.randint(min_limit, max_limit),
             'y': random.randint(min_limit, max_limit)}
    return point


def create_triangle(points_name):
    return {key: create_point() for key in points_name}


# triangle_ABC = create_triangle('ABC')
# triangle_MNK = create_triangle('MNK')
# print(triangle_ABC)
# print(triangle_MNK)

triangle_list = []
names = ['ABC', 'MNK', 'QWE', 'ZSD']
for name in names:
    triangle = create_triangle(name)
    triangle_list.append(triangle)

print(triangle_list)