from abc import ABC, abstractmethod

COMMAND_END: str = 'exam finished'


class Entry(ABC):
    @abstractmethod
    def process_entry(self) -> None:
        pass


class NormalEntry(Entry):
    def __init__(self, command) -> None:
        self.command = command

    def process_entry(self, command, registry) -> None:
        participant: str
        language: str
        score: int

        reg_participants: dict[str, int] = registry.participants
        reg_submissions: dict[str, int] = registry.submissions

        participant, language, score = self.command[0], self.command[1], self.command[2]

        if participant in reg_participants:
            if int(score) > reg_participants[participant]:
                reg_participants[participant] = int(score)
        else:
            reg_participants[participant] = int(score)

        reg_submissions[language] = reg_submissions.get(language, 0) + 1


class BanEntry(Entry):
    def __init__(self, command) -> None:
        self.command = command

    def process_entry(self, command, registry) -> None:
        reg_participants: dict[str, int] = registry.participants

        participant: str = self.command

        if participant in reg_participants:
            del reg_participants[participant]


class Exam:
    def __init__(self) -> None:
        self.participants: dict[str, int] = {}
        self.submissions: dict[str, int] = {}

    @staticmethod
    def parse_entry(input_entry) -> BanEntry | NormalEntry:
        participant: str
        language: str
        score: str

        if input_entry.endswith('-banned'):
            participant:str = input_entry.split(sep='-')[0]
            return BanEntry(participant)

        participant, language, score = input_entry.split(sep='-')
        return NormalEntry((participant, language, score))

    def view(self) -> None:
        print('Results:')

        for key, value in self.participants.items():
            print(f'{key} | {value}')

        print('Submissions:')

        for key, value in self.submissions.items():
            print(f'{key} - {value}')


def take_user_input() -> list[str]:
    result: list[str] = []

    while True:
        user_input: str = input()

        if user_input == COMMAND_END:
            break

        result.append(user_input)

    return result


def main() -> None:
    exam: Exam = Exam()
    participant_dict: dict[str, int] = exam.participants
    submissions_dict: dict[str, int] = exam.submissions

    entries_list: list[str] = take_user_input()

    for entry in entries_list:
        curr_entry: BanEntry | NormalEntry = exam.parse_entry(entry)

        curr_entry.process_entry(curr_entry, exam)

    exam.view()


if __name__ == '__main__':
    main()
