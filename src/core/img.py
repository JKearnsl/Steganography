"""
    Модуль сокрытия изображения в изображении путем изменения наименее значимых бит

"""
import os

from PIL import Image


def hide(cover_path: str, img_path: str, output_dir: str) -> str:
    cover = Image.open(cover_path)
    img = Image.open(img_path)
    result_path = os.path.join(output_dir, "hidden.png")

    if cover.size != img.size:
        raise ValueError("Размеры изображений должны быть одинаковыми")

    cover_pixels = tuple(cover.getdata())
    img_pixels = tuple(img.getdata())

    new_pixels = []

    for cover_pixel, img_pixel in zip(cover_pixels, img_pixels):
        r_cover, g_cover, b_cover = cover_pixel
        r_img, g_img, b_img = img_pixel

        r_embedded = (r_cover & 0b11111100) | (r_img >> 6)
        g_embedded = (g_cover & 0b11111100) | (g_img >> 6)
        b_embedded = (b_cover & 0b11111100) | (b_img >> 6)

        new_pixels.append((r_embedded, g_embedded, b_embedded))

    new_image = Image.new('RGB', cover.size)
    new_image.putdata(new_pixels)
    new_image.save(result_path)
    return result_path


def reveal(img_path: str, output_dir: str) -> str:
    img = Image.open(img_path)
    img_pixels = tuple(img.getdata())
    reveal_path = os.path.join(output_dir, "revealed.png")

    hidden_pixels = []

    for img_pixel in img_pixels:
        r_img, g_img, b_img = img_pixel

        r_hidden = (r_img & 0b00000011) << 6
        g_hidden = (g_img & 0b00000011) << 6
        b_hidden = (b_img & 0b00000011) << 6

        hidden_pixels.append((r_hidden, g_hidden, b_hidden))

    secret_image = Image.new('RGB', img.size)
    secret_image.putdata(hidden_pixels)
    secret_image.save(reveal_path)
    return reveal_path
