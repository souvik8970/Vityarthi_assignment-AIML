import book_ops

def main():
    while True:
        print("\n--- LIBRARY MANAGEMENT SYSTEM ---")
        print("1. Add New Book")
        print("2. Search Book")
        print("3. View Inventory")
        print("4. AI User Classification (New Feature)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            print("\n--- ADD BOOK ---")
            isbn = input("Enter ISBN: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            genre = input("Enter Genre (e.g. Fiction, Tech, History): ")
            
            # Now passing all 4 arguments including genre
            book_ops.add_book(isbn, title, author, genre)

        elif choice == '2':
            print("\n--- SEARCH BOOK ---")
            query = input("Enter Title or Author to search: ")
            book_ops.search_book(query)

        elif choice == '3':
            print("\n--- CURRENT INVENTORY ---")
            book_ops.view_inventory()

        elif choice == '4':
            # This calls your new AI function
            book_ops.classify_user_interest()

        elif choice == '5':
            print("Exiting system. Data saved.")
            break

        else:
            print("Invalid choice! Please enter 1-5.")

if __name__ == "__main__":
    main()