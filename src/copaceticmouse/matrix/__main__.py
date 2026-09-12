# example tensor
import torch

from elementary import rref
from elementary import rowswap, rowscale, rowreplacement

matrix = torch.tensor([[1,3,0,0,3], [0,0,1,0,9],[0,0,0,1,-4]], dtype=torch.float32)

matrix = rowswap(matrix, 0, 1)
print(matrix)

matrix = rowscale(matrix,0,1/3)
print(matrix)

matrix = rowreplacement(matrix, 2, 0, -3, 1)
print(matrix)