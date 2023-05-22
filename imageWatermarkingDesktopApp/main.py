import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont


def browse_image():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=(("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*")))
    # Perform watermarking operations on the selected image
    apply_watermark()


def apply_watermark():
    watermark_text = watermark_entry.get()  # Get the watermark text from the entry field
    image = Image.open(file_path)
    watermark = Image.new("RGBA", image.size, (255, 255, 255, 0))

    draw = ImageDraw.Draw(watermark)
    font = ImageFont.truetype("arial.ttf", 72)  # Choose your desired font and size

    # Get the dimensions of the image and the watermark
    image_width, image_height = image.size
    watermark_width, watermark_height = draw.textsize(watermark_text, font=font)

    # Calculate the position to place the watermark at the center of the image
    x = (image_width - watermark_width) // 2
    y = (image_height - watermark_height) // 2

    draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))  # Adjust transparency as needed

    watermarked_image = Image.alpha_composite(image.convert("RGBA"), watermark)
    watermarked_image.show()  # Display the watermarked image


# Create a window
window = tk.Tk()
window.geometry("600x600")
# Add components and define their behavior
browse_button = tk.Button(window, text="Browse", command=browse_image)
browse_button.pack()

watermark_label = tk.Label(window, text="Watermark Text:")
watermark_label.pack()

watermark_entry = tk.Entry(window)
watermark_entry.pack()

# Run the event loop
window.mainloop()
