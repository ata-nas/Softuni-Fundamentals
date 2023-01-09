def parse_user_input(user_inp):
    return user_inp.split(sep=' -> ')


def update_dicts(cont_dict, part_dict, parse_func):
    username, contest, points = parse_func

    curr_contestant = {username: int(points)}

    if contest not in cont_dict.keys():
        cont_dict[contest] = curr_contestant
    else:
        for key, value in cont_dict.items():
            if key == contest:
                if username in value.keys() and int(points) > cont_dict[contest][username]:
                    cont_dict[contest][username] = int(points)
                elif username not in value.keys():
                    cont_dict[contest][username] = int(points)

    part_dict[username] = part_dict.get(username, 0) + int(points)


def print_dicts(cont_dict, part_dict):
    for key, value in cont_dict.items():
        print(f'{key}: {len(value)} participants')

        iteration = 1
        for user, points in dict(sorted(value.items(), key=lambda x: x[1], reverse=True)).items():
            print(f'{iteration}. {user} <::> {points}')
            iteration += 1

    print('Individual standings:')

    iteration = 1
    for user, points in dict(sorted(part_dict.items(), key=lambda x: x[1], reverse=True)).items():
            print(f'{iteration}: {user} -> {points}')

def main():
    contest_dict = {}
    participant_dict = {}

    while True:
        user_input = input()

        if user_input == 'no more time':
            break

        update_dicts(contest_dict, participant_dict,
                     parse_user_input(user_input))

    print_dicts(contest_dict, participant_dict)


if __name__ == '__main__':
    main()
