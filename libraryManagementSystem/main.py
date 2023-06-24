import tkinter as tk

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def display_available_books(self):
        available_books = []
        for book in self.books:
            if book.available:
                available_books.append(str(book))
        return available_books

    def search_book(self, title):
        search_results = []
        for book in self.books:
            if book.title.lower() == title.lower():
                search_results.append(str(book))
        return search_results


def add_book():
    title = entry_title.get()
    author = entry_author.get()
    book = Book(title, author)
    library.add_book(book)
    entry_title.delete(0, tk.END)
    entry_author.delete(0, tk.END)
    update_available_books()


def search():
    title = entry_search.get()
    search_results = library.search_book(title)
    listbox_search_results.delete(0, tk.END)
    for result in search_results:
        listbox_search_results.insert(tk.END, result)


def update_available_books():
    available_books = library.display_available_books()
    listbox_available_books.delete(0, tk.END)
    for book in available_books:
        listbox_available_books.insert(tk.END, book)


library = Library()

root = tk.Tk()
root.title("Library Management System")
root.geometry("800x800")

label_title = tk.Label(root, text="Title:")
label_title.pack()
entry_title = tk.Entry(root, width=50)
entry_title.pack()

label_author = tk.Label(root, text="Author:")
label_author.pack()
entry_author = tk.Entry(root, width=50)
entry_author.pack()

button_add_book = tk.Button(root, text="Add Book", command=add_book, width=20)
button_add_book.pack()

label_search = tk.Label(root, text="Search:")
label_search.pack()
entry_search = tk.Entry(root, width=50)
entry_search.pack()

button_search = tk.Button(root, text="Search", command=search, width=20)
button_search.pack()

label_available_books = tk.Label(root, text="Available Books:")
label_available_books.pack()
listbox_available_books = tk.Listbox(root, width=80)
listbox_available_books.pack()

label_search_results = tk.Label(root, text="Search Results:")
label_search_results.pack()
listbox_search_results = tk.Listbox(root, width=80)
listbox_search_results.pack()

update_available_books()

root.mainloop()
