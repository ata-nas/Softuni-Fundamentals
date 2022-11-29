COMMAND_REGISTER = 'register'
COMMAND_UNREGISTER = 'unregister'


class ParkingLot:
    def __init__(self) -> None:
        self.registry = {}

    def register(self, user, plate):
        if self.registry.get(user) == plate:
            print(f"ERROR: already registered with plate number {plate}")
        else:
            self.registry[user] = plate
            print(f"{user} registered {plate} successfully")

    def unregister(self, user):
        if user in self.registry.keys():
            self.registry.pop(user)
            print(f"{user} unregistered successfully")
        else:
            print(f"ERROR: user {user} not found")

    def registry_check(self):
        pass

    def print_lot_status(self):
        [print(f"{key} => {value}") for key, value in self.registry.items()]


def main():
    parking_lot = ParkingLot()

    user_input_number_of_commands = int(input())

    for _ in range(user_input_number_of_commands):
        user_input_command = input().split(sep=' ')

        if user_input_command[0] == COMMAND_REGISTER:
            username, license_plate = user_input_command[1], user_input_command[2]
            parking_lot.register(username, license_plate)
        elif user_input_command[0] == COMMAND_UNREGISTER:
            username = user_input_command[1]
            parking_lot.unregister(username)

    parking_lot.print_lot_status()


if __name__ == '__main__':
    main()
