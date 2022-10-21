class Pokemon:
    def __init__(self, pokemons_list: list):
        self.pokemons_list = pokemons_list
        self.pokemons_captured = list()

    def capture_pokemon(self, index: int):
        curr_captured_pokemon_value = 0

        if index < 0:
            curr_captured_pokemon_value = self.pokemons_list.pop(0)
            self.pokemons_captured.append(curr_captured_pokemon_value)
            self.pokemons_list.insert(0, self.pokemons_list[-1])
        elif index > len(self.pokemons_list) - 1:
            curr_captured_pokemon_value = self.pokemons_list.pop()
            self.pokemons_captured.append(curr_captured_pokemon_value)
            self.pokemons_list.insert(len(self.pokemons_list), self.pokemons_list[0])
        else:
            curr_captured_pokemon_value = self.pokemons_list.pop(index)
            self.pokemons_captured.append(curr_captured_pokemon_value)

        for index, item in enumerate(self.pokemons_list):
            if item <= curr_captured_pokemon_value:
                self.pokemons_list[index] += curr_captured_pokemon_value
            elif item > curr_captured_pokemon_value:
                self.pokemons_list[index] -= curr_captured_pokemon_value


user_input_list = [int(i) for i in input().split(sep=" ")]

pokemons_value = Pokemon(user_input_list)

while pokemons_value.pokemons_list:
    curr_index = int(input())
    pokemons_value.capture_pokemon(curr_index)

print(sum(pokemons_value.pokemons_captured))
