import random

MIN_LIMIT = -10
MAX_LIMIT = 10


def create_point(min_limit=MIN_LIMIT, max_limit=MAX_LIMIT):
    point = {'x': random.randint(min_limit, max_limit),
             'y': random.randint(min_limit, max_limit)}
    return point


def create_triangle(points_name: str) -> dict:
    return {key: create_point() for key in points_name}


def print_triangles_list(triangles_list: list) -> None:
    for triangle in triangles_list:
        print('---------------------------------------')
        print(triangle)
        print('---------------------------------------')


# triangle_ABC = create_triangle('ABC')
# triangle_MNK = create_triangle('MNK')
# print(triangle_ABC)
# print(triangle_MNK)

triangle_list = []
names = ['ABC', 'MNK', 'QWE', 'ZSD']
for name in names:
    triangle = create_triangle(name)
    triangle_list.append(triangle)

print_triangles_list(triangle_list)
