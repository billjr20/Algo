import sys

def knapsack(weight, items, left, right):
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
                dp_mat[j] = with_item
                if i > (right+left)//2-1:
                    K[j] = K[j - item_w]
    
    return K[-1]


def knapsack_idea(weight, items, left, right):
    print(weight, items)
    if right - left == 1:
        return [items[left]] if items[left][0] == weight else None
    k = knapsack(weight, items, left, right)
    mid = (left + right) // 2
    S_L = knapsack_idea(k, items, left, mid)
    S_R = knapsack_idea(weight-k, items, mid, right)
    if S_L and S_R:
        return S_L + S_R
    elif S_L:
        return S_L
    elif S_R:
        return S_R


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


def main():
    if (len(sys.argv) != 2):
        print("CLI Format: python Q1_Knap_w_Trace.py <Knapsack_Data.txt>")
        return

    # Ripped if statement from https://stackoverflow.com/questions/5899497/how-can-i-check-the-extension-of-a-file
    if not (sys.argv[1].endswith('.txt')):
        print("Please make sure knapsack data files are passed as text files (.txt)")
        return

    weight, items = openFile(sys.argv[1])
    out_items = knapsack_idea(weight, items, 0, len(items))
    print(out_items)

main()
