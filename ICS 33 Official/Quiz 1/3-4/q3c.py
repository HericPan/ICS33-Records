from q3a import jobs

def popular(database) -> list:
    """
    
    The popular function:
        takes a database as an argument,
        returns a list of job names(str), (SORTED DESCENDINGLY)
        sorted descending by how often they appear in the database,
            and increasing alphabetical order by job name.
        
    May need to call jobs function
    
    """
#     allRecords = list()
#     for name, skills in database.items():
#         for skill_name in skills.keys():
#             allRecords.append(skill_name)
#     
#     records = [(name, allRecords.count(name)) for name in jobs(db,0)]
# #     return records
# #     return [i for i,j in sorted(record, key=(lambda t: (-t[1], t[0])))]
#     return [i for i,j in sorted(records, key=(lambda t: (-t[1], t[0])))]

    return [i for i, j in sorted([(name, [skill_name for name,skills in database.items() for skill_name in skills.keys()].count(name)) for name in jobs(database,0)], key=(lambda t: (-t[1], t[0])))]

if __name__ == "__main__":
    db = {'Adam': {'Cleaning': 4, 'Tutoring': 2, 'Baking': 1},'Betty': {'Gardening': 2, 'Tutoring': 1, 'Cleaning': 3}, 'Charles': {'Plumbing': 2, 'Cleaning': 5}, 'Diane': {'Laundry': 2, 'Cleaning': 4, 'Gardening': 3}}
    print(popular(db))