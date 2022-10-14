import re                               # used in my sentence_at_a_time generator function
import math                             # use in cosine_meteric
import prompt                           # for use in script
import goody                            # for use in script
from collections import defaultdict     #  dicts and defaultdictsare == when they have the same keys/associations


# For use in build_semantic_dictionary: see problem specifications
def sentence_at_a_time(open_file : open, ignore_words : {str}) -> [str]:
    end_punct    = re.compile('[.?\!;:]')
    remove_punct = re.compile(r'(,|\'|"|\*|\(|\)|--)')

    prev   = []
    answer = []
    for l in open_file:
        l = remove_punct.sub(' ',l.lower())
        prev = prev + l.split()
        while prev:
            w = prev.pop(0)
            if end_punct.search(w):
                while end_punct.search(w):
                    w = w[0:-1]
                if w != '' and w not in ignore_words:
                    if end_punct.search(w):
                        print(w)
                    answer.append(w)
                    yield answer
                    answer = []
            else:
                if w != '' and w not in ignore_words:
                    answer.append(w)
                    
    # handle special case of last sentence missing final punctuation                
    if answer:
        yield answer


def build_semantic_dictionary(training_files : [open], ignore_file : open) -> {str:{str:int}}:
    ignore_words = {word.rstrip() for word in ignore_file}
    semantic_dict = dict()
    for nfile in training_files:
        for s in sentence_at_a_time(nfile, ignore_words):
            for w in s:
                if len(s) == 1 or s.count(w) == len(s): break
                if w not in semantic_dict: 
                    semantic_dict[w] = defaultdict(int)
                for w_context in s:
                    if w_context != w:
                        semantic_dict[w][w_context] += 1
    return semantic_dict

def dict_as_str(semantic : {str:{str:int}}) -> str:
    string = ""
    for word,context in sorted(semantic.items()):
        string += f"  context for {word} = " + ', '.join(f'{c}@{t}' for c,t in sorted(context.items())) + "\n"
    string += f'  min/max context lengths = {min(len(x) for x in semantic.values())}/{max(len(x) for x in semantic.values())}\n'
    return string

       
def cosine_metric(context1 : {str:int}, context2 : {str:int}) -> float:
    if len(context1) == 0 or len(context2) == 0: raise ZeroDivisionError
    return sum(context1[k]*context2.get(k, 0) for k in context1)/(math.sqrt(sum(context1[k1]**2 for k1 in context1)) * math.sqrt(sum(context2[k2]**2 for k2 in context2)))


def most_similar(word : str, choices : [str], semantic : {str:{str:int}}, metric : callable) -> str:
    for w in [word]+choices: 
        if w not in semantic: raise ZeroDivisionError
    max_value = 0
    for can in choices:
        i = metric(semantic[word], semantic[can])
        if i > max_value:
            syn = can
            max_value = i
    return syn
        


def similarity_test(test_file : open, semantic : {str:{str:int}}, metric : callable) -> str:
    string = ""
    total_count = 0
    win_count = 0
    for line in test_file:
        test_list = line.rstrip().split(" ")
        try:
            result = most_similar(test_list[0], test_list[1:len(test_list)-1], semantic, metric)
            if result == test_list[len(test_list)-1]:
                win_count += 1
                total_count += 1
                string += f"  Correct: \'{test_list[0]}\' is most like \'{test_list[len(test_list)-1]}\' from {test_list[1:len(test_list)-1]}\n"
            else:
                total_count += 1
                string += f"  Incorrect: \'{test_list[0]}\' is most like \'{test_list[len(test_list)-1]}\', not \'{result}\' from {test_list[1:len(test_list)-1]}\n"
        except ZeroDivisionError:
            total_count += 1
            string += f"  Metric failure: could not choose synonym for \'{test_list[0]}\' from {test_list[1:len(test_list)-1]}\n"
        
    return string + f"{win_count/total_count * 100}% correct\n"


# Script

if __name__ == '__main__':
    # Write script here
    file_list = []
    i = ""
    while i != "no-more":
        try:
            i = prompt.for_value("Provide the name of a text file for training \(or type no-more\)", default="no-more")
            file_list.append(open(i))
        except FileNotFoundError:
            if i != 'no-more': 
                print(f'  file named {i} rejected: cannot be opened')
    print()
    if file_list:
        semantic_dict = build_semantic_dictionary(file_list, {})
        if prompt.for_bool("Dump (True or False) Semantic dictionary?", default=False, error_message = 'Please enter a valid bool value.'):
            print("Semantic Dictionary")
            print(dict_as_str(semantic_dict))
        else:
            print()
        
        test_file = goody.safe_open('Enter name of problem file', 'r', 'Illegal file name', default='synonym-problems.txt')
        print(similarity_test(test_file, semantic_dict, cosine_metric))

    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc5.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
