COMMAND_ADD = "add"
COMMAND_INSERT = "insert"
COMMAND_LEAVE = "leave"
COMMAND_END = "End"


class Train:
    def __init__(self, wagons=0):
        self.wagons = wagons

    def curr_train(self):
        return [0 for _ in range(self.wagons)]

    @staticmethod
    def add_people(user_list: list, number_of_people: int):
        user_list[-1] += number_of_people

    @staticmethod
    def insert_people(user_list: list, index: int, people: int):
        user_list[index] += people

    @staticmethod
    def remove_people(user_list: list, index: int, people: int):
        user_list[index] -= people


def main():
    user_input_wagons = int(input())

    user_train = Train(wagons=user_input_wagons)
    user_list = user_train.curr_train()

    while True:
        user_command = input()
        if user_command == COMMAND_END:
            break

        current_command = user_command.split(sep=" ")

        if current_command[0] == COMMAND_ADD:
            user_train.add_people(user_list, int(current_command[1]))
        elif current_command[0] == COMMAND_INSERT:
            user_train.insert_people(user_list, int(current_command[1]), int(current_command[2]))
        elif current_command[0] == COMMAND_LEAVE:
            user_train.remove_people(user_list, int(current_command[1]), int(current_command[2]))

    print(user_list)


if __name__ == '__main__':
    main()
