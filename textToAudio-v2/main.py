from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from gtts import gTTS

def convert_sentence_to_audio():
    sentence = entry.get()
    if not sentence:
        messagebox.showerror("Error", "Please enter a sentence.")
        return

    lang = language_var.get()
    if lang == "English":
        lang_code = "en"
    elif lang == "Turkish":
        lang_code = "tr"
    else:
        messagebox.showerror("Error", "Please select a language.")
        return

    tts = gTTS(text=sentence, lang=lang_code)

    save_path = filedialog.asksaveasfilename(defaultextension=".mp3",
                                             filetypes=[("MP3 Audio", "*.mp3")])
    if save_path:
        tts.save(save_path)
        messagebox.showinfo("Success", "Audio file saved successfully.")

# Create the main window
window = Tk()
window.title("Text-to-Audio Converter")
window.geometry("600x250")

# Calculate the center coordinates
window.update_idletasks()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
window.geometry(f"+{x}+{y}")

# Welcome label
welcome_label = Label(window, text="Welcome to Text-To-Audio App by semihdursungul", font=("Arial", 18))
welcome_label.pack(pady=20)

# Language selection
language_var = StringVar(window)
language_var.set("English")

language_frame = Frame(window)
language_frame.pack()

language_label = Label(language_frame, text="Select Language:", font=("Arial", 16))
language_label.pack(side=LEFT, padx=(20, 10))

english_radio = Radiobutton(language_frame, text="English", variable=language_var, value="English", font=("Arial", 14))
english_radio.pack(side=LEFT)

turkish_radio = Radiobutton(language_frame, text="Turkish", variable=language_var, value="Turkish", font=("Arial", 14))
turkish_radio.pack(side=LEFT)

# Sentence input
sentence_label = Label(window, text="Enter Sentence:", font=("Arial", 16))
sentence_label.pack()

entry = Entry(window, width=30, font=("Arial", 14))
entry.pack(pady=10)

# Convert button
convert_button = Button(window, text="Convert to Audio", font=("Arial", 16), command=convert_sentence_to_audio)
convert_button.pack()

# Run the GUI
window.mainloop()
