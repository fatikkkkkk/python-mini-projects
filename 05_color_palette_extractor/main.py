from PIL import Image
from collections import Counter

def extract_colors(image_path, num_colors=5):
    image = Image.open(image_path)
    image = image.resize((100, 100))  # performans için küçült
    pixels = list(image.getdata())

    most_common = Counter(pixels).most_common(num_colors)
    return most_common

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

if __name__ == "__main__":
    image_path = "sample.jpg"
    colors = extract_colors(image_path)

    print("Baskın Renkler:")
    for color, count in colors:
        print(rgb_to_hex(color))
