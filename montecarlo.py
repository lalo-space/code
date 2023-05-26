from PIL import Image
import random

def load_image(filename):
    image = Image.open(filename).convert("L")  # Converte l'immagine in scala di grigi
    return image

def calculate_area(image, num_samples):
    width, height = image.size
    pixel_count = 0
    total_samples = 0

    for _ in range(num_samples):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        pixel_value = image.getpixel((x, y))

        if pixel_value == 0:  # Assumendo che il colore bianco sia rappresentato da 0
            pixel_count += 1

        total_samples += 1

    area = (pixel_count / total_samples) * (width * height)
    return area

# Esempio di utilizzo
image = load_image("image.jpg")
num_samples = 1000000  # Numero di campioni per il metodo di Montecarlo

area = calculate_area(image, num_samples)
print("Area calcolata:", area)
