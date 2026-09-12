import torch 

def rowswap(matrix: torch.Tensor, row1: int, row2: int) -> torch.Tensor:
    """
    Swap two rows of a matrix.

    Args:
        matrix (torch.Tensor): The input matrix.
        row1 (int): The index of the first row to swap.
        row2 (int): The index of the second row to swap.

    Returns:
        torch.Tensor: The matrix with the specified rows swapped.
    """
    if row1 < 0 or row1 >= matrix.size(0) or row2 < 0 or row2 >= matrix.size(0):
        raise IndexError("Row indices are out of bounds.")

    # Create a copy of the matrix to avoid modifying the original
    swapped_matrix = matrix.clone()
    
    # Swap the rows
    swapped_matrix[[row1, row2]] = swapped_matrix[[row2, row1]]
    
    return swapped_matrix

def rowscale(matrix: torch.Tensor, row: int, scalar: float) -> torch.Tensor:
    """
    Scale a row of a matrix by a given scalar.

    Args:
        matrix (torch.Tensor): The input matrix.
        row (int): The index of the row to scale.
        scalar (float): The scalar value to multiply the row by.

    Returns:
        torch.Tensor: The matrix with the specified row scaled.
    """
    if row < 0 or row >= matrix.size(0):
        raise IndexError("Row index is out of bounds.")

    # Create a copy of the matrix to avoid modifying the original
    scaled_matrix = matrix.clone()
    
    # Scale the specified row
    scaled_matrix[row] *= scalar
    
    return scaled_matrix

def rowreplacement(matrix: torch.Tensor, target_row: int, source_row: int, i: float, j: float) -> torch.Tensor:
    """
    Replace a row of a matrix with a linear combination of itself and another row.

    Args:
        matrix (torch.Tensor): The input matrix.
        target_row (int): The index of the row to be replaced.
        source_row (int): The index of the row to be used for replacement.
        i (float): The scalar value to multiply the source row by before adding it to the target row.
        j (float): The scalar value to multiply the target row by before adding the scaled source row.

    Returns:
        torch.Tensor: The matrix with the specified row replaced.
    """
    if target_row < 0 or target_row >= matrix.size(0) or source_row < 0 or source_row >= matrix.size(0):
        raise IndexError("Row indices are out of bounds.")

    # Create a copy of the matrix to avoid modifying the original
    replaced_matrix = matrix.clone()
    
    # Replace the target row with the linear combination
    replaced_matrix[target_row] = j * replaced_matrix[target_row] + i * replaced_matrix[source_row]
    
    return replaced_matrix


def rref(matrix: torch.Tensor) -> torch.Tensor:
    """
    Compute the Reduced Row Echelon Form (RREF) of a matrix.

    Args:
        matrix (torch.Tensor): The input matrix.

    Returns:
        torch.Tensor: The RREF of the input matrix.
    """
    # Create a copy of the matrix to avoid modifying the original
    rref_matrix = matrix.clone().float()
    
    num_rows, num_cols = rref_matrix.size()
    lead = 0

    for r in range(num_rows):
        if lead >= num_cols:
            return rref_matrix
        i = r
        while rref_matrix[i, lead] == 0:
            i += 1
            if i == num_rows:
                i = r
                lead += 1
                if num_cols == lead:
                    return rref_matrix
        # Swap rows
        rref_matrix[[i, r]] = rowswap(rref_matrix, i, r)[[i, r]]
        
        # Scale the leading row
        rowscale_factor = rref_matrix[r, lead]
        rref_matrix[r] = rowscale(rref_matrix, r, 1.0 / rowscale_factor)[r]
        
        # Eliminate other rows
        for i in range(num_rows):
            if i != r:
                lv = rref_matrix[i, lead]
                rref_matrix[i] = rowreplacement(rref_matrix, i, r, -lv, 1.0)[i]
        
        lead += 1

    return rref_matrix


#



