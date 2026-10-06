from app.vector_store.vector_store import VectorStore
import numpy as np

# numbers = np.array([1,2,3,4,5])

# print(numbers)
# print(type(numbers))

# ==========================================================

# vector = np.array([0.1, 0.2, 0.3, 0.4])

# print(vector.shape)

# ==========================================================

# vector = np.array([10, 20, 30, 40])

# print(vector[0])
# print(vector[2])
# print(vector[-1])

# ==========================================================


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

cosine_similarity = VectorStore.cosine_similarity(a,b)
print(cosine_similarity)