import numpy as np

def cosine_similarity(vector_a, vector_b):
        cosine_similarity = np.dot(vector_a, vector_b)/(np.linalg.norm(vector_a)*np.linalg.norm(vector_b))
        return cosine_similarity