definitions = {}

for item in input().split(sep=' | '):
    a = item.split(sep=': ')
    key = a[0]
    value = a[1]
    if key not in definitions.keys():
        definitions[key] = [value]
    else:
        definitions[key].append(value)

test_words = [word for word in input().split(sep=' | ')]

command = input()

if command == 'Test':
    for word in test_words:
        if word in definitions.keys():
            print(f'{word}:')
            for item in definitions[word]:
                print(f'-{item}')
elif command == 'Hand Over':
    for word in definitions.keys():
        print(word, end=' ')
        