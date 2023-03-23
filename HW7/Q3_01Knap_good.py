import sys

def knapsack(weight, items):
    # create 1D array to store subproblem solutions
    dp_matrix = [0] * (weight + 1)

    # fill in the array in a bottom-up manner
    for i in range(len(items)):
        item_w, item_v = items[i]
        # iterate over the possible weight limits in reverse order
        for j in range(weight, item_w - 1, -1):
            # update the current value of dp_matrix[j] by comparing it
            # against the value you could get by including the item
            dp_matrix[j] = max(dp_matrix[j], dp_matrix[j - item_w] + item_v)

    # Return the last value (optimal knapsack value)
    return dp_matrix[-1]

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
