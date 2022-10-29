class Bookshelf:
    def __init__(self, books: list):
        self.shelf = books

    def add_book(self, book):
        if book not in self.shelf:
            self.shelf.insert(0, book)

    def take_book(self, book):
        if book in self.shelf:
            self.shelf.remove(book)

    def swap_books(self, first_book, second_book):
        if first_book in self.shelf and second_book in self.shelf:
            index_first_book = self.shelf.index(first_book)
            index_second_book = self.shelf.index(second_book)
            self.shelf[index_first_book], self.shelf[index_second_book] = self.shelf[index_second_book], self.shelf[index_first_book]

    def insert_book(self, book):
        if book not in self.shelf:
            self.shelf.append(book)

    def check_book(self, index):
        if index in range(len(self.shelf)):
            return self.shelf[index]


books_list = [item for item in input().split(sep="&")]

bookshelf = Bookshelf(books_list)

while True:
    user_input = input()
    if user_input == "Done":
        break
    command = user_input.split(sep=" | ")
    if command[0] == "Add Book":
        bookshelf.add_book(command[1])
    elif command[0] == "Take Book":
        bookshelf.take_book(command[1])
    elif command[0] == "Swap Books":
        bookshelf.swap_books(command[1], command[2])
    elif command[0] == "Insert Book":
        bookshelf.insert_book(command[1])
    elif command[0] == "Check Book":
        if int(command[1]) in range(len(bookshelf.shelf)):
            print(bookshelf.check_book(int(command[1])))

result_shelf = ", ".join(bookshelf.shelf)

print(f"{result_shelf}")
