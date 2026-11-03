print("Library Borrowing Management System\n")
records = {
    "member1": ["Book A", "Book B"],
    "member2": [],
    "member3": ["Book A", "Book C", "Book B"],
    "member4": ["Book C"],
    "member5": ["Book A"]
}

# Step 1: Compute average number of books borrowed by all members
def average(records):
    total_books = 0
    # Count total books borrowed
    for books in records.values():
        total_books = total_books + len(books)

    # Count total members
    total_members = len(records)

    # Calculate average
    average = total_books / total_members
    print(f"Average books borrowed per member: {average:.2f}") 
average(records) #call of average Function

# Step 2: Find the book with the highest and lowest number of borrowings
def max_min(records):
    book_count = {}

    for books in records.values():
        for book in books:
            if book not in book_count:
                book_count[book] = 1
            else:
                book_count[book] += 1

    most = max(book_count, key=book_count.get)
    least = min(book_count, key=book_count.get)
    print("Most borrowed book :", most, "for", book_count[most], "times")
    print("Least borrowed book:", least, "for", book_count[least], "times")

max_min(records) #call of max_min Function

# Step 3: Count members who have not borrowed any books
def zero_members(records):
    count = 0

    for books in records.values():
        if len(books) == 0:
            count = count + 1

    print(f"Number of members who borrowed 0 books: {count}")
zero_members(records) #call of zero_members Function
 
# Step 4: Display the most frequently borrowed book (mode)
def most_frequent_book(records):
    book_count = {}

    # Count each book
    for books in records.values():
        for book in books:
            if book not in book_count:
                book_count[book] = 1
            else:
                book_count[book] += 1

    if not book_count:
        return None

    max_count = max(book_count.values())

    mode_books = []

    for book in book_count:
        if book_count[book] == max_count:
            mode_books.append(book)

    print("Most frequently borrowed book(s):", ", ".join(mode_books))
most_frequent_book(records) #call of most_frequent_book Function