import logging
import requests
import json

#Настройка логирования
logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w', encoding='utf-8', format='%(levelname)s: %(message)s')


def main():
    url = "https://dummyjson.com/test"
    try:
        response = requests.get(url)
        #Проверка статуса ответа
        response.raise_for_status() 
        data = response.json()
        print(json.dumps(data, indent=4))
        logging.info("Данные успешно получены")
    except requests.exceptions.RequestException as e:
        logging.error(e)
        logging.error(f"Ошибка при выполнении запроса: {e}")

if __name__ == "__main__":
    main()