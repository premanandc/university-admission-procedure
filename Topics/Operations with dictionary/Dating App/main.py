def select_dates(potential_dates):
    names = [x['name'] for x in potential_dates if x['age'] > 30 and 'art' in x['hobbies'] and x['city'] == 'Berlin']
    return ", ".join(names)
