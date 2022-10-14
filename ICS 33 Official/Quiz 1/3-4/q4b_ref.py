def by_skill(db1 : {str: {str: int}}) -> [(int, [(str, [str])])]:
    record = dict()
    for name in db1:
        for skill,level in db1[name].items():
            if level not in record:
                record[level] = dict()
            if skill not in record[level]:
                record[level][skill] = list()
            record[level][skill].append(name)
        
    return sorted([(l,\
                    sorted([(s,sorted(record[l][s])) for s in record[l]])) for l in record], \
                    reverse=True)
        
db = {'Adam': {'Cleaning': 4, 'Tutoring': 2, 'Baking': 1},'Betty': {'Gardening': 2, 'Tutoring': 1, 'Cleaning': 3}, 'Charles': {'Plumbing': 2, 'Cleaning': 5}, 'Diane': {'Laundry': 2, 'Cleaning': 4, 'Gardening': 3}}
dtc = [(5, [('Cleaning', ['Charles'])]),(4, [('Cleaning', ['Adam', 'Diane'])]),(3, [('Cleaning', ['Betty']), ('Gardening', ['Diane'])]),(2, [('Gardening', ['Betty']), ('Laundry', ['Diane']), ('Plumbing', ['Charles']), ('Tutoring', ['Adam'])]),(1, [('Baking', ['Adam']), ('Tutoring', ['Betty'])])]

print(by_skill(db) == dtc)