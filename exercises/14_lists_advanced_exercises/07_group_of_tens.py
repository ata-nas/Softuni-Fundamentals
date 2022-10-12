class GroupsOfTens:
    def __init__(self, numbers):
        self.numbers = [int(number) for number in numbers.split(sep=", ")]
        self.groups = self.create_groups()

    def create_groups(self):
        result = []
        obj_list = list(self.numbers)
        boundary = 10
        while obj_list:
            result_list = []
            for item in self.numbers:
                if item <= boundary:
                    result_list.append(item)
                    obj_list.remove(item)
            curr_res = f"Group of {boundary}'s: {result_list}"
            result.append(curr_res)
            boundary += 10
            self.numbers = list(obj_list)
        self.numbers = None
        return result


user_input = input()

user_group = GroupsOfTens(user_input)

for res in user_group.groups:
    print(res)
