from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import speech_recognition as sr


def import_audio():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
    if file_path:
        transcribe_audio(file_path)


def transcribe_audio(file_path):
    r = sr.Recognizer()

    try:
        with sr.AudioFile(file_path) as source:
            audio_data = r.record(source)
            text = r.recognize_google(audio_data, language="en-US")

        save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text File", "*.txt")])
        if save_path:
            with open(save_path, "w") as file:
                file.write(text)
            messagebox.showinfo("Success", "Transcription saved successfully.")

    except sr.UnknownValueError:
        messagebox.showerror("Error", "Speech recognition could not understand the audio.")
    except sr.RequestError:
        messagebox.showerror("Error", "Could not connect to the speech recognition service.")
    except ValueError:
        messagebox.showerror("Error", "Audio file could not be read. Please check if the file is corrupted or in another format.")


# Create the main window
window = Tk()
window.title("Audio Transcriber")
window.geometry("600x150")

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
welcome_label = Label(window, text="Welcome to Audio Transcriber by semihdursungul", font=("Arial", 18))
welcome_label.pack(pady=20)

# Import Audio button
import_button = Button(window, text="Add File", font=("Arial", 16), command=import_audio)
import_button.pack(pady=10)

# Run the GUI
window.mainloop()
