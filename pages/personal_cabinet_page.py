import allure
from pages.base_page import BasePage
from locators.personal_cabinet_locators import PersonalCabinetLocators

class PersonalCabinetPage(BasePage):

    @allure.step('Переход в секцию История заказов')
    def click_orders_history_section_name(self):
        return self.click_element_located(PersonalCabinetLocators.ORDERS_HISTORY_AREA)

    @allure.step('Ожидание загрузки заголовка секции Профиль')
    def wait_for_profile_header_loaded(self):
        return self.wait_for_element_loaded(PersonalCabinetLocators.PROFILE_AREA)

    @allure.step('Выход из аккаунта')
    def click_exit(self):
        return self.click_element_located(PersonalCabinetLocators.BUTTON_EXIT_ACCOUNT)
