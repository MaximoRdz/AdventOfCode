import numpy as np

positions = [[1, 0], [0, 1]]
a, b = positions

a, b = np.array(a), np.array(b)

a_mod = np.sqrt(a.dot(a))
b_mod = np.sqrt(b.dot(b))

cosine_angle = a.dot(b) / (a_mod*b_mod)

angle = np.arccos(cosine_angle) * 180 / np.pi

print(angle)

# Assume we have a list of points

centroids = [
    [1, 2, 3], 
    [-2, 5, 0], 
    [3, -1, 4], 
    [0, 0, 0], 
    [7, 2, -1], 
    [-3, 6, 2], 
    [4, 4, 1], 
    [-5, -3, 6], 
    [2, -2, -2], 
    [6, 1, 5]
    ]
centroids = np.array(centroids)

conn_vectors = centroids[1:] - centroids[:-1]

def get_cosine_angle(a, b):
    a_mod = np.sqrt(np.dot(a, a))
    b_mod = np.sqrt(np.dot(b, b))

    cosine_angle = np.dot(a, b) / (a_mod*b_mod)

    angle = np.arccos(cosine_angle) * 180 / np.pi

    return angle


print(conn_vectors[1:]-conn_vectors[:-1])
print(list(map(lambda vec: get_cosine_angle(vec[1:], vec[:-1]), conn_vectors)))
print(get_cosine_angle(np.array([0, 1]), np.array([1, 0])))
