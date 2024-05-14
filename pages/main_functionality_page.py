from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.main_functionality_locators import MainFunctionalityLocators
import allure

class MainFunctionalityPage(BasePage):

    @allure.step('Ожидание загрузки заголовка главной страницы проекта')
    def wait_for_main_page_header_loaded(self):
        self.wait_for_element_loaded(MainFunctionalityLocators.MAIN_PAGE_HEADER)

    @allure.step('Кнопка Личный кабинет')
    def click_private_area_button(self):
        self.click_element_located(MainFunctionalityLocators.PRIVATE_AREA)

    @allure.step('Проверка наличия кнопки Войти в аккаунт для неавторизованого пользователя')
    def check_enter_account_button(self):
        return self.find_element_located(MainFunctionalityLocators.BUTTON_ENTER_ACCOUNT)

    @allure.step('Проверка наличия кнопки Оформить заказдля неавторизованого пользователя')
    def check_make_order_button(self):
        return self.find_element_located(MainFunctionalityLocators.BUTTON_MAKE_ORDER)

    @allure.step('Переход в Ленту Заказов')
    def click_orders_line(self):
        self.click_element_located(MainFunctionalityLocators.ORDER_LINE)

    @allure.step('Выбор первого ингредиента на главной странице')
    def click_first_ingredient(self):
        self.click_element_located(MainFunctionalityLocators.FIRST_INGREDIENT)

    @allure.step('Проверка видимости модального окна ингредиента')
    def check_modal_opened(self):
        try:
            self.find_element_waiting(MainFunctionalityLocators.INGREDIENT_MODAL_XPATH)
        except NoSuchElementException:
            return False
        return True

    @allure.step('Проверка невидимости модального окна ингредиента')
    def check_modal_closed(self):
        return self.wait_until_element_not_present(MainFunctionalityLocators.CLOSE_MODAL)

    @allure.step('Ожидание загрузки заголовка модального окна ингредиента')
    def wait_modal_header_loaded(self):
        self.wait_for_element_loaded(MainFunctionalityLocators.INGREDIENT_MODAL_HEADER)

    @allure.step('Закрыть модальное окно ингредиента')
    def click_close_modal(self):
        self.click_element_located(MainFunctionalityLocators.CLOSE_MODAL)
        self.wait_until_element_not_present(MainFunctionalityLocators.CLOSE_MODAL)

    @allure.step('Получение значения счетчика ингредиента')
    def get_first_ingredient_counter_value(self):
        return self.get_text_by_locator(MainFunctionalityLocators.FIRST_INGREDIENT_COUNTER_XPATH)

    @allure.step('Добавление первого ингредиента в корзину')
    def drag_n_drop_first_ingredient_to_basket(self):
        self.do_drag_n_drop(source=MainFunctionalityLocators.FIRST_INGREDIENT, target=MainFunctionalityLocators.BASKET)

    @allure.step('Оформить заказ')
    def click_make_order(self):
        self.click_element_located(MainFunctionalityLocators.BUTTON_MAKE_ORDER)

    @allure.step('Получение значения ID заказа при его оформлении')
    def get_order_id_when_created(self):
        self.wait_until_element_not_present(MainFunctionalityLocators.TEMPORARY_ORDER_MODAL_HEADER)
        return self.driver.find_element(By.XPATH, MainFunctionalityLocators.ORDER_ID_XPATH).text

    @allure.step('Создание заказа')
    def make_order(self):
        self.drag_n_drop_first_ingredient_to_basket()
        self.click_make_order()

    @allure.step('Ожидание загрузки модального окна')
    def wait_for_order_modal_window(self):
        self.wait_for_element_loaded(MainFunctionalityLocators.ORDER_IDENTIFIER)

    @allure.step('Ожидание загрузки заголовка страницы входа')
    def wait_for_entrance_page_header_loaded(self):
        return self.wait_for_element_loaded(MainFunctionalityLocators.ENTRANCE_HEADER)

    @allure.step('Переход по кнопке восстановления пароля')
    def click_restore_password(self):
        return self.click_element_located(MainFunctionalityLocators.BUTTON_RESTORE_PASSWORD)

    @allure.step('Ввести email')
    def enter_email(self, email):
        self.send_keys_to_element_located(locator=MainFunctionalityLocators.EMAIL_INPUT_FIELD, keys=email)

    @allure.step('Ввести пароль')
    def enter_password(self, password):
        self.send_keys_to_element_located(locator=MainFunctionalityLocators.PASSWORD_INPUT_FIELD, keys=password)

    @allure.step('Переход по кнопке Войти')
    def click_enter_button(self):
        return self.click_element_located(MainFunctionalityLocators.BUTTON_ENTER)

    @allure.step('Переход в Конструктор')
    def click_constructor(self):
        return self.click_element_located(MainFunctionalityLocators.MENU_CONSTRUCTOR)

    @allure.step('Заполнение полей email и пароль, переход по кнопке Вход')
    def fill_email_and_password_and_enter(self, email='', password=''):
        self.wait_for_entrance_page_header_loaded()
        self.enter_email(email)
        self.enter_password(password)
        self.click_enter_button()
        self.check_page()
