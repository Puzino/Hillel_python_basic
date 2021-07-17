import random

point_A = {'x': random.randint(-10, 10),
           'y': random.randint(-10, 10)}

point_B = {'x': random.randint(-10, 10),
           'y': random.randint(-10, 10)}

point_C = {'x': random.randint(-10, 10),
           'y': random.randint(-10, 10)}

triangle_ABC = {'A': point_A,
                'B': point_B,
                'C': point_C}

print(triangle_ABC)
