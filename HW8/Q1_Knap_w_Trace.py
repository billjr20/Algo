import sys
import collections

# Class-like Knapsack Algorithm implementation that 
# runs in O(nW) and requires O(nW) space for a 2D table 
def knapsack(weight, items):
    # create a 2D array to store knapsack table of subproblem solutions
    dp_mat = [[0 for _ in range(weight + 1)] for _ in range(len(items) + 1)]

    # fill in the array in a bottom-up manner
    for i in range(1, len(items) + 1):
        item_w, item_v = items[i - 1]
        for j in range(1, weight + 1):
            # exclude too heavy item
            if item_w > j:
                dp_mat[i][j] = dp_mat[i - 1][j]
            
            # choose whether to include the item or not based on which yields a higher value
            else:
                dp_mat[i][j] = max(dp_mat[i - 1][j], dp_mat[i - 1][j - item_w] + item_v)


    # basic queue data structure for python
    # appendleft (prepending) operation is O(1), https://wiki.python.org/moin/TimeComplexity
    trace_queue = collections.deque()
    res = dp_mat[i][j]
    for i in range(len(items), 0, -1):
        # knapsack if full
        if res <= 0:
            break
        # either the result comes from the
        # top (K[i-1][w]) or from (val[i-1]
        # + K[i-1] [w-wt[i-1]]) as in Knapsack
        # table. If it comes from the latter
        # one/ it means the item is included.
        if res == dp_mat[i - 1][weight]:
            continue
        
        else:
            # This item is included
            trace_queue.appendleft((i, items[i-1][0], items[i-1][1]))
             
            # Since this weight is included
            # its value is deducted
            weight = weight - items[i-1][0]
            res = res - items[i-1][1]
    # return bottom right corner (optimal knapsack value)
    return dp_mat[-1][-1], trace_queue

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
            f_out.write(f"{trace[i][0]}\n")


# driver code
def main():
    if (len(sys.argv) != 3):
        print("CLI Format: python Q1_Knap_w_Trace.py <Knapsack_Data.txt> <Knapsack_OutputFile>")
        return

    # Ripped if statement from https://stackoverflow.com/questions/5899497/how-can-i-check-the-extension-of-a-file
    if not (sys.argv[1].endswith('.txt') or sys.argv[2].endswith('.txt')):
        print("Please make sure knapsack data files are passed as text files (.txt)")
        return

    # open and read data from input file
    weight, items = openFile(sys.argv[1])

    # compute O(nW) time and space knapsack and compute the item trace
    optimal_knapsack_val, trace_queue = knapsack(weight, items)

    # print the item trace
    outputFilePrint(optimal_knapsack_val, trace_queue, sys.argv[2])


if __name__ == "__main__":
    main()
