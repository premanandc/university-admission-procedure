# write your code here
MONTHS = 12
with open('salary.txt') as in_file:
    with open('salary_year.txt', 'w') as out_file:
        for line in in_file.readlines():
            monthly_salary = int(line)
            yearly_salary = monthly_salary * MONTHS
            out_file.write(f'{yearly_salary}\n')
