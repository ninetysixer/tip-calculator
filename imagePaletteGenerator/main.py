import io
import requests
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


def extract_colors_from_image(url, n_colors=10):
    # Load image from URL
    response = requests.get(url)
    img = Image.open(io.BytesIO(response.content))
    # Convert image to numpy array
    img_array = np.array(img)
    # Reshape numpy array to 2D array
    shape = img_array.shape
    img_array = img_array.reshape(np.prod(shape[:2]), shape[2]).astype(float)
    # Use KMeans clustering to extract dominant colors
    kmeans = KMeans(n_clusters=n_colors, random_state=42, n_init=10).fit(img_array)
    colors = kmeans.cluster_centers_
    # Convert colors from float to integer
    colors = colors.astype(int)
    # Convert colors to hexadecimal format
    hex_colors = [rgb_to_hex(color) for color in colors]
    # Display color palette
    generate_color_palette(colors)
    # Return top 10 most common colors in the image
    return hex_colors[:10]


def rgb_to_hex(color):
    return '#{:02x}{:02x}{:02x}'.format(*color)


def generate_color_palette(colors):
    # Convert RGB color values to float between 0 and 1
    colors = np.array(colors) / 255.0
    # Create a color map from the RGB values
    color_map = plt.cm.colors.ListedColormap(colors)
    # Generate the color palette using the color map
    n_colors = len(colors)
    fig, ax = plt.subplots(figsize=(n_colors, 2))
    fig.subplots_adjust(bottom=0.1)
    cb = plt.colorbar(plt.imshow(np.arange(n_colors).reshape(1, n_colors), cmap=color_map, aspect='auto'))
    cb.set_ticks(np.arange(n_colors))
    cb.set_ticklabels(['']*n_colors)
    ax.axis('off')
    plt.show()


url = "https://www.diken.com.tr/wp-content/uploads/2022/11/20221128-metallica.jpg"
colors = extract_colors_from_image(url)
print(colors)
