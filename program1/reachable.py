import goody
import prompt
from collections import defaultdict
from fileinput import filename


def read_graph(file : open) -> {str:{str}}:
    record = defaultdict(set)
    for line in file:
        node = line.rstrip().split(';')
        record[node[0]].add(node[1])
    return record
        


def graph_as_str(graph : {str:{str}}) -> str:
    string = ""
    for fr,to in sorted([(start, sorted(graph[start])) for start in graph]):
        string += "  " + fr + " -> " + str(to) + '\n'
    return string
        
def reachable(graph : {str:{str}}, start : str, trace : bool = False) -> {str}:
    reached_set = set()
    exploring_list = [start]
    while len(exploring_list) != 0:
        if trace == True: print(f"  reached set    = {reached_set}\n  exploring list = {exploring_list}")
        current_node = exploring_list.pop(0)
        reached_set.add(current_node)
        if trace == True: print(f"  now remove node a from the exploring list, then add it to the reached set\n  after adding all nodes reachable directly from {current_node} but not already in reached, exploring = {[x for x in exploring_list+list(graph.get(current_node, []))]}\n")
        if graph.get(current_node, None) != None: exploring_list += list( x for x in graph[current_node] if x not in reached_set )
            
    return reached_set




if __name__ == '__main__':
    # Write script here
    file_name = goody.safe_open('Provide the file name storing a graph','r','Illegal file name')
    print("\nGraph Dump: source node -> list of all destination nodes")
    stored_graph = read_graph(file_name)
    print(graph_as_str(stored_graph), end = "")
    while True:
        print()
        node = prompt.for_value("Provide a node for starting (or type quit)", is_legal=(lambda x: True if x in stored_graph or x == 'quit' else False),
                                 error_message="Illegal: not a source node\n  Please enter a legal String\n")
        if node == "quit": break
        trace_bool = prompt.for_bool("Trace (True or False) the algorithm", default=True)
        print("Starting from node a all the reachable nodes: " + str(reachable(stored_graph, node, trace=trace_bool)))
    
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc1.txt"
    driver.default_show_traceback = True
    driver.default_show_exception = True
    driver.default_show_exception_message = True
    driver.driver()
