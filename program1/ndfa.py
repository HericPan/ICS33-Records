import goody
from collections import defaultdict

# sample output: {'end': {}, 'start': {'1': {'start'}, '0': {'start', 'near'}}, 'near': {'1': {'end'}}}
def read_ndfa(file : open) -> {str:{str:{str}}}:
    record = defaultdict(dict)
    for line in file:
        a_rule = line.rstrip().split(";") # sample line: [start;0;start;1;start;0;near]
        record[a_rule[0]] = dict()
        for num,state in list(zip(a_rule[1::2], a_rule[2::2])):
            record[a_rule[0]].setdefault(num,set())
            record[a_rule[0]][num].add(state)
    return record


def ndfa_as_str(ndfa : {str:{str:{str}}}) -> str: # sample output: "  end transitions: []\n  near transitions: [('1', ['end'])]\n  start transitions: [('0', ['near', 'start']), ('1', ['start'])]\n"
    string = ""
    for state in sorted(ndfa):
        string += ("  "+state+" transitions: " + str(sorted([(x,sorted(ndfa[state][x])) for x in sorted(ndfa[state])]))+ "\n")
    return string

# sample ndfa: {'end': {}, 'start': {'1': {'start'}, '0': {'start', 'near'}}, 'near': {'1': {'end'}}}
# sample output: ['start', ('1', {'start'}), ('0', {'start', 'near'}), ('1', {'end', 'start'}), ('1', {'start'}), ('0', {'start', 'near'}), ('1', {'end', 'start'})]
def process(ndfa : {str:{str:{str}}}, state : str, inputs : [str]) -> [None]:
    current_states = [state]
    input_list = [state]
    index = 1
    while len(inputs) != 0 and len(current_states) != 0:
        current_input = inputs.pop(0)
        input_list.append((current_input, set()))
        for possible_s in current_states:
            if current_input in ndfa[possible_s]:
                for x in ndfa[possible_s][current_input]:
                    input_list[index][1].add(x)
        current_states = sorted(input_list[index][1])
        index += 1
    return input_list


# sample input: ['start', ('1', {'start'}), ('0', {'start', 'near'}), ('1', {'end', 'start'}), ('1', {'start'}), ('0', {'start', 'near'}), ('1', {'end', 'start'})]
def interpret(result : [None]) -> str:
    string = f"Start state = {result[0]}\n"
    input_list = result[1:]
    for i in range(len(input_list)):
        string += ("  Input = " + str(input_list[i][0]) + "; new possible states = " + str(sorted(input_list[i][1])) +"\n")
    string += (f"Stop state(s) = {sorted(input_list[len(input_list) - 1][1])}\n")
    return string





if __name__ == '__main__':
    # Write script here
    rule = goody.safe_open("Provide the file name storing a Non-Deterministic Finite Automaton", 'r', 'Illegal file name')
    print()
    ndfa = read_ndfa(rule)
    print("Non-Deterministic Finite Automaton Dump: state: list of transitions\n"+ndfa_as_str(ndfa))
    inputs = rule = goody.safe_open("Provide the file name storing a sequence of start-states and their subsequent inputs", 'r', 'Illegal file name')
    print()
    for line in inputs:
        line = line.rstrip().split(";")
        print("Tracing NDFA (from a start-state)\n"+interpret(process(ndfa, line[0], line[1:])))
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc4.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
