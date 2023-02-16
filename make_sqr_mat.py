import sys
import random

def fillMatrix(N):
    matrix = []
    for _ in range(N):
        curr_row = []
        for _ in range(N):
            curr_row.append(str(random.randrange(1,10)))
        matrix.append(curr_row)
    return matrix

def writeOutMatFile(filePath, matrix):
    filePath = filePath.replace(".txt", "")
    pathA = filePath + "_matA.txt"
    pathB = filePath + "_matB.txt"
    with open(pathA, "w") as pathA_w:
        with open(pathB, "w") as pathB_w:
            for row in matrix:
                for num in row[:-1]:
                    pathA_w.write(num + " ")
                    pathB_w.write(num + " ")
                pathA_w.write(row[-1] + "\n")
                pathB_w.write(row[-1] + "\n")


def __main__():
    if (len(sys.argv) != 3):
        print("CLI Format: python make_sqr_mat.py <MatrixOutputFile.txt> <int N>")
        return
    
    # Ripped if statement fromhttps://stackoverflow.com/questions/5899497/how-can-i-check-the-extension-of-a-file
    if not (sys.argv[1].endswith('.txt')):
        print("Output Matrix output files must be text files (.txt)")
        return

    try:
        # assume if N is passed that it is a power of 2
        N = int(sys.argv[2])
    except:
        print("Size of Matrix output files must be a number and divisible by 2")


    mat1 = fillMatrix(N)
    writeOutMatFile(sys.argv[1], mat1)



if (__name__ == "__main__"):
    __main__()