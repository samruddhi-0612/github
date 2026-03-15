class Book:
    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title
        self.issued = False


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_id, title):
        self.books.append(Book(book_id, title))
        print("Book added successfully")

    def issue_book(self, book_id):
        for b in self.books:
            if b.book_id == book_id and not b.issued:
                b.issued = True
                print("Book issued")
                return
        print("Book not available")

    def return_book(self, book_id):
        for b in self.books:
            if b.book_id == book_id and b.issued:
                b.issued = False
                print("Book returned")
                return
        print("Invalid book ID")

    def display_books(self):
        if not self.books:
            print("No books in library")
        for b in self.books:
            print("ID:", b.book_id, "Title:", b.title, "Issued:", b.issued)


library = Library()

while True:
    print("\n1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Display Books")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")
        library.add_book(book_id, title)

    elif choice == 2:
        book_id = int(input("Enter Book ID: "))
        library.issue_book(book_id)

    elif choice == 3:
        book_id = int(input("Enter Book ID: "))
        library.return_book(book_id)

    elif choice == 4:
        library.display_books()

    elif choice == 5:
        break