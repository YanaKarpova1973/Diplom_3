from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure
from locators.order_list_locators import OrdersListLocators
from locators.main_functionality_locators import MainFunctionalityLocators


class OrderListPage(BasePage):

    @allure.step('Ожидание загрузки заголовка страницы Ленты Заказов')
    def wait_for_orders_list_header_loaded(self):
        self.wait_for_element_loaded(OrdersListLocators.ORDER_LINE_HEADER)

    @allure.step('Получение ID первого заказа')
    def get_first_order_id(self):
        return self.driver.find_element(By.XPATH, OrdersListLocators.FIRST_ORDER[1]).text

    @allure.step('Заказ Ленты Заказов по номеру {order_id}')
    def click_order_by_id(self, order_id):
        locator = f"//p[text()='{order_id}']"
        selector = (By.XPATH, locator)
        self.click_element_located(selector)

    @allure.step('Проверка видимости модального окна')
    def check_order_details_modal_opened(self):
        try:
            self.driver.find_element(By.XPATH, OrdersListLocators.ORDER_DETAILS_MODAL)
        except NoSuchElementException:
            return False
        return True

    @allure.step('ID заказа из заголовка модального окна')
    def get_order_id_from_modal(self):
        return self.driver.find_element(By.XPATH, OrdersListLocators.ORDER_DETAILS_MODAL_ORDER_ID_XPATH).text

    @allure.step('Проверка наличия ID {order_id} заказа в Ленте заказов')
    def check_order_id_in_orders_line(self, order_id):
        locator = f"//p[contains(text(), '{order_id}')]"
        try:
            self.driver.find_element(By.XPATH, locator)
        except NoSuchElementException:
            return False
        return True

    @allure.step('Переход в Конструктор')
    def click_constructor(self):
        return self.click_element_located(MainFunctionalityLocators.MENU_CONSTRUCTOR)

    @allure.step('Получение значения счетчика Выполнено за все время')
    def get_total_count(self):
        return self.driver.find_element(By.XPATH, OrdersListLocators.TOTAL_COUNT_XPATH).text

    @allure.step('Получение значения счетчика Выполнено за сегодня')
    def get_today_count(self):
        return self.driver.find_element(By.XPATH, OrdersListLocators.TODAY_COUNT_XPATH).text

    @allure.step('Проверка наличия ID {order_id} заказа среди заказов в работе')
    def check_order_id_in_processing_orders(self, order_id):
        locator = f"//li[text()='{order_id}']"
        try:
            self.driver.find_element(By.XPATH, locator)
        except NoSuchElementException:
            return False
        return True

    @allure.step('Ожидание загрузки первого заказа из Ленты Заказов')
    def wait_for_orders_loaded(self):
        self.wait_for_element_loaded(OrdersListLocators.FIRST_ORDER)

    @allure.step('Проверка наличия ID заказа в Истории заказов')
    def check_order_id_in_orders_history(self, order_id):
        locator = f"//p[contains(text(), '{order_id}')]"
        try:
            self.driver.find_element(By.XPATH, locator)
        except NoSuchElementException:
            return False
        return True

    @allure.step('Переход в Ленту Заказов')
    def click_orders_list(self):
        self.click_element_located(MainFunctionalityLocators.ORDER_LINE)
