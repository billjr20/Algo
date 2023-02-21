import Algo_HW6
import sys

def MakeRecommendations(adj_list, output_file):
    with open(output_file, "w") as f_out:
        for start_vertex in adj_list:
            max_two_path = (len(adj_list)+1, 0)
            for end_vertex, count in adj_list[start_vertex]:
                if count > max_two_path[1]:
                    max_two_path = (end_vertex, count)
                elif count == max_two_path[1] and end_vertex < max_two_path[0]:
                    max_two_path = (end_vertex, count)
            
            if (max_two_path[1] == 0):
                f_out.write("0\n")
            else:
                f_out.write(str(max_two_path[0]) + "\n")




def __main__():
    if (len(sys.argv) != 3):
        print("CLI Format: python Recommendations.py <MatrixFile1.txt> <OutputFile.txt>")
        return
    
    # Ripped if statement from https://stackoverflow.com/questions/5899497/how-can-i-check-the-extension-of-a-file
    if not (sys.argv[1].endswith('.txt') or sys.argv[2].endswith('.txt')):
        print("Please make sure Matrix input parse files are text files (.txt)")
        return

    
    # open command line arguments
    raw_adj_list = Algo_HW6.openFile(sys.argv[1])

    paths_adj_list = Algo_HW6.countTwoPaths(raw_adj_list)

    MakeRecommendations(paths_adj_list, sys.argv[2])





if (__name__ == "__main__"):
    __main__()