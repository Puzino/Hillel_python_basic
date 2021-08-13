import random

# DRY

point_A = {"x": random.randint(-10, 10),
           "y": random.randint(-10, 10)}

point_B = {"x": random.randint(-10, 10),
           "y": random.randint(-10, 10)}

point_C = {"x": random.randint(-10, 10),
           "y": random.randint(-10, 10)}

triangle_ABC = {"A": point_A,
                "B": point_B,
                "C": point_C}

point_M = {"x": random.randint(-10, 10),
           "y": random.randint(-10, 10)}

point_N = {"x": random.randint(-10, 10),
           "y": random.randint(-10, 10)}

point_K = {"x": random.randint(-10, 10),
           "y": random.randint(-10, 10)}

triangle_MNK = {"M": point_M,
                "N": point_N,
                "K": point_K}

print(triangle_MNK)