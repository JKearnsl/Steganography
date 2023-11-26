
def encode_file():
    pass

def decode_file():
    pass


def hide_image():
    pass

def reveal_image():
    pass







def main():
    while True:
        print("\n\nЧто вы хотите сделать?")
        print("1. Закодировать файл")
        print("2. Раскодировать файл")
        print("3. Скрыть изображение")
        print("4. Раскрыть изображение")
        print("5. Выход")
        choice = input("Ваш выбор: ")
        if choice == "1":
            encode_interval_lz78()
        elif choice == "2":
            decode_interval_lz78()
        elif choice == "3":
            encode_interval()
        elif choice == "4":
            decode_interval()
        elif choice == "5":
            break
        else:
            print("Неверный ввод")


if __name__ == "__main__":
    main()
