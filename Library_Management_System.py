# Library Management System
# Stores books in a list of dictionaries with basic operations
# Each book is a dictionary with: title, author, ISBN, and availability
books = []

# Display the main menu and get the user choice
def main_menu():
    print("\n----------------------------")
    print("WELCOME TO THE GREAT HARTLAND COMMUNITY LIBRARY")
    print("Please select one of the options below\n")
    print("[1] Add new book")
    print("[2] Search for books")
    print("[3] Checkout book")
    print("[4] Return book")
    print("[5] Show all books")
    print("[6] Exit")
    return input("Enter your choice (1-6): ")

# Add a new book to the library with validation
def add_book():
    print("\n*** Add New Book ***")
    
    # Book details to be input from the user
    title = input("Book title: ").strip()
    author = input("Author: ").strip()
    isbn = input("ISBN: ").strip()
    
    # Validate ISBN (can only be numbers and unique)
    if not isbn.isdigit():
        print("Error: ISBN must be numbers only!")
        return
    
    # Check for any duplicate ISBN
    for book in books:
        if book["isbn"] == isbn:
            print("Error: This ISBN already exists!")
            return
    
    # Add the new book to the list
    books.append({
        "title": title,
        "author": author,
        "isbn": isbn,
        "available": True
    })
    print("Book added successfully!")

# Search books by title, author or ISBN
def search_books():
    print("\n--- Search Books ---")
    search_term = input("Enter search term: ").strip().lower()
    
    found = []
    for book in books:
        # Check if search term matches in any field (not case-sensitive)
        if (search_term in book["title"].lower() or
            search_term in book["author"].lower() or
            search_term == book["isbn"]):
            found.append(book)
    
    if not found:
        print("\nNo matches found!")
        return
    
    print(f"\nFound {len(found)} book(s):")
    for i, book in enumerate(found, 1):
        status = "Available" if book["available"] else "Checked Out"
        print(f"{i}. {book['title']} by {book['author']} (ISBN: {book['isbn']}) - {status}")

# Mark a book as checked out if available
def checkout_book():
    isbn = input("Enter ISBN to checkout: ").strip() # Will remove extra unwanted spaces
    
    for book in books:
        if book["isbn"] == isbn:
            if book["available"]:
                book["available"] = False
                print("\nBook checked out successfully!")
            else:
                print("\nThis book is already checked out!")
            return
    
    print("\nBook not found!")

# Mark a book as returned (if it was checked out)
def return_book():
    isbn = input("Enter ISBN to return: ").strip()
    
    for book in books:
        if book["isbn"] == isbn:
            if not book["available"]:
                book["available"] = True
                print("\nBook returned successfully!")
            else:
                print("\nThis book isn't checked out!")
            return
    
    print("Book not found!")

# Display all the books in the library
def show_all_books():
    print("\n--- All Books ---")
    if not books:
        print("THERE ARE NO BOOKS IN THE LIBRARY!")
        return
    
    for i, book in enumerate(books, 1):
        status = "Available" if book["available"] else "Checked Out"
        print(f"{i}. {book['title']} by {book['author']} (ISBN: {book['isbn']}) - {status}")

# This loop keeps the program running until the user chooses to exit
while True:
    choice = main_menu()
    
    if choice == "1":
        add_book()
    elif choice == "2":
        search_books()
    elif choice == "3":
        checkout_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        show_all_books()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please enter 1-6")