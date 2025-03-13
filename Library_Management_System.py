# Import built-in modules to manage timestamp and due date in checkouts and returns
import datetime
import calendar

# Library Management System
# Stores books in a list of dictionaries with basic operations
# Each book is a dictionary with: title, author, ISBN, and availability
books = [
    {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "isbn": "9780261102385", "available": True},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "isbn": "9780345339683", "available": True},
    {"title": "A Game of Thrones", "author": "George R.R. Martin", "isbn": "9780553103540", "available": True},
    {"title": "1984", "author": "George Orwell", "isbn": "9780451524935", "available": True},
    {"title": "The Brothers Karamazov", "author": "Fyodor Dostoevsky", "isbn": "9780374528379", "available": True},
    {"title": "The Divine Comedy", "author": "Dante Alighieri", "isbn": "9780140448955", "available": True},
    {"title": "The Da Vinci Code", "author": "Dan Brown", "isbn": "9780307474278", "available": True},
    {"title": "War and Peace", "author": "Leo Tolstoy", "isbn": "9781400079988", "available": True},
    {"title": "Lord of the Flies", "author": "William Golding", "isbn": "9780399501487", "available": True},
    {"title": "The Prince", "author": "Niccolò Machiavelli", "isbn": "9780140441079", "available": True},
    {"title": "Pinocchio", "author": "Carlo Collodi", "isbn": "9780141331645", "available": True}
]

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
    isbn = input("Enter ISBN to checkout: ").strip()  # Will remove extra unwanted spaces
    
    for book in books:
        if book["isbn"] == isbn:
            if book["available"]:
                book["available"] = False
                current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # Get the current date and time in the UK format
                checkout_date = datetime.datetime.now()  # Store the current date and time as a datetime object
                due_date = checkout_date + datetime.timedelta(days=14)  # Calculate the due date by adding 14 days to the checkout date
                due_date_str = due_date.strftime("%d/%m/%Y")  # Format the due date as a string in "DD/MM/YYYY" format
                day_name = calendar.day_name[due_date.weekday()]  # Get the name of the day corresponding to the due date
                print("\nBOOK CHECKED OUT SUCCESSFULLY!")
                print(f"Time of checkout: {current_time}")
                print(f"Due Date: {due_date_str} ({day_name})")             
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
                current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get the current date and time in the UK format
                print("\nBOOK RETURNED SUCCESSFULLY!")
                print(f"Time of return: {current_time}")
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
