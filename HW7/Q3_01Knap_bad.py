import sys

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

    # return bottom right corner (optimal knapsack value)
    return dp_mat[-1][-1]

def openFile(txt_file):
    # weight is the size of the knapsack
    # items are the possible items to place into said knapsack
    weight, items = 0, []

    with open(txt_file, "r") as f_in:
        iters = 0
        for line in f_in:
            if iters == 0:
                weight = int(line.split(" ")[1])
            elif iters == 1:
                items = [(0,0)] * int(line.split(" ")[1])

            else:
                line = line.split(" ")
                item_w, item_v = int(line[1]), int(line[3])
                items[iters-2] = (item_w, item_v)
            iters += 1
    return weight, items


def main():
    if (len(sys.argv) != 2):
        print("CLI Format: python Q3_01Knap_good.py <Knapsack_Data.txt>")
        return

    # Ripped if statement from https://stackoverflow.com/questions/5899497/how-can-i-check-the-extension-of-a-file
    if not (sys.argv[1].endswith('.txt')):
        print("Please make sure knapsack data files are passed as text files (.txt)")
        return

    weight, items = openFile(sys.argv[1])
    optimal_knapsack_val = knapsack(weight, items)
    print(optimal_knapsack_val)

if __name__ == "__main__":
    main()