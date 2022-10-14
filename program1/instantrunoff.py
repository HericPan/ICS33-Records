import goody
from collections import defaultdict
from tkinter.constants import CURRENT

def read_voter_preferences(file : open):
    record = dict()
    for line in file:
        a_vote = line.rstrip().split(';')
        record[a_vote[0]] = [x for x in a_vote[1:]]
    return record
        


def dict_as_str(d : {None:None}, key : callable=None, reverse : bool=False) -> str:
    string = ""
    for a_vote in sorted(d, key = key, reverse = reverse):
        string += ("  "+a_vote + " -> " + str(d[a_vote]) + "\n")
    return string

def evaluate_ballot(vp : {str:[str]}, cie : {str}) -> {str:int}:
    record = defaultdict(int)
    for voter in vp:
        for candid in vp[voter]:
            if candid in cie:
                record[candid] += 1
                break
    return record


def remaining_candidates(vd : {str:int}) -> {str}:
    min_votes = vd.pop(min(vd, key=(lambda key: vd[key])))
    while min_votes in vd.values(): vd.pop(min(vd, key=(lambda key: vd[key])))
    return set(vd.keys())


def run_election(vp_file : open) -> {str}:
    all_votes = read_voter_preferences(vp_file)
    print("Preferences Dump: voter -> list of all candidates by decreasing preference")
    print(dict_as_str(all_votes), end="")
    ballot_counter = 0
    for x in all_votes.values():    # get the list of all candidates
        candidates = set(x)
        break   # only get once
    while len(candidates) != 0 and len(candidates) != 1:
        ballot_counter += 1
        current_ballot = evaluate_ballot(all_votes, candidates)
        print(f"Vote count on ballot #{ballot_counter}: candidates still in election: sorted alphabetically")
        print(dict_as_str(current_ballot, key = (lambda x: x)))
        print(f"Vote count on ballot #{ballot_counter}: candidates still in election: sorted numerically")
        print(dict_as_str(current_ballot, key = (lambda x: current_ballot[x]), reverse = True))
        candidates = remaining_candidates(current_ballot)
    return candidates
  
  
  
    
if __name__ == '__main__':
    # Write script here
    infile = goody.safe_open("Provide the file name storing voter preferences", 'r', 'Illegal file name')
    print()
    print("Winner determined: "+ str(run_election((open('votepref1.txt')))))
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc2.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
