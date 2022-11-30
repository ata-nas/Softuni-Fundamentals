COMMAND_CONTEST_END = 'end of contests'
COMMAND_SUBMISSIONS_END = 'end of submissions'


class Passwords:
    def __init__(self) -> None:
        self.dict = {}

    def add_password(self, contest, password):
        if contest not in self.dict.keys():
            self.dict[contest] = password

    def generate_passwords_list(self):
        while True:
            user_input = input()

            if user_input == COMMAND_CONTEST_END:
                break

            contest, curr_pass = user_input.split(sep=':')

            self.add_password(contest, curr_pass)

        return self.dict


class Contest:
    def __init__(self) -> None:
        self.entries = {}
        self.prime_participant = None

    def conduct(self):
        valid_passwords = Passwords().generate_passwords_list()

        self.entries = ContestApplication().generate_applications(valid_passwords)

        self.prime_participant = self.best_participant()

    def best_participant(self):
        result = None

        max_score = 0

        for contestant in self.entries.keys():
            curr_max_score = 0

            for contest, score in self.entries[contestant].items():
                curr_max_score += score

            if curr_max_score >= max_score:
                max_score = curr_max_score
                result = [contestant, int(max_score)]

        return tuple(result)

    def view(self):
        print_dict = dict(sorted(self.entries.items()))

        print(
            f'Best candidate is {self.prime_participant[0]} with total {self.prime_participant[1]} points.')

        print('Ranking:')

        for key, value in print_dict.items():
            print(f'{key}')

            value_sorted_print_dict = dict(
                sorted(value.items(), key=lambda item: item[1], reverse=True))

            for contest, score in value_sorted_print_dict.items():
                print(f'#  {contest} -> {score}')


class ContestApplication:
    def __init__(self) -> None:
        self.applications = {}

    @staticmethod
    def is_valid(curr_contest, curr_pass, passwords):
        return curr_pass == passwords.get(curr_contest)

    def render_application(self):
        pass

    def generate_applications(self, valid_pass):
        while True:
            user_input = input()

            if user_input == COMMAND_SUBMISSIONS_END:
                break

            contest, password, username, points = user_input.split(sep='=>')

            if self.is_valid(contest, password, valid_pass):
                if username not in self.applications.keys():
                    curr_value = {contest: int(points)}
                    self.applications[username] = curr_value
                else:
                    if contest not in self.applications[username].keys():
                        self.applications[username][contest] = int(points)
                    else:
                        for key, value in self.applications[username].items():
                            if key == contest:
                                if int(points) > value:
                                    self.applications[username][contest] = int(
                                        points)

        return self.applications


def main():
    contest = Contest()

    contest.conduct()

    contest.view()


if __name__ == '__main__':
    main()
