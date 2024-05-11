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

    @allure.step('Просмотр заказа из Ленты Заказов')
    def click_order_by_id(self):
        selector = (By.XPATH, OrdersListLocators.FIRST_ORDER)
        self.click_element_located(selector)

    @allure.step('Проверка видимости модального окна')
    def check_order_details_modal_opened(self):
        try:
            self.find_element_located(OrdersListLocators.ORDER_DETAILS_MODAL)
        except NoSuchElementException:
            return False
        return True

    @allure.step('ID заказа из заголовка модального окна')
    def get_order_id_from_modal(self):
        return self.get_text_by_locator(OrdersListLocators.ORDER_DETAILS_MODAL_ORDER_ID_XPATH)

    @allure.step('Проверка наличия ID {order_id} заказа в Ленте заказов')
    def check_order_id_in_orders_line(self, order_id):
        return order_id in self.get_text_by_locator(OrdersListLocators.LIST_OF_ORDERS)

    @allure.step('Проверка отображения состава')
    def check_order_content(self):
        return self.find_element_waiting(OrdersListLocators.ORDERS_CONTENT).is_displayed()

    @allure.step('Переход в Конструктор')
    def click_constructor(self):
        return self.click_element_located(MainFunctionalityLocators.MENU_CONSTRUCTOR)

    @allure.step('Переход в секцию История заказов')
    def click_orders_history(self):
        return self.click_element_located(OrdersListLocators.ORDERS_HISTORY)

    @allure.step('Ожидание загрузки Истории Заказов')
    def wait_for_orders_history_loaded(self):
        self.wait_for_element_loaded(OrdersListLocators.WHOLE_ORDERS_HISTORY)

    @allure.step('Получение значения счетчика Выполнено за все время')
    def get_total_count(self):
        return self.get_text_by_locator(OrdersListLocators.TOTAL_COUNT_XPATH)

    @allure.step('Получение значения счетчика Выполнено за сегодня')
    def get_today_count(self):
        return self.get_text_by_locator(OrdersListLocators.TODAY_COUNT_XPATH)

    @allure.step('Проверка наличия ID {order_id} заказа среди заказов в работе')
    def check_order_id_in_processing_orders(self, order_id):
        return order_id in self.get_text_by_locator(OrdersListLocators.LIST_OF_ORDERS)

    @allure.step('Ожидание загрузки Истории Заказов')
    def wait_for_orders_loaded(self):
        self.wait_for_element_loaded(OrdersListLocators.WHOLE_ORDERS_HISTORY)

    @allure.step('Переход в секцию История заказов')
    def click_orders_history(self):
        return self.click_element_located(OrdersListLocators.ORDERS_HISTORY)

    @allure.step('Проверка наличия ID заказа в Истории заказов')
    def check_order_id_in_orders_history(self, order_id):
        locator = OrdersListLocators.LOCATOR_WITH_CHANGE_CONTAIN.format(order_id)
        try:
            self.find_element_without_xpath(locator)
        except NoSuchElementException:
            return False
        return True

    @allure.step('Переход в Ленту Заказов')
    def click_orders_list(self):
        self.click_element_located(OrdersListLocators.ORDER_LIST)
