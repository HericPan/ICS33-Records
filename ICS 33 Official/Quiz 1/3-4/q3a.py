def jobs(database: dict, min_skill_level) -> set: 
    """
    
    Function jobs returns a set of job names(str):
        all job names appearing in the database whose
        associated skill level is equal or larger than 
        the minimum skill level.
    
    We can assume the second argument is an int value.
    
    For example, if db is the database above calling 
        jobs(db,3) would return {'Cleaning', 'Gardening'}.

    """
# This is the older version
#     record = set()
#     for person in database.values():
#         for jName, skillLv in person:
#             if skillLv >= min_skill_level:
#                 record.add(jName)
#     return record

# This is one-statement version.
    return set(jName for person in database.values() for (jName, skillLv) in person.items() if skillLv >= min_skill_level)
if __name__ == "__main__":
    db = {'Adam': {'Cleaning': 4, 'Tutoring': 2, 'Baking': 1},'Betty': {'Gardening': 2, 'Tutoring': 1, 'Cleaning': 3}, 'Charles': {'Plumbing': 2, 'Cleaning': 5}, 'Diane': {'Laundry': 2, 'Cleaning': 4, 'Gardening': 3}}
    print(jobs(db, 3))