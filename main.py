import json
import os

DATA_FILE = "library.json"

class Library:
    def __init__(self):
        self.books = []
        self.load_data()

    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as file:
                self.books = json.load(file)
        else:
            self.books = []

    def save_data(self):
        with open(DATA_FILE, "w") as file:
            json.dump(self.books, file, indent=4)

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author: ")

        book = {
            "title": title,
            "author": author,
            "available": True
        }

        self.books.append(book)
        self.save_data()
        print("Book added successfully!")

    def view_books(self):
        if not self.books:
            print("No books in library.")
            return

        print("\nLibrary Books:")
        for i, book in enumerate(self.books, start=1):
            status = "Available" if book["available"] else "Borrowed"
            print(f"{i}. {book['title']} by {book['author']} - {status}")

    def borrow_book(self):
        self.view_books()
        if not self.books:
            return

        try:
            choice = int(input("Enter book number to borrow: "))
            book = self.books[choice - 1]

            if book["available"]:
                book["available"] = False
                self.save_data()
                print("Book borrowed successfully!")
            else:
                print("Book is already borrowed.")
        except (ValueError, IndexError):
            print("Invalid selection.")

    def return_book(self):
        self.view_books()
        if not self.books:
            return

        try:
            choice = int(input("Enter book number to return: "))
            book = self.books[choice - 1]

            if not book["available"]:
                book["available"] = True
                self.save_data()
                print("Book returned successfully!")
            else:
                print("Book was not borrowed.")
        except (ValueError, IndexError):
            print("Invalid selection.")


def main():
    library = Library()

    while True:
        print("\n==== Library Menu ====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.view_books()
        elif choice == "3":
            library.borrow_book()
        elif choice == "4":
            library.return_book()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()