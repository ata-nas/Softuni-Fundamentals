class AtomShell:
    def __init__(self, electrons: int):
        self.electrons = electrons
        self.shells = self.create_shells()

    def create_shells(self):
        result_list = []
        curr_shell = 0
        electrons_left = self.electrons
        while electrons_left:
            max_electrons = 2 * (curr_shell + 1) ** 2
            if electrons_left >= max_electrons:
                result_list.insert(curr_shell, max_electrons)
                electrons_left -= max_electrons
            else:
                result_list.insert(curr_shell, electrons_left)
                electrons_left = 0
            curr_shell += 1
        return result_list


user_input = int(input())

atom = AtomShell(user_input)

print(atom.shells)
