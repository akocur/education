with open('salary.txt', 'r') as f_month, open('salary_year.txt', 'w') as f_year:
    for line in f_month:
        print(int(line.strip()) * 12, file=f_year)
