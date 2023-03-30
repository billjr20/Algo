import sys

"""""
Compute the idea capacity k of the knapsack filled by the
items {i,.., floor(right/2)}
The core idea of this algorithm is track the column (weight) index
that the final knapsack value passes through so that the knapsack 
problem can be independently split into two knapsack problem
that can solved with a divide and conquer algorithm 
"""""
def opt_k_val(weight, items, left, right):
    # preallocate matrices to hold matrix value
    # and row index recording
    dp_mat = [0] * (weight + 1)
    K = [i for i in range(weight + 1)]

    # fill in the array in a bottom-up manner
    for i in range(left, right):
        item_w, item_v = items[i]
        # iterate over the possible weight limits in reverse order
        for j in range(weight, item_w - 1, -1):
            # update the current value of dp_matrix[j] by comparing it
            # against the value you could get by including the item
            without_item = dp_mat[j]
            with_item = dp_mat[j - item_w] + item_v
            if with_item > without_item:
                # update matrix
                dp_mat[j] = with_item
                # determining the middle row column index
                # that the final knapsack value passes through
                if i > (right+left)//2-1:
                    K[j] = K[j - item_w]
    
    return K[-1]


# All file parsing pieces are constant time operations as the 
# size of a given line of input is fixed, so reading N items 
# from a file would be O(n) and not time dominant
def openFile(txt_file):
    # weight is the size of the knapsack
    # items are the possible items to place into said knapsack
    weight, items = 0, []

    with open(txt_file, "r") as f_in:
        iters = 0
        # O(N) in the worst case as each line contains a item
        # Each line is formatted with as "w # v #"
        for line in f_in:
            if iters == 0:
                # line splitting is O(1) as the input line is fixed in size
                weight = int(line.split(" ")[1])
            elif iters == 1:
                # preallocate N-length items array
                items = [(0,0)] * int(line.split(" ")[1])
            else:
                # line splitting is O(1) as the input line is fixed in size
                line = line.split(" ")
                item_w, item_v = int(line[1]), int(line[3])
                items[iters-2] = (item_w, item_v)
            iters += 1
    return weight, items


# driver code
def main():
    if (len(sys.argv) != 2):
        print("CLI Format: python Q2_Opt_K.py <Knapsack_Data.txt>")
        return

    # Ripped if statement from https://stackoverflow.com/questions/5899497/how-can-i-check-the-extension-of-a-file
    if not (sys.argv[1].endswith('.txt')):
        print("Please make sure knapsack data files are passed as text files (.txt)")
        return

    # open and parse knapsack start data file
    weight, items = openFile(sys.argv[1])

    # compute optimal capacity k for the full knapsack
    first_opt_k = opt_k_val(weight, items, 0, len(items))
    print(first_opt_k)


if __name__ == "__main__":
    main()


    
