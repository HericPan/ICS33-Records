def by_job(database) -> dict:
    records = dict()
    for name, skills in database.items():
        for skill_names, level in skills.items():
            if skill_names not in records.keys():
                records[skill_names] = dict()
            records[skill_names][name] = level
            
    return records

if __name__ == "__main__":
    db = {'Adam': {'Cleaning': 4, 'Tutoring': 2, 'Baking': 1},'Betty': {'Gardening': 2, 'Tutoring': 1, 'Cleaning': 3}, 'Charles': {'Plumbing': 2, 'Cleaning': 5}, 'Diane': {'Laundry': 2, 'Cleaning': 4, 'Gardening': 3}}
    print(by_job(db))