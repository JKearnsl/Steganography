"""
    Модуль сокрытия изображения в изображении путем изменения наименее значимых бит

    Используется метод LSB
"""
import os

from PIL import Image
from PIL.PyAccess import PyAccess


def hide(cover_path: str, img_path: str, output_dir: str) -> str:
    container = Image.open(cover_path)
    data = Image.open(img_path)

    container_pixels: PyAccess = container.load()
    data_pixels: PyAccess = data.load()

    result_path = os.path.join(output_dir, "hidden.png")

    if data.size[0] * data.size[1] > container.size[0] * container.size[1]:
        raise ValueError("Ошибка: Размер данных для скрытия больше размера контейнера")

    for i in range(data.size[0]):
        for j in range(data.size[1]):
            container_pixel = list(container_pixels[i, j])
            data_pixel = tuple(data_pixels[i, j])

            for channel in range(3):
                container_pixel[channel] = (container_pixel[channel] & 0b11111100) | (data_pixel[channel] >> 6)

            container_pixels[i, j] = tuple(container_pixel)

    container.save(result_path)
    return result_path


def reveal(img_path: str, output_dir: str) -> str:
    img = Image.open(img_path)
    reveal_image = Image.new("RGB", img.size)

    img_pixels: PyAccess = img.load()
    reveal_pixels: PyAccess = reveal_image.load()

    reveal_path = os.path.join(output_dir, "revealed.png")

    # Проходим по каждому пикселю для извлечения данных из LSB
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            img_pixel = list(img_pixels[i, j])
            reveal_pixel = [0, 0, 0]

            for channel in range(3):
                reveal_pixel[channel] = (img_pixel[channel] & 0b00000011) << 6

            reveal_pixels[i, j] = tuple(reveal_pixel)

    reveal_image.save(reveal_path)
    return reveal_path
