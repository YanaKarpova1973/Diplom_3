from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from datas import URLS
from selenium.webdriver.common.by import By
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открытие страницы по URL')
    def open_page(self, subdir=''):
        url = URLS.MAIN_PAGE_URL+subdir
        return self.driver.get(url)

    @allure.step('Проверка текущей ссылки')
    def check_page(self, subdir=''):
        combined_url = URLS.MAIN_PAGE_URL + subdir
        return self.driver.current_url == combined_url

    @allure.step('Ожидание загрузки заголовка страницы')
    def wait_for_element_loaded(self, locator, time=50):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Поиск элемента по локатору')
    def find_element_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator),
                                                      message=f'Element not found in {locator}')

    @allure.step('Поиск элемента с ожиданием')
    def find_element_waiting(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Поиск элемента c локатором без XPATH')
    def find_element_without_xpath(self, locator):
        return self.driver.find_element(By.XPATH, locator)

    @allure.step('Ввод текста в элемент')
    def send_keys_to_element_located(self, locator, keys=None):
        self.find_element_located(locator)
        self.find_element_located(locator).send_keys(keys)

    @allure.step('Нажать на элемент')
    def click_element_located(self, locator):
        return self.find_element_located(locator).click()

    @allure.step('Получение текста элемента по локатору')
    def get_text_by_locator(self, locator):
        return self.find_element_located(locator).text

    @allure.step('Получение текста элемента по локатору')
    def get_id_by_locator(self, locator):
        return self.driver.find_element(By.XPATH, locator).text

    @allure.step('Драг-н-дроп элемента на элемент')
    def do_drag_n_drop(self, source, target):
        drag = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(source))
        drop = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(target))
        ActionChains(self.driver).drag_and_drop(drag, drop).perform()

    @allure.step('Ожидание исчезновения элемента')
    def wait_until_element_not_present(self, locator, time=50):
        return WebDriverWait(self.driver, time).until(expected_conditions.invisibility_of_element_located(locator))
