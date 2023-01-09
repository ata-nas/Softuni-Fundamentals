import re

pattern = re.compile(r'^(?P<tag>\$[A-Z][a-z]{2,}\$+|\%[A-Z][a-z]{2,}\%+): \[(?P<fnum>\d+)\]\|\[(?P<snum>\d+)\]\|\[(?P<tnum>\d+)\]\|+$')

number_of_inputs = int(input())

for _ in range(number_of_inputs):
    message = input()

    matches = pattern.match(message)

    if matches:
        tag = matches['tag'].strip('$')
        tag = tag.strip('%')
        fchar = chr(int(matches['fnum']))
        schar = chr(int(matches['snum']))
        tchar = chr(int(matches['tnum']))
        print(f'{tag}: {fchar}{schar}{tchar}')
    else:
        print('Valid message not found!')
