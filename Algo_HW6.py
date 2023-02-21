import sys


def processVertex(vertex, adj_list):

    two_paths_map = {}
    for inner_edge in adj_list[vertex]:
        for outer_edge in adj_list[inner_edge]:
            if outer_edge not in two_paths_map:
                two_paths_map[outer_edge] = 1
            else:
                two_paths_map[outer_edge] += 1
    
    two_path_res = []
    for dest_vertex, num_times in two_paths_map.items():
        two_path_res.append((dest_vertex, num_times))

    return two_path_res 


def countTwoPaths(input_adj_list):
    output_adj_list = {} #  personID (int) -> [(twoPathPerson, numTimes)]

    for key in input_adj_list:
        output_adj_list[key] = processVertex(key, input_adj_list)


    return output_adj_list


# Opens and parses input matrices from text files
def openFile(matFile):
    matrix = []
    adj_list = {} # personID (int) -> [connected nonzero IDs]
    curr_row_ID = 0
    with open(matFile, 'r') as f_read:
        for line in f_read:
            line = line.replace(" \n", "").replace("\n", "")
            line_split = line.split(" ")
            
            curr_row = []
            for otherPersonIdx, row_num in enumerate(line_split):
                row_num = int(row_num)
                if (row_num == 1):
                    curr_row.append(otherPersonIdx+1)
            adj_list[curr_row_ID+1] = curr_row
            curr_row_ID+=1
    return adj_list


def __main__():
    if (len(sys.argv) != 2):
        print("CLI Format: python Algo_HW6.py <MatrixFile1.txt>")
        return
    
    # Ripped if statement from https://stackoverflow.com/questions/5899497/how-can-i-check-the-extension-of-a-file
    if not (sys.argv[1].endswith('.txt')):
        print("Please make sure Matrix input parse files are text files (.txt)")
        return

    # open command line arguments
    input_adj_list = openFile(sys.argv[1])
    print(input_adj_list)

    output_adj_list = countTwoPaths(input_adj_list)
    print(output_adj_list)





if (__name__ == "__main__"):
    __main__()