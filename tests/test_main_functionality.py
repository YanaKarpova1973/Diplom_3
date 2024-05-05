from pages.main_functionality_page import MainFunctionalityPage
from pages.order_list_page import OrderListPage
import allure
from datas import URLS

class TestMainFunctionality:
    @allure.title('Переход из Личного кабинета в Конструктор')
    def test_redirect_to_constructor(self, driver):
        page = MainFunctionalityPage(driver)
        page.open_page(URLS.ENTRANCE_PAGE_SUBDIRECTORY)
        page.wait_for_entrance_page_header_loaded()
        page.click_constructor()
        main_page = MainFunctionalityPage(driver)
        main_page.wait_for_main_page_header_loaded()
        assert main_page.check_page()

    @allure.title('Переход из Основной страницы в Ленту заказов')
    def test_redirect_to_orders_line(self, driver):
        entrance_page = MainFunctionalityPage(driver)
        entrance_page.open_page(URLS.ENTRANCE_PAGE_SUBDIRECTORY)
        entrance_page.click_constructor()
        entrance_page.check_page()
        main_page = MainFunctionalityPage(driver)
        main_page.wait_for_main_page_header_loaded()
        main_page.click_orders_line()
        order_list = OrderListPage(driver)
        assert order_list.check_page(URLS.ORDER_LINE_SUBDIRECTORY)

    @allure.title('Выбор ингредиента - появление всплывающего окна с деталями')
    def test_click_to_ingredient_opens_details_modal(self, driver):
        page = MainFunctionalityPage(driver)
        page.open_page()
        page.wait_for_main_page_header_loaded()
        page.click_first_ingredient()
        assert page.check_modal_opened()

    @allure.title('Всплывающее окно с деталями можно закрыть нажатием на знак "х"')
    def test_click_to_x_closes_ingredient_popup(self, driver):
        page = MainFunctionalityPage(driver)
        page.open_page()
        page.wait_for_main_page_header_loaded()
        page.click_first_ingredient()
        page.wait_modal_header_loaded()
        page.click_close_modal()
        assert not page.check_modal_opened()

    @allure.title('Добавление ингредиента в заказы увеличивает счетчик этого ингредиента')
    def test_drag_and_drop_ingredient_to_basket_increases_ingredient_count(self, driver):
        page = MainFunctionalityPage(driver)
        initial_value = page.get_first_ingredient_counter_value()
        page.drag_n_drop_first_ingredient_to_basket()
        updated_value = page.get_first_ingredient_counter_value()
        assert initial_value < updated_value

    @allure.title('Авторизованный пользователь может оформить заказ')
    def test_logged_in_user_can_make_order(self, driver, make_user, create_user_payload):
        entrance_page = MainFunctionalityPage(driver)
        entrance_page.open_page(URLS.ENTRANCE_PAGE_SUBDIRECTORY)
        payload = create_user_payload(name='rand', password='rand', email='rand')
        user = make_user(data=payload)
        entrance_page.fill_email_and_password_and_enter(email=payload["email"], password=payload["password"])
        page = MainFunctionalityPage(driver)
        page.wait_for_main_page_header_loaded()
        page.check_make_order_button()
        page.drag_n_drop_first_ingredient_to_basket()
        page.click_make_order()
        assert page.check_modal_opened()
