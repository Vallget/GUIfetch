from PIL import Image, ImageDraw, ImageTk


def create_circular_image_with_round_border(image_path, size, border_width=5, border_color=(0, 122, 255)):
    image = Image.open(image_path).resize((size, size)).convert("RGBA")

    # Створюємо маску для круга
    mask = Image.new('L', (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)

    # Робимо кругле зображення
    circular_image = Image.new('RGBA', (size, size))
    circular_image.paste(image, (0, 0), mask=mask)

    # Розмір зображення з рамкою
    total_size = size + border_width * 2

    # Створюємо нове зображення з прозорим фоном
    final_image = Image.new('RGBA', (total_size, total_size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(final_image)

    # Малюємо зовнішнє коло (рамку)
    draw.ellipse((0, 0, total_size, total_size), fill=border_color + (255,))

    # Вставляємо кругле зображення поверх
    final_image.paste(circular_image, (border_width, border_width), mask=mask)

    return ImageTk.PhotoImage(final_image)

