def select_dates(potential_dates, age=30, hobby='art', city='Berlin'):
    find_people = [row['name'] for row in potential_dates
                   if row['age'] > age and hobby in row['hobbies'] and row['city'] == city]
    return ', '.join(find_people)
