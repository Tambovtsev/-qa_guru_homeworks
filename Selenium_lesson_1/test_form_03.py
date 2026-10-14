import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test1():  # Измененный тест, со своими данными и на поля Current Address и Permanent Address
    # 1. Запуск браузера Chrome
    driver = webdriver.Chrome()
    try:
        # 2. Открытие страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(1)  # Пауза, чтобы визуально заметить открытие

        # 3. Поиск элементов и заполнение полей
        # Находим поле Full Name по его ID и вводим текст
        full_name_field = driver.find_element(By.ID, "userName")
        # web_elements = driver.find_elements(By.XPATH, "someXPath")

        full_name_field.send_keys("Владимир Сергеевич")

        # Находим поле Email по его ID и вводим текст
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("xxx123@example.com")

        currentAddress_field = driver.find_element(By.ID, "currentAddress")
        currentAddress_field.send_keys("г. Саранск, ул. Ленина, 11")

        permanentAddress_field = driver.find_element(By.ID, "permanentAddress")
        permanentAddress_field.send_keys("г. Москва, ул. Сергеева, 11")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(1)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")

        # Проверяем, что в блоке результата появился введенный текст
        assert "Владимир Сергеевич" in result_box.text
        assert "г. Саранск, ул. Ленина, 11" in result_box.text
        assert "г. Москва, ул. Сергеева, 11" in result_box.text
        assert "xxx123@example.com" in result_box.text
        print("Тест успешно пройден!")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()


def test2():  # Тест на длину имени
    # 1. Запуск браузера Chrome
    driver = webdriver.Chrome()
    try:
        # 2. Открытие страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(1)  # Пауза, чтобы визуально заметить открытие

        # 3. Поиск элементов и заполнение полей
        # Находим поле Full Name по его ID и вводим текст
        full_name_field = driver.find_element(By.ID, "userName")
        # web_elements = driver.find_elements(By.XPATH, "someXPath")

        full_name_field.send_keys("jldkjvbdkfvjldskjvblkdsjbfvlkdsjbfvlkjdsbfvlkjdsbfvlkldkfvb")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(1)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")

        # Проверяем, что в блоке результата появился введенный текст
        assert "jldkjvbdkfvjldskjvblkdsjbfvlkdsjbfvlkjdsbfvlkjdsbfvlkldkfvb" in result_box.text
        print("Тест успешно пройден!")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()


def test3():  # Негативный тест на ввод email без домена
    # 1. Запуск браузера Chrome
    driver = webdriver.Chrome()
    try:
        # 2. Открытие страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(1)  # Пауза, чтобы визуально заметить открытие

        # Находим поле Email по его ID и вводим текст
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("xxx123@example")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(1)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")

        # Проверяем, что в блоке результата появился введенный текст
        assert "xxx123@example" in result_box.text
        print("Тест успешно пройден!")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()


def test4():  # Тест на ввод адреса на английском языке с использованием специальных символов
    # 1. Запуск браузера Chrome
    driver = webdriver.Chrome()
    try:
        # 2. Открытие страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(1)  # Пауза, чтобы визуально заметить открытие

        # 3. Поиск элементов и заполнение полей

        currentAddress_field = driver.find_element(By.ID, "currentAddress")
        currentAddress_field.send_keys("Saransk City, Lenina Street, $72*>")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(1)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")

        # Проверяем, что в блоке результата появился введенный текст
        assert "Saransk City, Lenina Street, $72*>" in result_box.text
        print("Тест успешно пройден!")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()
