import numpy as np
import sys

def matmul(A, B):
    # If the input matrices are of size 1x1, return the element-wise product
    if A.shape[0] == 1 and A.shape[1] == 1 and B.shape[0] == 1 and B.shape[1] == 1:
        return A * B
    
    # Partition the input matrices into 4 sub-matrices
    A11, A12 = A[:len(A)//2, :len(A)//2], A[:len(A)//2, len(A)//2:]
    A21, A22 = A[len(A)//2:, :len(A)//2], A[len(A)//2:, len(A)//2:]
    B11, B12 = B[:len(B)//2, :len(B)//2], B[:len(B)//2, len(B)//2:]
    B21, B22 = B[len(B)//2:, :len(B)//2], B[len(B)//2:, len(B)//2:]
    
    # Calculate the sub-matrices of the result
    D11 = matmul(A11, B11)
    D12 = matmul(A11, B12)
    D21 = matmul(A21, B11)
    D22 = matmul(A21, B12)
    E11 = matmul(A12, B21)
    E12 = matmul(A12, B22)
    E21 = matmul(A22, B21)
    E22 = matmul(A22, B22)
    
    # Combine sub-matrices
    D1 = np.concatenate((D11, D12), axis=1)
    D2 = np.concatenate((D21, D22), axis=1)
    D = np.concatenate((D1, D2), axis=0)
    E1 = np.concatenate((E11, E12), axis=1)
    E2 = np.concatenate((E21, E22), axis=1)
    E = np.concatenate((E1, E2), axis=0)

    # Return combination of the sub-matrices
    return D + E

# Opens and parses input matrices from text files
def openFile(matFile):
    matrix = []
    with open(matFile, 'r') as f_read:
        for line in f_read:
            line = line.replace("\n", "")
            line_split = line.split(" ")
            curr_row = []
            for row_num in line_split:
                curr_row.append(int(row_num))
            matrix.append(curr_row)

    return np.array(matrix)



def __main__():
    if (len(sys.argv) != 3):
        print("CLI Format: python matmul_hw5.py <MatrixFile1.txt> <MatrixFile2.txt>")
        return
    
    # Ripped if statement from https://stackoverflow.com/questions/5899497/how-can-i-check-the-extension-of-a-file
    if not (sys.argv[1].endswith('.txt')) or not (sys.argv[2].endswith('.txt')):
        print("Please make sure are Matrix input parse files as text files (.txt)")
        return

    # open command line arguments
    mat1 = openFile(sys.argv[1])
    mat2 = openFile(sys.argv[2])

    # compute my implementation of divide and conquer matmul
    matmul_self_res = matmul(mat1, mat2)

    # compute the hopefully same matmul result using the numpy library
    matmul_res_np = np.matmul(mat1, mat2)

    # assert that the two matmul answers are correct
    assert np.array_equal(matmul_self_res, matmul_res_np)

    # print result if the two compuations produce the same array
    print("Matmul result: ")
    print(matmul_self_res)



if (__name__ == "__main__"):
    __main__()