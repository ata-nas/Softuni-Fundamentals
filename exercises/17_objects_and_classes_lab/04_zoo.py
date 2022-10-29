class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        result = ""

        if species == "mammal":
            animals_names = ", ".join(self.mammals)
            result = f"Mammals in {self.zoo_name}: {animals_names}\n" \
                     f"Total animals: {Zoo.__animals}"
        elif species == "fish":
            animals_names = ", ".join(self.fishes)
            result = f"Fishes in {self.zoo_name}: {animals_names}\n" \
                     f"Total animals: {Zoo.__animals}"
        elif species == "bird":
            animals_names = ", ".join(self.birds)
            result = f"Birds in {self.zoo_name}: {animals_names}\n" \
                     f"Total animals: {Zoo.__animals}"

        return result


user_input_name_of_zoo = input()
user_input_items_to_add = int(input())

z = Zoo(user_input_name_of_zoo)

for index in range(user_input_items_to_add):
    user_input = input().split(sep=" ")

    curr_species = user_input[0]
    curr_name = user_input[1]

    z.add_animal(curr_species, curr_name)

species_to_get_info = input()

print(z.get_info(species_to_get_info))
