from collections import defaultdict  # Use or ignore

def function_cycler(*fs : callable) -> callable:
    if len(fs) == 0: raise TypeError("The function should take at least 1 argument.")
    fs = list(fs)
    
    times_called = [0]
    def internal_func(n):
        times_called[0] += 1
        current_index = times_called[0] % len(fs) - 1
        
        internal_func.times_called = times_called[0]
        return fs[current_index](n)
    internal_func.times_called = times_called[0]
    return internal_func


def jobs(db1 : {str:{str:int}}, min_skill_level : int) -> {str}:
    return set(jName for person in db1.values() for (jName, skillLv) in person.items() if skillLv >= min_skill_level)
    



def rank(db1 : {str:{str:int}}) -> [str]:
    return [name for name, skills in sorted(db1.items(), key = (lambda t : (-sum(t[1].values()) / len(t[1]) , t[0] ) ) )]
    # for full credit, use a single return statement  



def popular(db1 : {str:{str:int}}) -> [str]:
    return [i for i, j in sorted([(name, [skill_name for name,skills in db1.items() for skill_name in skills.keys()].count(name)) for name in jobs(db1,0)], key=(lambda t: (-t[1], t[0])))] # for full credit, use a single return statement  



def who(db1 : {str:{(str,int)}}, job : str, min_skill_level : int) -> [(str,int)]:
    return sorted([(name, level) for name, skills in db1.items() for skill_name, level in skills.items() if level >= min_skill_level and skill_name == job], key=(lambda t: (-t[1], t[0])))
    # for full credit, use a single return statement  



def by_job(db1 : {str:{str:int}}) -> {str:{str:int}}:
    records = dict()
    for name, skills in db1.items():
        for skill_names, level in skills.items():
            if skill_names not in records.keys():
                records[skill_names] = dict()
            records[skill_names][name] = level
            
    return records



def by_skill(db1 : {str:{str:int}}) -> [int,[str,[str]]]:
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
        if len(innerdict) == 0:
            outerdict.pop(chosen_level)
    record = sorted([(level, sorted([(skill_name, sorted(name)) for skill_name,name in skills.items()], key=(lambda t:t[0]))) for level, skills in outerdict.items()], key=(lambda t: -t[0]))
    return record





if __name__ == '__main__':
    from goody import irange
    
    print('\nTesting function_cycler')
    try:
        cycler0 = function_cycler()
        print("Incorrect: Did not raise required exception for no-argument function call")
    except TypeError:
        print("Correct: rasised required exception for no-argument function call")
    cycler1 = function_cycler( (lambda x : x), (lambda x : x**2))
    print('Cycler 1:',[cycler1(x) for x in irange(1,10)],'... times called: ',cycler1.times_called)
    cycler2 = function_cycler( (lambda x : x+1), (lambda x : 2*x), (lambda x : x**2))
    print('Cycler 2:',[cycler2(x) for x in irange(1,10)],'... times called: ',cycler2.times_called)
 
    print('Cycler 1 again:',[cycler1(x) for x in irange(10,15)],'... times called: ',cycler1.times_called)
    print('Cycler 2 again:',[cycler2(x) for x in irange(10,20)],'... times called: ',cycler2.times_called)
    
    
    # Note: the keys in this dicts are not specified in alphabetical order
    db1 = {
          'Diane':   {'Laundry': 2,   'Cleaning': 4, 'Gardening': 3},
          'Betty':   {'Gardening': 2, 'Tutoring': 1, 'Cleaning': 3},
          'Charles': {'Plumbing': 2,  'Cleaning': 5},
          'Adam':    {'Cleaning': 4,  'Tutoring': 2, 'Baking': 1}
          }

    db2 = {
           'Adam': {'Laundry': 2, 'Driving': 2, 'Tutoring': 2, 'Reading': 1, 'Gardening': 1},
           'Emil': {'Errands': 4, 'Driving': 1, 'Baking': 3},
           'Chad': {'Repairing': 2, 'Reading': 2, 'Errands': 4, 'Baking': 2},
           'Ivan': {'Gardening': 5, 'Errands': 5, 'Reading': 4, 'Cleaning': 3},
           'Gene': {'Driving': 1, 'Laundry': 1, 'Baking': 2, 'Gardening': 2, 'Repairing': 2, 'Errands': 5},
           'Dana': {'Driving': 2}, 
           'Hope': {'Driving': 5, 'Reading': 3, 'Errands': 2, 'Shopping': 2, 'Gardening': 1, 'Laundry': 2},
           'Bree': {'Baking': 2, 'Errands': 5},
           'Faye': {'Tutoring': 2, 'Reading': 5, 'Repairing': 5, 'Baking': 4}
           }

    print('\nTesting jobs')
    print('jobs(db1,0):',jobs(db1,0))
    print('jobs(db1,3):',jobs(db1,3))
    print('jobs(db2,0):',jobs(db2,0))
    print('jobs(db2,5):',jobs(db2,5))


    print('\nTesting rank')
    print ('rank(db1):',rank(db1))
    print ('rank(db2):',rank(db2))


    print('\nTesting popular')
    print ('popular(db1):',popular(db1))
    print ('popular(db2):',popular(db2))


    print('\nTesting who')
    print("who(db1,'Cleaning',4):", who(db1,'Cleaning',4))
    print("who(db1,'Gardening',0):", who(db1,'Gardening',0))
    print("who(db1,'Tutoring',3):", who(db1,'Tutoring',3))
    print("who(db1,'Gambling',0):", who(db1,'Gambling',0))
    print("who(db2,'Baking',0):", who(db2,'Baking',0))
    print("who(db2,'Cleaning',1):", who(db2,'Cleaning',1))
    print("who(db2,'Driving',2):", who(db2,'Driving',2))
    print("who(db2,'Errands',3):", who(db2,'Errands',3))
    print("who(db2,'Gardening',4):", who(db2,'Gardening',4))
    print("who(db2,'Laundry',5):", who(db2,'Laundry',5))

    print('\nTesting by_job')
    print ('by_job(db1):',by_job(db1))
    print ('by_job(db2):',by_job(db2))


    print('\nTesting by_skill')
    print ('by_skill(db1):',by_skill(db1))
    print ('by_skill(db2):',by_skill(db2))



    print('\ndriver testing with batch_self_check:')
    import driver
    driver.default_file_name = 'bscq1F20.txt'
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
