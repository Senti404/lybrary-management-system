# Library Management System
# Stores books in a list of dictionaries with basic operations
# Each book is a dictionary with: title, author, ISBN, and availability
import datetime
import calendar

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

def add_book():
    print("\n*** Add New Book ***")
    
    title = input("Book title: ").strip()
    author = input("Author: ").strip()
    isbn = input("ISBN: ").strip()
    
    if not isbn.isdigit():
        print("Error: ISBN must be numbers only!")
        return
    
    for book in books:
        if book["isbn"] == isbn:
            print("Error: This ISBN already exists!")
            return
    
    books.append({
        "title": title,
        "author": author,
        "isbn": isbn,
        "available": True
    })
    print("Book added successfully!")

def search_books():
    print("\n--- Search Books ---")
    search_term = input("Enter search term: ").strip().lower()
    
    found = []
    for book in books:
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

def checkout_book():
    isbn = input("Enter ISBN to checkout: ").strip()
    
    for book in books:
        if book["isbn"] == isbn:
            if book["available"]:
                book["available"] = False
                current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                checkout_date = datetime.datetime.now()
                due_date = checkout_date + datetime.timedelta(days=14)
                due_date_str = due_date.strftime("%d/%m/%Y")
                day_name = calendar.day_name[due_date.weekday()]
                print("\nBOOK CHECKED OUT SUCCESSFULLY!")
                print(f"Time of checkout: {current_time}")
                print(f"Due Date: {due_date_str} ({day_name})")             
            else:
                print("\nThis book is already checked out!")
            return
    
    print("\nBook not found!")

def return_book():
    isbn = input("Enter ISBN to return: ").strip()
    
    for book in books:
        if book["isbn"] == isbn:
            if not book["available"]:
                book["available"] = True
                current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                print("\nBOOK RETURNED SUCCESSFULLY!")
                print(f"Time of return: {current_time}")
            else:
                print("\nThis book isn't checked out!")
            return
    
    print("Book not found!")

def show_all_books():
    print("\n--- All Books ---")
    if not books:
        print("THERE ARE NO BOOKS IN THE LIBRARY!")
        return
    
    for i, book in enumerate(books, 1):
        status = "Available" if book["available"] else "Checked Out"
        print(f"{i}. {book['title']} by {book['author']} (ISBN: {book['isbn']}) - {status}")

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
