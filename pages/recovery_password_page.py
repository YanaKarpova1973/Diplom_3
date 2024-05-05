from pages.base_page import BasePage
import allure
from locators.recovery_password_locators import RecoveryPasswordLocators

class RecoveryPasswordPage(BasePage):

    @allure.step('Ожидание загрузки заголовка страницы Восстановления пароля')
    def wait_for_recovery_page_header_loaded(self):
        self.wait_for_element_loaded(RecoveryPasswordLocators.HEADER_RESTORE_PASSWORD)

    @allure.step('Ввести email')
    def enter_email(self, email):
        self.send_keys_to_element_located(locator=RecoveryPasswordLocators.EMAIL_INPUT_FIELD, keys=email)

    @allure.step('Кнопка восстановления пароля')
    def recover_button_click(self):
        self.click_element_located(RecoveryPasswordLocators.BUTTON_RESTORE_PASSWORD)

    @allure.step('Кнопка Показать пароль')
    def button_password_click(self):
        self.click_element_located(RecoveryPasswordLocators.SHOW_PASSWORD_BUTTON)

    @allure.step('Проверка активности поля ввода пароля')
    def password_checking(self):
        return self.find_element_located(RecoveryPasswordLocators.ACTIVE_PASSWORD_INPUT_FIELD)
