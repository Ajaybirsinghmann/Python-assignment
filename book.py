from book import Book  # Importing the Book class from book.py

# Function to search for books by title or author
def search_book(books, search_value):
    found_books = [b for b in books if search_value.lower() in b.get_title().lower() or search_value.lower() in b.get_author().lower()]
    return found_books

# Function to borrow a book by ISBN
def borrow_book(books, isbn):
    for b in books:
        if b.get_isbn() == isbn:
            if b.borrow_it():
                print(f"'{b.get_title()}' with ISBN {b.get_isbn()} successfully borrowed.")
            else:
                print(f"'{b.get_title()}' with ISBN {b.get_isbn()} is not currently available.")
            return
    print("No book found with that ISBN.")

# Function to return a borrowed book by ISBN
def return_book(books, isbn):
    for b in books:
        if b.get_isbn() == isbn:
            if b.return_it():
                print(f"'{b.get_title()}' with ISBN {b.get_isbn()} successfully returned.")
            else:
                print(f"'{b.get_title()}' with ISBN {b.get_isbn()} is not currently borrowed.")
            return
    print("No book found with that ISBN.")

# Librarian menu for managing the library
def librarian_menu(books):
    while True:
        print("\nReader's Guild Library - Librarian Menu")
        print("=======================================")
        print("1. Search for books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Add a book")
        print("5. Remove a book")
        print("6. Print catalog")
        print("0. Exit the system")
        choice = input("Enter your selection: ")

        if choice == '1':
            print("\n-- Search for books --")
            search_value = input("Enter search value: ")
            found_books = search_book(books, search_value)
            if found_books:
                print("ISBN           Title                     Author                    Genre                Availability")
                print("-------------- ------------------------- ------------------------- -------------------- ------------")
                for book in found_books:
                    print(book)
            else:
                print("No matching books found.")
        elif choice == '2':
            print("\n-- Borrow a book --")
            isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
            borrow_book(books, isbn)
        elif choice == '3':
            print("\n-- Return a book --")
            isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
            return_book(books, isbn)
        elif choice == '4':
            print("\n-- Add a book --")
            isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
            title = input("Enter title: ")
            author = input("Enter author name: ")
            genre = input("Enter genre: ")
            new_book = Book(isbn, title, author, genre, True)  # Assuming added books are always available
            books.append(new_book)
            print(f"'{title}' with ISBN {isbn} successfully added.")
        elif choice == '5':
            print("\n-- Remove a book --")
            isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
            for i, b in enumerate(books):
                if b.get_isbn() == isbn:
                    del books[i]
                    print(f"'{b.get_title()}' with ISBN {b.get_isbn()} successfully removed.")
                    break
            else:
                print("No book found with that ISBN.")
        elif choice == '6':
            print("\n-- Print book catalog --")
            print("ISBN           Title                     Author                    Genre                Availability")
            print("-------------- ------------------------- ------------------------- -------------------- ------------")
            for book in books:
                print(book)
        elif choice == '0':
            print("\n-- Exit the system --")
            print("Good Bye!")
            break
        else:
            print("Invalid option")

# Main function to start the library system
def main():
    print("Starting the system ...")
    while True:
        filename = input("Enter book catalog filename: ")
        books = Book.load_from_csv(filename)
        if books:
            print("Book catalog has been loaded.")
            break
    
    librarian_menu(books)

if __name__ == "__main__":
    main()
