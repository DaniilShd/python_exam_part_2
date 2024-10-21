import logging
import cowsay

#Настройка логирования
logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w', encoding='utf-8', format='%(levelname)s: %(message)s')

def main():
    try:
        command = input("Введите сообщение")
    except ValueError as err:
        logging.error(f"при вводе данных возникла ошибка {err}")
    except TypeError as err:
        logging.error(f"при вводе данных возникла ошибка {err}")
    cowsay.cow(command)
    logging.info("Программа успешно выполнена")

if __name__ == "__main__":
    main()