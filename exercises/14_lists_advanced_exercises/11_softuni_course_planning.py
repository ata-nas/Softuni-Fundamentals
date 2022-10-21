COMMAND_ADD = 'Add'
COMMAND_INSERT = 'Insert'
COMMAND_REMOVE = 'Remove'
COMMAND_SWAP = 'Swap'
COMMAND_EXERCISE = 'Exercise'
COMMAND_END = "course start"


class Course:
    def __init__(self, schedule: list):
        self.schedule = schedule

    def course_add(self, curr_command: list):
        lesson_title = curr_command[1]

        if lesson_title not in self.schedule:
            self.schedule.append(lesson_title)

    def course_insert(self, curr_command: list):
        lesson_title = curr_command[1]
        index = int(curr_command[2])

        if lesson_title not in self.schedule:
            self.schedule.insert(index, lesson_title)

    def course_remove(self, curr_command: list):
        lesson_title = curr_command[1]

        if lesson_title in self.schedule:
            self.schedule.remove(lesson_title)
        if f'{lesson_title}-Exercise' in self.schedule:
            self.schedule.remove(f'{lesson_title}-Exercise')

    def course_swap(self, curr_command: list):
        first_title = curr_command[1]
        second_title = curr_command[2]

        if first_title in self.schedule and second_title in self.schedule:
            first_title_position = self.schedule.index(first_title)
            second_title_position = self.schedule.index(second_title)

            self.schedule[first_title_position], self.schedule[second_title_position] = \
                self.schedule[second_title_position], self.schedule[first_title_position]

            if f"{first_title}-Exercise" in self.schedule:
                self.schedule.insert(second_title_position + 1, self.schedule[first_title_position + 1])
                self.schedule.pop(first_title_position + 2)

            if f"{second_title}-Exercise" in self.schedule:
                self.schedule.insert(first_title_position + 1, self.schedule[second_title_position + 1])
                self.schedule.pop(second_title_position + 2)

    def course_exercise(self, curr_command: list):
        lesson_title = curr_command[1]
        if lesson_title in self.schedule:
            if f'{lesson_title}-Exercise' not in self.schedule:
                self.schedule.insert(self.schedule.index(lesson_title) + 1, f'{lesson_title}-Exercise')
        else:
            self.schedule.append(lesson_title)
            self.schedule.append(f'{lesson_title}-Exercise')


user_input_schedule = input().split(sep=', ')

course = Course(user_input_schedule)

while True:
    user_command = input()

    if user_command == COMMAND_END:
        break

    command = user_command.split(sep=":")

    if command[0] == COMMAND_ADD:
        course.course_add(command)
    elif command[0] == COMMAND_INSERT:
        course.course_insert(command)
    elif command[0] == COMMAND_REMOVE:
        course.course_remove(command)
    elif command[0] == COMMAND_SWAP:
        course.course_swap(command)
    elif command[0] == COMMAND_EXERCISE:
        course.course_exercise(command)

for index, item in enumerate(course.schedule, 1):
    print(f"{index}.{item}")
