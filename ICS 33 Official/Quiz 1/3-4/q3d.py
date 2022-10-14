def who(database, job, min_skill_level) -> list: # retusn a list of 2-tuples
    """
    
    The who function:
        takes in database, job(str), minimum skill level(int) as arguments
        returns a list of 2-tuples: persons and their skill level
        sorted by decreasing skill level (most skilled first)
    
    """
    
# Non-one-statement version:
#     records = list()
#     for name, skills in database.items():
#         for skill_name, level in skills.items():
#             if level >= min_skill_level and skill_name == job:
#                 records.append((name, level))
#                 
#     return sorted(records, key=(lambda t: (-t[1], t[0])))
#     
    return sorted([(name, level) for name, skills in database.items() for skill_name, level in skills.items() if level >= min_skill_level and skill_name == job], key=(lambda t: (-t[1], t[0])))

if __name__ == "__main__":
    db = {'Adam': {'Cleaning': 4, 'Tutoring': 2, 'Baking': 1},'Betty': {'Gardening': 2, 'Tutoring': 1, 'Cleaning': 3}, 'Charles': {'Plumbing': 2, 'Cleaning': 5}, 'Diane': {'Laundry': 2, 'Cleaning': 4, 'Gardening': 3}}
    print(who(db, 'Cleaning', 4))