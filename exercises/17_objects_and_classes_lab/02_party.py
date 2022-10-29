class Person:
    def __init__(self, name):
        self.name = name


class Party:
    people = []


p = Party()

while True:
    command = input()
    if command == "End":
        break
    person = Person(command)
    p.people.append(person.name)

people_going = ", ".join(p.people)
total_going = len(p.people)

print(f"Going: {people_going}\n"
      f"Total: {total_going}")
