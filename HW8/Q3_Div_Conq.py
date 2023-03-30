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


"""""
Implementation of the divide and conquer pseduo code given in problem 3
The algorithm makes use of the opt_k_val function that was developed
for problem 2
"""""
def div_conq_knapsack(weight, items, left, right):
    # base case:
    # if there is one item and that item is the weight argument,
    # the item must be in the overall knapsack
    if right - left == 1:
        return [right] if items[left][0] == weight else []
    
    # Compute optimal k capacity
    k = opt_k_val(weight, items, left, right)

    # partition the items array using a two pointers strategy
    mid = (left + right) // 2

    # recursive divide and conquer 
    S_L = div_conq_knapsack(k, items, left, mid)
    S_R = div_conq_knapsack(weight-k, items, mid, right)

    # win hearts and minds (maybe I don't remember)
    # combine divide and conquer result
    return S_L + S_R



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

# format output in accordance with how problem 1 outlines
def outputFilePrint(optimal_knapsack_val, trace, output_filename):
    with open(output_filename, "w") as f_out:
        f_out.write(f"V {optimal_knapsack_val}\n")
        f_out.write(f"i {len(trace)}\n")
        for i in range(len(trace)):
            # f_out.write(f"{trace_queue[i][0]}\n")
            f_out.write(f"{trace[i]}\n")

def main():
    if (len(sys.argv) != 3):
        print("CLI Format: python Q3_Div_Conq.py <Knapsack_Data.txt> <Tracing_Output_File.txt")
        return

    # Ripped if statement from https://stackoverflow.com/questions/5899497/how-can-i-check-the-extension-of-a-file
    if not (sys.argv[1].endswith('.txt') and sys.argv[2].endswith('.txt')):
        print("Please make sure knapsack data files are passed as text files (.txt)")
        return

    # open and parse starting knapsack data
    weight, items = openFile(sys.argv[1])

    # call divide and conquer knapsack algorithm
    out_items = div_conq_knapsack(weight, items, 0, len(items))
    
    # using items in the knapsack computed above generate the max
    # value of the knapsack O(n), items, bounded so not time dominant
    # very much repeated work but much easier than passing something
    # more back from div_conq_knapsack
    max_val = 0
    for knap_item in out_items:
        max_val += items[knap_item-1][1]

    # print to output file
    outputFilePrint(max_val, out_items, sys.argv[2])

if __name__ == "__main__":
    main()
