def rank(database) -> list:
    """
    
    The rank function:
        takes an argument database
        returns a list of str (names) (SORTED! DESCENDING!)
            sorted descending by the average skill level of
            jobs each name does. people who have the same 
            average skill level must appear in increasing
            alphabetical order by name.
    
    """
#     record = dict()
#     for name, skills in database.items():
#         record[name]  = sum(skills.values()) / len(skills)
#     return record
#     return [i for i,j in sorted(record.items(), key = (lambda t : (-t[1], t[0])))]
    return [name for name, skills in sorted(database.items(), key = (lambda t : (-sum(t[1].values()) / len(t[1]) , t[0] ) ) )]

if __name__ == "__main__":
    db = {'Adam': {'Cleaning': 4, 'Tutoring': 2, 'Baking': 1},'Betty': {'Gardening': 2, 'Tutoring': 1, 'Cleaning': 3}, 'Charles': {'Plumbing': 2, 'Cleaning': 5}, 'Diane': {'Laundry': 2, 'Cleaning': 4, 'Gardening': 3}}
    print(rank(db))