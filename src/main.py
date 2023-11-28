import os

from src.core import img


def request_filepath(request_text: str = "\n\nВведите путь к файлу") -> str | None:
    print(request_text)
    filepath = input("Путь: ")
    if not os.path.exists(filepath):
        print("Файл не найден")
        return
    return filepath


def encode_file():
    pass


def decode_file():
    pass


def hide_image():
    filepath_cover = request_filepath("\n\nВведите путь к изображению-контейнеру")
    filepath_img = request_filepath("Введите путь к изображению, которое нужно спрятать")
    output_dir = os.path.dirname(filepath_img)

    result_path = img.hide(cover_path=filepath_cover, img_path=filepath_img, output_dir=output_dir)
    print("Файл успешно спрятан")
    print("Результат сохранен в файл: ", result_path)


def reveal_image():
    filepath_img = request_filepath("\n\nВведите путь к изображению, которое нужно раскрыть")
    output_dir = os.path.dirname(filepath_img)

    result_path = img.reveal(img_path=filepath_img, output_dir=output_dir)
    print("Файл успешно раскрыт")
    print("Результат сохранен в файл: ", result_path)


def main():
    while True:
        print("\n\nЧто вы хотите сделать?")
        print("1. Закодировать изображение")
        print("2. Раскодировать изображение")
        print("3. Скрыть изображение")
        print("4. Раскрыть изображение")
        print("5. Выход")
        choice = input("Ваш выбор: ")
        if choice == "1":
            encode_file()
        elif choice == "2":
            decode_file()
        elif choice == "3":
            hide_image()
        elif choice == "4":
            reveal_image()
        elif choice == "5":
            break
        else:
            print("Неверный ввод")


if __name__ == "__main__":
    main()
