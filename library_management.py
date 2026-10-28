import json
import os

FILE_NAME = "library.json"


def load_books():
    """Load books from the JSON file."""
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return []
    return []


def save_books(books):
    """Save books to the JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(books, file, indent=4)


def display_books(books):
    """Display all books in the library."""
    if not books:
        print("\nNo books available in the library.")
        return

    print("\n" + "-" * 75)
    print(f"{'ID':<8}{'Title':<25}{'Author':<20}{'Status':<15}")
    print("-" * 75)

    for book in books:
        status = "Available" if book["available"] else "Issued"
        print(
            f"{book['id']:<8}"
            f"{book['title']:<25}"
            f"{book['author']:<20}"
            f"{status:<15}"
        )

    print("-" * 75)


def add_book(books):
    """Add a new book."""
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()

    if not title or not author:
        print("Title and author cannot be empty.")
        return

    new_id = max((book["id"] for book in books), default=0) + 1

    book = {
        "id": new_id,
        "title": title,
        "author": author,
        "available": True
    }

    books.append(book)
    save_books(books)

    print(f"Book added successfully! Book ID: {new_id}")


def search_book(books):
    """Search books by title or author."""
    keyword = input("Enter title or author to search: ").strip().lower()

    results = [
        book for book in books
        if keyword in book["title"].lower()
        or keyword in book["author"].lower()
    ]

    if results:
        display_books(results)
    else:
        print("No matching books found.")


def issue_book(books):
    """Issue an available book."""
    try:
        book_id = int(input("Enter book ID to issue: "))
    except ValueError:
        print("Please enter a valid numeric ID.")
        return

    for book in books:
        if book["id"] == book_id:
            if book["available"]:
                book["available"] = False
                save_books(books)
                print(f"'{book['title']}' issued successfully!")
            else:
                print("This book has already been issued.")
            return

    print("Book ID not found.")


def return_book(books):
    """Return an issued book."""
    try:
        book_id = int(input("Enter book ID to return: "))
    except ValueError:
        print("Please enter a valid numeric ID.")
        return

    for book in books:
        if book["id"] == book_id:
            if not book["available"]:
                book["available"] = True
                save_books(books)
                print(f"'{book['title']}' returned successfully!")
            else:
                print("This book is already available.")
            return

    print("Book ID not found.")


def delete_book(books):
    """Delete a book from the library."""
    try:
        book_id = int(input("Enter book ID to delete: "))
    except ValueError:
        print("Please enter a valid numeric ID.")
        return

    for book in books:
        if book["id"] == book_id:
            if not book["available"]:
                print("Return the book before deleting it.")
                return

            books.remove(book)
            save_books(books)
            print("Book deleted successfully!")
            return

    print("Book ID not found.")


def main():
    books = load_books()

    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Display All Books")
        print("2. Add a Book")
        print("3. Search for a Book")
        print("4. Issue a Book")
        print("5. Return a Book")
        print("6. Delete a Book")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            display_books(books)
        elif choice == "2":
            add_book(books)
        elif choice == "3":
            search_book(books)
        elif choice == "4":
            issue_book(books)
        elif choice == "5":
            return_book(books)
        elif choice == "6":
            delete_book(books)
        elif choice == "7":
            print("Thank you for using the Library Management System!")
            break
        else:
            print("Invalid choice. Please select between 1 and 7.")


if __name__ == "__main__":
    main()
```
