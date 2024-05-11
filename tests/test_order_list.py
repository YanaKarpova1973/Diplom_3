from pages.order_list_page import OrderListPage
from pages.main_functionality_page import MainFunctionalityPage
from pages.personal_cabinet_page import PersonalCabinetPage
import allure
from datas import URLS


class TestOrdersLine:
    @allure.title('Eсли кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_order_opens_order_details_modal(self, driver):
        page = MainFunctionalityPage(driver)
        page.wait_for_main_page_header_loaded()
        page.click_orders_line()
        orders_list = OrderListPage(driver)
        orders_list.wait_for_orders_list_header_loaded()
        orders_list.click_order_by_id()
        assert orders_list.check_order_content()

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_new_order_appears_in_orders_list(self, driver, make_user, create_user_payload):
        entrance_page = MainFunctionalityPage(driver)
        entrance_page.open_page(URLS.ENTRANCE_PAGE_SUBDIRECTORY)
        payload = create_user_payload(name='rand', password='rand', email='rand')
        user = make_user(data=payload)
        entrance_page.fill_email_and_password_and_enter(email=payload["email"], password=payload["password"])
        main_page = MainFunctionalityPage(driver)
        main_page.wait_for_main_page_header_loaded()
        main_page.make_order()
        main_page.wait_for_order_modal_window()
        order_id = main_page.get_order_id_when_created()
        main_page.click_close_modal()
        main_page.click_private_area_button()
        cabinet_page = PersonalCabinetPage(driver)
        cabinet_page.wait_for_profile_header_loaded()
        orders_history = OrderListPage(driver)
        orders_history.click_orders_history()
        orders_history.wait_for_orders_history_loaded()
        assert orders_history.check_order_id_in_orders_history(order_id)
        orders_history.click_orders_list()
        orders_history.wait_for_orders_list_header_loaded()
        assert orders_history.check_order_id_in_orders_line(order_id)

    @allure.title('При создании нового заказа счётчики "Выполнено за всё время" и "Выполнено за сегодня" увеличиваются')
    def test_new_order_increases_total_and_today_orders_counters(self, driver, make_user, create_user_payload):
        entrance_page = MainFunctionalityPage(driver)
        entrance_page.open_page(URLS.ENTRANCE_PAGE_SUBDIRECTORY)
        payload = create_user_payload(name='rand', password='rand', email='rand')
        user = make_user(data=payload)
        entrance_page.fill_email_and_password_and_enter(email=payload["email"], password=payload["password"])
        main_page = MainFunctionalityPage(driver)
        main_page.wait_for_main_page_header_loaded()
        main_page.click_orders_line()
        orders_list = OrderListPage(driver)
        orders_list.wait_for_orders_list_header_loaded()
        total_count = orders_list.get_total_count()
        today_count = orders_list.get_today_count()
        orders_list = OrderListPage(driver)
        orders_list.click_constructor()
        main_page.make_order()
        main_page.wait_for_order_modal_window()
        main_page.click_close_modal()
        main_page.click_orders_line()
        orders_list.wait_for_orders_list_header_loaded()
        new_total_count = orders_list.get_total_count()
        new_today_count = orders_list.get_today_count()
        assert new_total_count > total_count and new_today_count > today_count

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    def test_new_order_appears_in_processing_orders(self, driver, make_user, create_user_payload):
        entrance_page = MainFunctionalityPage(driver)
        entrance_page.open_page(URLS.ENTRANCE_PAGE_SUBDIRECTORY)
        payload = create_user_payload(name='rand', password='rand', email='rand')
        user = make_user(data=payload)
        entrance_page.fill_email_and_password_and_enter(email=payload["email"], password=payload["password"])
        main_page = MainFunctionalityPage(driver)
        main_page.wait_for_main_page_header_loaded()
        main_page.make_order()
        main_page.wait_for_order_modal_window()
        order_id = main_page.get_order_id_when_created()
        main_page.click_close_modal()
        main_page.click_orders_line()
        orders_list = OrderListPage(driver)
        orders_list.wait_for_orders_list_header_loaded()
        assert orders_list.check_order_id_in_processing_orders(order_id)
