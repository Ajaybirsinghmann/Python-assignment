import book  # Importing the Book class from another module

def main():
    # Create a list containing 3 books (test the constructor)
    book_list = []
    book_list.append(book.Book("978-0441172719", "Dune", "Frank Herbert", 2, True))
    book_list.append(book.Book("978-0375822742", "The City of Ember", "Jeanne DuPrau", 4, True))
    book_list.append(book.Book("978-0060513030", "Where the Sidewalk Ends", "Shel Silverstein", 9, False))

    # Test 1 
    # Get the first book in the list and borrow it
    # Then, using getters, display all information for this book
    current_book = book_list[0]
    current_book.borrow_it()
    print("*** Test 1 Output ***")
    print("ISBN: ", current_book.get_isbn())
    print("Title: ", current_book.get_title())
    print("Author: ", current_book.get_author())
    print("Genre: ", current_book.get_genre_name())
    print("Availability: ", current_book.get_availability())

    # Test 2
    # Find all books with "city" in the title
    print("\n*** Test 2 Output ***")
    search_value = "city"
    for current_book in book_list:
        if search_value.lower() in current_book.get_title().lower():
            print("Found a match... Title: ", current_book.get_title(),
                  ", ISBN: ", current_book.get_isbn())

    # Test 3
    # Get the last book in the list and return it
    # Then, using setters, update the other information for this book
    current_book = book_list[-1]
    current_book.return_it()

# Entry point of the program
if __name__ == "__main__":
    main()
