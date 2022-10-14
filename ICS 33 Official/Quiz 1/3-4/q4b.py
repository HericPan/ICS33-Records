def by_skill(database) -> list:
    # sorted by decreasing skill level!
    records = list()
    
    # 1. For the top-level 2-tuple - (n, [(), ()])
    for chosen_level in range(5, 0, -1):
        
        records.append((chosen_level, []))
        
        # 2. For the lower-level 2-tuple - [(), (), ()]
        for name, skills in sorted(database.items(), key=(lambda t:t[0])): # sorted by name
            
            currentSlot = records[5 - chosen_level]
#             skillList = currentSlot[1]
            
            # 3. Inside the tuple (skill_name, [])
            for skill_name, level in sorted(skills.items(), key=(lambda t:t[0])): # sorted by skill_name
                if chosen_level == level:
                    if skill_name not in [t[0] for t in currentSlot[1]]:
                        currentSlot[1].append((skill_name, [name]))
                    else:
                        for index,skill_roster in enumerate(currentSlot[1]):
                            currentSlot[1][index][1].append(name)
                            
    # adding completed, now we are going to sort it.
    # 1. Sorted by decreasing skill level
    records.sort(key=(lambda t: -t[0]))
    
    # 2. Sorted on the skill alphabetically
    for slot in records:
        slot[1].sort(key=(lambda t : t[0]))
#         slot[1] = sorted(slot[1], key = (lambda t: t[0]), reverse = True)
        for each_skill in slot[1]:
            each_skill[1].sort()
                    
                
        
    return records


if __name__ == "__main__":
    db = {'Adam': {'Cleaning': 4, 'Tutoring': 2, 'Baking': 1},'Betty': {'Gardening': 2, 'Tutoring': 1, 'Cleaning': 3}, 'Charles': {'Plumbing': 2, 'Cleaning': 5}, 'Diane': {'Laundry': 2, 'Cleaning': 4, 'Gardening': 3}}
    print(by_skill(db) == )