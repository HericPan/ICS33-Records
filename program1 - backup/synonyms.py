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

# sample output: {'i': {'went': 1, 'gym': 1, 'this': 1, 'morning': 2, 'later': 1, 'rested': 1, 'was': 1, 'tired': 1}, 'went': {'i': 1, 'gym': 1, 'this': 1, 'morning': 1}, 'gym': {'i': 1, 'went': 1, 'this': 1, 'morning': 1}, 'this': {'i': 1, 'went': 1, 'gym': 1, 'morning': 1}, 'morning': {'i': 2, 'went': 1, 'gym': 1, 'this': 1, 'later': 1, 'rested': 1}, 'later': {'morning': 1, 'i': 1, 'rested': 1}, 'rested': {'later': 1, 'morning': 1, 'i': 1}, 'was': {'i': 1, 'tired': 1}, 'tired': {'i': 1, 'was': 1}}
def build_semantic_dictionary(training_files : [open], ignore_file : open) -> {str:{str:int}}:
    ignore_words = {word.rstrip() for word in ignore_file}
    semantic_dict = dict()
    nfile = training_files[0]
    for s in sentence_at_a_time(nfile, ignore_words):
        for w in s:
            if w not in semantic_dict:
                semantic_dict[w] = defaultdict(int)
            for w_context in s:
                if w_context != w:
                    semantic_dict[w][w_context] += 1
    
    return semantic_dict

def dict_as_str(semantic : {str:{str:int}}) -> str:
    pass

       
def cosine_metric(context1 : {str:int}, context2 : {str:int}) -> float:
    pass 


def most_similar(word : str, choices : [str], semantic : {str:{str:int}}, metric : callable) -> str:
    pass 


def similarity_test(test_file : open, semantic : {str:{str:int}}, metric : callable) -> str:
    pass 




# Script

if __name__ == '__main__':
    # Write script here
    print(build_semantic_dictionary([open('simple1.txt'), open("simple2.txt")],open('ignore_words.txt')))
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc5.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
