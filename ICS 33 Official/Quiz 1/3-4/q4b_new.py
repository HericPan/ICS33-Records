# from collections import defaultdict
def by_skill(db1: {str : { str : int } }) -> [ (int, [(str, [str]) ] ) ]:
    records = list
    outerdict = dict()
    for chosen_level in range(5, 0, -1):
        outerdict[chosen_level] = dict()
        innerdict = outerdict[chosen_level]
        
        # now iterate through db to get each skill_name and add qualified people into the list
        for name,skill_set in db1.items():
            for skill_name, skill_level in skill_set.items():
                if skill_level == chosen_level:
                    if skill_name not in innerdict:
                        innerdict[skill_name] = []
                    innerdict[skill_name].append(name)
    record = sorted([(level, sorted([(skill_name, sorted(name)) for skill_name,name in skills.items()], key=(lambda t:t[0]))) for level, skills in outerdict.items()], key=(lambda t: -t[0]))
    return record
                
        
db = {'Adam': {'Cleaning': 4, 'Tutoring': 2, 'Baking': 1},'Betty': {'Gardening': 2, 'Tutoring': 1, 'Cleaning': 3}, 'Charles': {'Plumbing': 2, 'Cleaning': 5}, 'Diane': {'Laundry': 2, 'Cleaning': 4, 'Gardening': 3}}
dtc = [(5, [('Cleaning', ['Charles'])]),(4, [('Cleaning', ['Adam', 'Diane'])]),(3, [('Cleaning', ['Betty']), ('Gardening', ['Diane'])]),(2, [('Gardening', ['Betty']), ('Laundry', ['Diane']), ('Plumbing', ['Charles']), ('Tutoring', ['Adam'])]),(1, [('Baking', ['Adam']), ('Tutoring', ['Betty'])])]

print(by_skill(db) == dtc)