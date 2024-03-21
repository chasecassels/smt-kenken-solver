import sys
import re

def parse_smt_output(smt_output):
    #Empty Dict to hold our variables
    assignments = {}
    for line in smt_output:
        #REGEX to match each line
        match = re.search(r'\(V(\d+)\s+(\d+)\)', line)
        if match:
            var_index = int(match.group(1))
            value = int(match.group(2))
            #Grab value of each line after match
            assignments[var_index] = value
    return assignments
#Formats the dictionary into a string
def format_solution(assignments):

    sorted_values = [assignments[i] for i in sorted(assignments)]
    return ''.join(map(str, sorted_values))

def main(file_path):
    with open(file_path, 'r') as file:
        smt_output = file.readlines()
    assignments = parse_smt_output(smt_output)
    solution_string = format_solution(assignments)
    #Print statement for formating our solution.txt
    print(f"{solution_string}")


if __name__ == "__main__":    
    file_path = sys.argv[1]
    main(file_path)
