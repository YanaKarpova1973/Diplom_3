from pages.main_functionality_page import MainFunctionalityPage
from pages.recovery_password_page import RecoveryPasswordPage
import allure
from datas import URLS

class TestPasswordRecovery:
    @allure.title('Переходим на страницу восстановления пароля по кнопке Восстановить пароль ')
    def test_password_recovery_transfer_to_recovery_page(self, driver):
        page = MainFunctionalityPage(driver)
        page.open_page(subdir=URLS.ENTRANCE_PAGE_SUBDIRECTORY)
        page.wait_for_entrance_page_header_loaded()
        page.click_restore_password()
        password_recovery_page = RecoveryPasswordPage(driver)
        password_recovery_page.wait_for_recovery_page_header_loaded()
        assert password_recovery_page.check_page(subdir=URLS.RECOVER_PASSWORD_SUBDIRECTORY)

    @allure.title('Ввод почты и переход по кнопке «Восстановить»')
    def test_password_reset_for_valid_email(self, driver, make_user, create_user_payload):
        payload = create_user_payload(name='rand', password='rand', email='rand')
        user = make_user(data=payload)
        password_recovery_page = RecoveryPasswordPage(driver)
        password_recovery_page.open_page(subdir=URLS.RECOVER_PASSWORD_SUBDIRECTORY)
        password_recovery_page.wait_for_recovery_page_header_loaded()
        email = payload["email"]
        password_recovery_page.enter_email(email)
        password_recovery_page.recover_button_click()
        password_recovery_page.wait_for_recovery_page_header_loaded()
        assert password_recovery_page.check_page(subdir=URLS.RECOVER_PASSWORD_SUBDIRECTORY)

    @allure.title('Нажатие по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_password_reset_gets_highlighted_field(self, driver, make_user, create_user_payload):
        password_recovery_page = RecoveryPasswordPage(driver)
        password_recovery_page.open_page(URLS.RECOVER_PASSWORD_SUBDIRECTORY)
        password_recovery_page.wait_for_recovery_page_header_loaded()
        payload = create_user_payload(name='rand', password='rand', email='rand')
        user = make_user(data=payload)
        email = payload["email"]
        password_recovery_page.enter_email(email)
        password_recovery_page.recover_button_click()
        password_recovery_page.wait_for_recovery_page_header_loaded()
        password_recovery_page.check_page(subdir=URLS.RESET_PASSWORD_SUBDIRECTORY)
        password_recovery_page.button_password_click()
        assert password_recovery_page.password_checking()
