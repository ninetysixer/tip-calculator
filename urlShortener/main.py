import tkinter as tk
import pyshorteners
import pyperclip


def shorten_url():
    long_url = entry.get()
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(long_url)
    result_label.config(text=short_url)
    copy_button.config(state="normal")


def copy_to_clipboard():
    short_url = result_label.cget("text")
    pyperclip.copy(short_url)


# Create the main window
window = tk.Tk()
window.title("URL Shortener")

# Create the URL entry field
entry = tk.Entry(window, width=50)
entry.pack(pady=10)

# Create the "Shorten" button
button = tk.Button(window, text="Shorten", command=shorten_url)
button.pack()

# Create the label to display the shortened URL
result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Create the "Copy" button
copy_button = tk.Button(window, text="Copy", command=copy_to_clipboard, state="disabled")
copy_button.pack()

# Start the main event loop
window.mainloop()
