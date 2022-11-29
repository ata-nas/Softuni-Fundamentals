COMMAND_END = "end"


class Course:
    def __init__(self) -> None:
        self.courses = {}

    def add(self, course, student):
        if course not in self.courses.keys():
            self.courses[course] = [student]
        else:
            self.courses[course].append(student)

    def print_courses(self):
        for key, value in self.courses.items():
            print(f"{key}: {len(value)}")
            for name in value:
                print(f"-- {name}")


def main():
    course = Course()

    while True:
        user_input = input()

        if user_input == COMMAND_END:
            break

        curr_course, curr_name = user_input.split(sep=' : ')

        course.add(curr_course, curr_name)

    course.print_courses()


if __name__ == '__main__':
    main()
