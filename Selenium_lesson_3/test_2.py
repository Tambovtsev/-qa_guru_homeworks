import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Локаторы элементов формы на странице
LOGIN_INPUT = (By.ID, "login-input")
PASSWORD_INPUT = (By.ID, "password-input")
SUBMIT_BUTTON = (By.ID, "submit-button")
STATUS_MESSAGE = (By.ID, "error-message")
WELCOME_MESSAGE = (By.ID, "welcome-message")


@pytest.fixture
def driver():
    """Фикстура для инициализации и закрытия браузера."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


# Реализация DDT подхода через параметризацию pytest
# Реализация DDT подхода через параметризацию pytest
# Реализация DDT подхода через параметризацию pytest
@pytest.mark.parametrize(
    "email, password, scenario_type, expected_text",
    [
        # --- ПОЗИТИВНЫЕ СЦЕНАРИИ ---
        ("user1", "password1", "positive", "Welcome, user1!"),

        # --- НЕГАТИВНЫЕ СЦЕНАРИИ ---
        ("QAGURU@QA.GURU", "qaguru", "negative", "Wrong login or password"),
        ("qaguru@qa.guru", "wrong_pass", "negative", "Wrong login or password"),
        ("unknown@qa.guru", "qaguru", "negative", "Wrong login or password"),

        # Специфические валидации пустых полей:
        ("", "qaguru", "negative", "Login is required (minimum 3 characters)"),
        ("qaguru@qa.guru", "", "negative", "Password is required (minimum 6 characters)"),
        ("", "", "negative", "Login and password are required (minimum 3 and 6 characters)"),  # ИСПРАВЛЕНО ТУТ

        # Формат Email:
        ("qaguruqa.guru", "qaguru", "negative", "Wrong login or password"),
        ("qaguru@", "qaguru", "negative", "Wrong login or password"),
        ("@qa.guru", "qaguru", "negative", "Wrong login or password"),
        ("qaguru' OR '1'='1", "' OR '1'='1", "negative", "Wrong login or password"),
    ]
)
def test_login_form(driver, email, password, scenario_type, expected_text):
    """Тест кейс, принимающий наборы данных (DDT)."""
    # 1. Открытие тестируемой страницы через стабильное зеркало
    driver.get("https://demo.qa.guru/login.html")

    # 2. Поиск элементов формы
    email_field = driver.find_element(*LOGIN_INPUT)
    password_field = driver.find_element(*PASSWORD_INPUT)
    submit_button = driver.find_element(*SUBMIT_BUTTON)

    # 3. Очистка полей и ввод тестовых данных
    email_field.clear()
    email_field.send_keys(email)
    password_field.clear()
    password_field.send_keys(password)

    # 4. Клик по кнопке отправки формы
    submit_button.click()

    # 5. Ожидание появления ответа (Алерт ИЛИ Текст)
    wait = WebDriverWait(driver, 4)
    actual_result = ""

    try:
        # Проверяем браузерный alert (если вдруг он предусмотрен)
        alert = wait.until(EC.alert_is_present())
        actual_result = alert.text
        alert.accept()
    except TimeoutException:
        # Умное ожидание: ждем, пока текст ХОТЯ БЫ ОДНОГО из элементов заполнится
        try:
            wait.until(lambda d: d.find_element(*STATUS_MESSAGE).text != "" or
                                 d.find_element(*WELCOME_MESSAGE).text != "")

            # Как только текст появился, забираем его из того элемента, который заполнен
            error_text = driver.find_element(*STATUS_MESSAGE).text
            welcome_text = driver.find_element(*WELCOME_MESSAGE).text

            actual_result = error_text if error_text != "" else welcome_text
        except TimeoutException:
            pytest.fail("Текст ответа (ошибка или приветствие) так и не появился на странице")

    # 6. Проверка результата (Assertion)
    assert expected_text in actual_result, f"Ожидался текст '{expected_text}', но на странице получено: '{actual_result}'"
