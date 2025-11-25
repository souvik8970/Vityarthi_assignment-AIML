import data_file

def add_book(isbn, title, author, genre):
    if isbn and title and author and genre:
        data_file.save_book_to_file(isbn, title, author, genre)
    else:
        print("Error: All fields are required!")

def search_book(query):
    books = data_file.read_all_books()
    found = False
    print("\n--- Search Results ---")
    for book in books:
        # Check if query is in Title (index 1) or Author (index 2)
        if query.lower() in book[1].lower() or query.lower() in book[2].lower():
            print(f"Found: {book[1]} by {book[2]} (ISBN: {book[0]}, Genre: {book[3]})")
            found = True
    if not found:
        print("No matching books found.")

def view_inventory():
    books = data_file.read_all_books()
    print("\n--- Library Inventory ---")
    if not books:
        print("Library is empty.")
    else:
        print(f"{'ISBN':<10} {'Title':<20} {'Author':<20} {'Genre':<15}")
        print("-" * 65)
        for book in books:
            # Ensure row has enough columns before printing to avoid index errors
            if len(book) >= 4:
                print(f"{book[0]:<10} {book[1]:<20} {book[2]:<20} {book[3]:<15}")

def classify_user_interest():
    """
    AI Feature for AI/ML Course Requirement
    """
    print("\n--- AI Analysis ---")
    history = input("Enter last 3 topics read: ").lower()
    
    if "python" in history or "code" in history:
        print("User Class: Tech Enthusiast")
    elif "fiction" in history or "story" in history:
        print("User Class: Fiction Lover")
    else:
        print("User Class: General Reader")