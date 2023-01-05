# write your code here
ENGINEERING = 'engineering'
CHEMISTRY = 'chemistry'
BIOTECH = 'biotech'
PHYSICS = 'physics'
MATH = 'mathematics'
subjects = {sub: [] for sub in sorted([MATH, PHYSICS, BIOTECH, CHEMISTRY, ENGINEERING])}
max_applicants = int(input().strip())


def sorter(subject):
    return lambda student: (-student[subject], student['first_name'], student['last_name'])


def student_parser(line):
    first_name, last_name, physics, chemistry, math, cs, special, first_priority, second_priority, third_priority = \
        line.split()
    return dict({'first_name': first_name,
                 'last_name': last_name,
                 PHYSICS: max(round((float(physics) + float(math)) / 2, 1), float(special)),
                 CHEMISTRY: max(float(chemistry), float(special)),
                 MATH: max(float(math), float(special)),
                 ENGINEERING: max(round((float(cs) + float(math)) / 2, 1), float(special)),
                 BIOTECH: max(round((float(chemistry) + float(physics)) / 2, 1), float(special)),
                 'subjects': [first_priority.lower(), second_priority.lower(), third_priority.lower()],
                 'enrolled': False})


def students_for(subject, students):
    return sorted([student for student in students if subject in student['subjects']], key=sorter(subject))


def enroll_students_for_priority(subject, priority, students):
    for student in students:
        current_subject = student['subjects'][priority]
        if current_subject == subject and not student['enrolled'] and len(subjects[current_subject]) < max_applicants:
            subjects[current_subject].append(student)
            student['enrolled'] = True


def enroll_students():
    students = [student_parser(line) for line in open('applicants.txt')]
    for priority in range(3):
        for subject in subjects:
            students_for_subject = students_for(subject, students)
            enroll_students_for_priority(subject, priority, students_for_subject)


def as_string(student, subject):
    return f"{student['first_name']} {student['last_name']} {student[subject]}"


def print_report():
    for subject, students in subjects.items():
        print(subject.capitalize())
        print(*[as_string(student, subject) for student in sorted(students, key=sorter(subject))], sep='\n', end='\n')
        print()


def write_report():
    for subject, students in subjects.items():
        with open(f'{subject}.txt', 'w') as file:
            file.writelines([f'{as_string(student, subject)}\n' for student in sorted(students, key=sorter(subject))])


enroll_students()
print_report()
write_report()
