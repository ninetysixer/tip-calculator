from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
dictionary = {}

# PANDAS DATA FRAME
try:
    data = pandas.read_csv("data/words_to_be_learned.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    dictionary = original_data.to_dict(orient="records")
else:
    dictionary = data.to_dict(orient="records")


# FUNCTIONS
def next_card():
    global current_card, flip_timer
    win.after_cancel(flip_timer)
    current_card = random.choice(dictionary)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(card_bg, image=card_front_img)
    win.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(card_bg, image=card_back_img)


def know_the_word():
    dictionary.remove(current_card)
    data = pandas.DataFrame(dictionary)
    data.to_csv("data/words_to_be_learned.csv", index=False)
    next_card()


# WINDOW
win = Tk()
win.title("Flashcard Project")
win.configure(background=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = win.after(3000, flip_card)

# BUTTONS
wrongbtn = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrongbtn, highlightthickness=0, command=next_card)
rightbtn = PhotoImage(file="images/right.png")
right_button = Button(image=rightbtn, highlightthickness=0, command=know_the_word)
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)


# CANVAS
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 264, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)
language_text = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

next_card()

win.mainloop()
