import time
from selenium import webdriver

# Инициализация драйвера (в Selenium 4 сервис скачивается автоматически)
driver = webdriver.Chrome()
driver.minimize_window()

try:
    # 1. Открываем целевую страницу учебной формы
    print("Открываем страницу формы...")
    driver.get("https://qa-guru.github.io/one-page-form/automation-practice-form.html")
    time.sleep(1)  # Пауза для наглядности студентам

    # 2. Демонстрация REFRESH (Обновление страницы)
    print("Обновляем текущую страницу...")
    driver.refresh()
    time.sleep(1)

    # 3. Переходим на другой сайт, чтобы создать историю переходов
    print("Переходим на сайт Google...")
    driver.get("https://google.com")
    time.sleep(1)

    # 4. Демонстрация BACK (Назад на страницу формы)
    print("Переходим назад в истории браузера...")
    driver.back()
    time.sleep(1)

    # 5. Демонстрация FORWARD (Вперед на страницу Google)
    print("Переходим вперед в истории браузера...")
    driver.forward()
    time.sleep(1)

finally:
    # Закрываем браузер после выполнения
    print("Закрываем браузер.")
    driver.quit()

    # driver.close() vs driver.quit(): Обратите внимание, что close() закрывает только активное окно/вкладку
    #  (если оно последнее — закроется браузер), а quit() полностью уничтожает процесс драйвера и закрывает всё.
