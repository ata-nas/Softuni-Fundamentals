from abc import ABC, abstractmethod


class ForceCommand(ABC):
    @abstractmethod
    def parse_command(self) -> None:
        pass

    @abstractmethod
    def push_registration(self, registry) -> None:
        pass


class PipeCommand(ForceCommand):
    def __init__(self, command) -> None:
        self.command = command

    def parse_command(self) -> tuple[str, str]:
        side: str
        user: str

        side, user = self.command.split(sep=' | ')
        return (user, side)

    def push_registration(self, commands, registry: dict) -> None:
        side: str
        user: str
        user_registered: bool

        user, side = commands

        user_registered = False
        for key in registry.keys():
            if user in registry[key]:
                user_registered = True

        if not user_registered:
            if side not in registry.keys():
                registry[side] = [user]
            else:
                registry[side].append(user)


class ArrowCommand(ForceCommand):
    def __init__(self, command) -> None:
        self.command = command

    def parse_command(self):
        side: str
        user: str

        user, side = self.command.split(sep=' -> ')
        return (user, side)

    def push_registration(self, commands, registry: dict) -> None:
        side: str
        user: str
        user_registered: bool

        user, side = commands

        user_registered = False
        for key in registry.keys():
            if user in registry[key]:
                user_registered = True

        if user_registered:
            for key, value in registry.items():
                for item in value:
                    if item == user:
                        registry[key].remove(item)

            registry[side].append(user)
        else:
            if side not in registry.keys():
                registry[side] = [user]
            else:
                registry[side].append(user)

        print(f"{user} joins the {side} side!")


class ForceBook:
    registry: dict[str, list[str]] = {}

    def print_registry(self) -> None:
        for key, value in self.registry.items():
            if self.registry[key]:
                print(f'Side: {key}, Members: {len(value)}')
            for item in value:
                print(f'! {item}')


def parse_user_input(user_inp) -> PipeCommand | ArrowCommand:
    if '|' in user_inp:
        return PipeCommand(user_inp)
    elif '->' in user_inp:
        return ArrowCommand(user_inp)
    else:
        raise ValueError(
            'Improper command entry! '
            'Command needs to include a separator "|" for PipeCommand() or "->" for ArrowCommand().')


def main() -> None:
    forcebook: ForceBook = ForceBook()

    registry: dict[str, list[str]] = forcebook.registry

    while True:
        user_input: str = input()

        if user_input == 'Lumpawaroo':
            break

        action: PipeCommand | ArrowCommand = parse_user_input(user_input)

        commands: tuple[str, str] = action.parse_command()

        action.push_registration(commands, registry)

    forcebook.print_registry()


if __name__ == '__main__':
    main()

# 90-100
