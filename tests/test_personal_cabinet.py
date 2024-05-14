from pages.personal_cabinet_page import PersonalCabinetPage
from pages.main_functionality_page import MainFunctionalityPage
import allure
from datas import URLS

class TestPrivateArea:
    @allure.title('Переход в Личный Кабинет')
    def test_main_page_route_to_private_area(self, driver, make_user, create_user_payload):
        page = MainFunctionalityPage(driver)
        page.open_page(URLS.ENTRANCE_PAGE_SUBDIRECTORY)
        payload = create_user_payload(name='rand', password='rand', email='rand')
        user = make_user(data=payload)
        page.wait_for_entrance_page_header_loaded()
        page.enter_email(payload["email"])
        page.enter_password(payload["password"])
        page.click_enter_button()
        page.check_page()
        page.wait_for_main_page_header_loaded()
        page.click_private_area_button()
        cabinet_page = PersonalCabinetPage(driver)
        cabinet_page.wait_for_profile_header_loaded()
        assert cabinet_page.check_page(URLS.PROFILE_PAGE_SUBDIRECTORY)

    @allure.title('Переход из Личного кабинета в Историю Заказов')
    def test_private_area_route_to_history(self, driver, make_user, create_user_payload):
        page = MainFunctionalityPage(driver)
        page.open_page(URLS.ENTRANCE_PAGE_SUBDIRECTORY)
        payload = create_user_payload(name='rand', password='rand', email='rand')
        user = make_user(data=payload)
        page.fill_email_and_password_and_enter(email=payload["email"], password=payload["password"])
        page.wait_for_main_page_header_loaded()
        page.click_private_area_button()
        page.check_page(URLS.PROFILE_PAGE_SUBDIRECTORY)
        cabinet_page = PersonalCabinetPage(driver)
        cabinet_page.wait_for_profile_header_loaded()
        cabinet_page.check_page(URLS.PROFILE_PAGE_SUBDIRECTORY)
        cabinet_page.click_orders_history_section_name()
        assert page.check_page(URLS.ORDER_HISTORY_SUBDIRECTORY)

    @allure.title('Выход из аккаунта - из Личного кабинета')
    def test_account_logout(self, driver, make_user, create_user_payload):
        page = MainFunctionalityPage(driver)
        page.open_page(URLS.ENTRANCE_PAGE_SUBDIRECTORY)
        payload = create_user_payload(name='rand', password='rand', email='rand')
        user = make_user(data=payload)
        page.fill_email_and_password_and_enter(email=payload["email"], password=payload["password"])
        page.wait_for_main_page_header_loaded()
        page.click_private_area_button()
        page.check_page(URLS.PROFILE_PAGE_SUBDIRECTORY)
        cabinet_page = PersonalCabinetPage(driver)
        cabinet_page.wait_for_profile_header_loaded()
        cabinet_page.check_page(URLS.PROFILE_PAGE_SUBDIRECTORY)
        cabinet_page.click_exit()
        page.check_page(URLS.ENTRANCE_PAGE_SUBDIRECTORY)
        page.wait_for_entrance_page_header_loaded()
        page.click_constructor()
        page.check_page()
        page.wait_for_main_page_header_loaded()
        assert page.check_enter_account_button()
