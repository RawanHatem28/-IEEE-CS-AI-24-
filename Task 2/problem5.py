def add_book_to_catalogue():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    publication_year = int(input("Enter the publication year of the book: "))
    return {"title": title, "author": author, "publication_year": publication_year}

def main():
    library_catalogue = {}

    while True:
        choice = input("Would you like to add a book to the catalogue? (yes/no): ").lower()
        if choice != 'yes':
            break

        book_id = len(library_catalogue) + 1
        library_catalogue[f"book{book_id}"] = add_book_to_catalogue()

    print("\nLibrary Catalogue:")
    for book_id, book_info in library_catalogue.items():
        print(f"Book ID: {book_id}")
        print(f"Title: {book_info['title']}")
        print(f"Author: {book_info['author']}")
        print(f"Publication Year: {book_info['publication_year']}")
        print()


main()
