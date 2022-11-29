CRITERIA_THRESHOLD = 4.5


class Academy:
    def __init__(self) -> None:
        self.students_list = {}

    def add_students(self, students: list):
        for index in range(0, len(students), 2):
            student = students[index]
            grade = students[index + 1]

            if student not in self.students_list.keys():
                self.students_list[student] = [float(grade)]
            else:
                self.students_list[student].append(float(grade))

    def pop_below_criteria(self, criteria=CRITERIA_THRESHOLD):
        for key, value in self.students_list.items():
            if sum(value) / len(value) < criteria:
                self.students_list[key] = None

        self.students_list = {key: (sum(value) / (len(value)))
                              for key, value in self.students_list.items() if value is not None}

    def print_students(self):
        [print(f'{key} -> {value:.2f}')
         for key, value in self.students_list.items() if value is not None]


def main():
    academy = Academy()

    rows = int(input())

    student_grade_pairs = [input() if i % 2 == 0 else float(input())
                           for i in range(rows * 2)]

    academy.add_students(student_grade_pairs)
    academy.pop_below_criteria()
    academy.print_students()


if __name__ == '__main__':
    main()
