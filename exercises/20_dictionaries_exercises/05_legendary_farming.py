SHADOWMOURNE_ELEMENT = 'shards'
SHADOWMOURNE_REQUIREMENTS = 250

VALANYR_ELEMENT = 'fragments'
VALANYR_REQUIREMENTS = 250

DRAGONWRATH_ELEMENT = 'motes'
DRAGONWRATH_REQUIREMENTS = 250

LEGENDARIES_REQUIREMENTS = {
        SHADOWMOURNE_ELEMENT: SHADOWMOURNE_REQUIREMENTS,
        VALANYR_ELEMENT: VALANYR_REQUIREMENTS,
        DRAGONWRATH_ELEMENT: DRAGONWRATH_REQUIREMENTS,
    }

WINNERS = {
    SHADOWMOURNE_ELEMENT: 'Shadowmourne',
    VALANYR_ELEMENT: 'Valanyr',
    DRAGONWRATH_ELEMENT: 'Dragonwrath',
}

def generate_element_quantity_lists():  # OK 
    user_input = input().split(sep=' ')
    elements = []
    quantities = []

    for item in user_input:
        try:
            quantity = int(item)
            quantities.append(quantity)
        except:
            element = item
            elements.append(element.lower())

    return zip(elements, quantities)


def main():
    legendary_tracker = {key: 0 for key in LEGENDARIES_REQUIREMENTS.keys()}

    winner = None
    while winner is None:
        for item in generate_element_quantity_lists():
            key = item[0]
            value = item[1]
            legendary_tracker[key] = legendary_tracker.get(key, 0) + value

            for key, value in LEGENDARIES_REQUIREMENTS.items():
                if value <= legendary_tracker.get(key):  # type: ignore
                    winner = WINNERS.get(key)
                    legendary_tracker[key] = legendary_tracker[key] - value
                    break

            if winner:
                break


    print(f"{winner} obtained!")

    key_materials = [f'{key}: {value}' for key, value in legendary_tracker.items() if key in LEGENDARIES_REQUIREMENTS.keys()]
    junk_materials = [f'{key}: {value}' for key, value in legendary_tracker.items() if key not in LEGENDARIES_REQUIREMENTS.keys()]

    print(*key_materials, sep='\n')
    print(*junk_materials, sep='\n')

if __name__ == '__main__':
    main()
