import goody
from collections import defaultdict


def read_fa(file : open) -> {str:{str:str}}:
    record = dict()
    for line in file:
        a_rule = line.rstrip().split(";") 
        if a_rule: record[a_rule[0]] = dict(zip([a_rule[i] for i in range(1, len(a_rule), 2)], [a_rule[i] for i in range(2, len(a_rule), 2)]))
    return record


def fa_as_str(fa : {str:{str:str}}) -> str:
    string = ""
    for state in sorted(fa):
        string += ("  "+state+" transitions: " + str(sorted(fa[state].items()))+ "\n")
    return string

def process(fa : {str:{str:str}}, state : str, inputs : [str]) -> [None]:
    current_state = state
    input_list = [current_state]
    while len(inputs) != 0:
        current_input = inputs.pop(0)
        if current_input not in fa[current_state]:
            input_list.append(tuple([current_input, None]))
            break
        current_state = fa[current_state][current_input]
        input_list.append(tuple([current_input, current_state]))
    return input_list


def interpret(fa_result : [None]) -> str: 
    string = f"Start state = {fa_result[0]}\n"
    input_list = fa_result[1:]
    for i in range(len(input_list)):
        if input_list[i][1] != None:
            string += ("  Input = " + str(input_list[i][0]) + "; new state = " + str(input_list[i][1] +"\n"))
        else:
            string += ("  Input = " + str(input_list[i][0]) + "; illegal input: simulation terminated\n")
    string += (f"Stop state = {input_list[len(input_list) - 1][1]}\n")
    return string



if __name__ == '__main__':
    # Write script here
    rule = goody.safe_open("Provide the file name storing a Finite Automaton", 'r', 'Illegal file name')
    print()
    fa = read_fa(rule)
    print("Finite Automaton Dump: state: list of transitions\n"+fa_as_str(fa))
    inputs = rule = goody.safe_open("Provide the file name storing a sequence of start-states and their subsequent inputs", 'r', 'Illegal file name')
    print()
    for line in inputs:
        line = line.rstrip().split(";")
        print("Tracing FA (from a start-state)\n"+interpret(process(fa, line[0], line[1:])))
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc3.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
