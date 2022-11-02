def add_student(student_name: str, student_id: int, student_course: str, student_dict: dict) -> dict:
    stud_tuple = tuple([student_name, student_id])
    if student_course not in student_dict.keys():
        student_dict[student_course] = [stud_tuple]
    else:
        student_dict[student_course].append(stud_tuple)
    return student_dict


def get_query(student_dict: dict, student_course: str) -> list:
    query = student_dict.get(student_course)
    return [f"{name} - {id}" for name, id in query]


def main():
    students_dict = {}

    while True:
        user_input = input()

        if ":" not in user_input:
            command = user_input.replace("_", " ")
            people = get_query(students_dict, command)
            for item in people:
                print(item)
            break

        command = user_input.split(sep=":")

        std_name = command[0]
        std_id = command[1]
        std_course = command[2]

        students_dict = add_student(
            std_name, std_id, std_course, students_dict)


if __name__ == '__main__':
    main()
