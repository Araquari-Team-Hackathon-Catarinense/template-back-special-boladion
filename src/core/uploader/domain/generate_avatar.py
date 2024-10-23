import io
import random

from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image, ImageDraw, ImageFont


def textsize(text, font):
    im = Image.new(mode="P", size=(0, 0))
    draw = ImageDraw.Draw(im)
    _, _, width, height = draw.textbbox((0, 0), text=text, font=font)
    return width, height


def generate_avatar(username):
    background_colors = [
        (0, 0, 0),
        (255, 0, 0),
        (0, 255, 0),
        (0, 0, 255),
        (255, 255, 0),
        (255, 0, 255),
        (0, 255, 255),
        (128, 128, 128),
        (128, 0, 0),
        (0, 128, 0),
        (0, 0, 128),
        (128, 128, 0),
        (128, 0, 128),
        (0, 128, 128),
        (192, 192, 192),
        (255, 140, 0),
        (128, 0, 128),
        (0, 128, 128),
        (0, 255, 255),
        (0, 255, 140),
        (255, 0, 140),
        (255, 140, 255),
        (140, 255, 255),
        (255, 140, 140),
    ]

    background_color = random.choice(background_colors)

    if sum(background_color) / 3 > 128:
        text_color = (0, 0, 0)
    else:
        text_color = (255, 255, 255)

    width, height = 50, 50
    image = Image.new("RGB", (width, height), "white")

    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("src/core/uploader/domain/Inter.ttf", 30)

    text = list(username)[0].upper()

    text_width, text_height = textsize(text, font)

    x = (width - text_width) // 2
    y = (height - text_height) // 2 - 5

    image.paste(background_color, [0, 0, width, height])
    draw.text((x, y), text, fill=text_color, font=font)

    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)

    image_file = InMemoryUploadedFile(
        buffer, None, "image.png", "image/png", buffer.tell(), None
    )

    return image_file
