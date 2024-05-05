from selenium.webdriver.common.by import By

class OrdersListLocators:
    ORDER_LINE_HEADER = (By.XPATH, ".//h1[text()='Лента заказов']")  # Хедер страницы ленты заказов
    FIRST_ORDER = (By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem')]/a/div/p[contains(@class, "
                             "'text_type_digits')]")
    ORDER_DETAILS_MODAL = ".//div[contains(@class, 'Modal_orderBox')]"
    ORDER_DETAILS_MODAL_ORDER_ID_XPATH = ".//div[contains(@class, 'Modal_orderBox')]/p"
    TOTAL_COUNT_XPATH = "//p[text()='Выполнено за все время:']/following-sibling::p"
    TODAY_COUNT_XPATH = "//p[text()='Выполнено за сегодня:']/following-sibling::p"
    FIRST_ORDERS_HISTORY_ORDER = (
        By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem')]/a/div/p[contains(@class, "
                  "'text_type_digits')]")

