from selenium.webdriver.common.by import By

class OrdersListLocators:

    ORDER_LINE_HEADER = (By.XPATH, ".//h1[text()='Лента заказов']")  # Хедер страницы ленты заказов
    ORDER_LIST = (By.XPATH, "//p[text() = 'Лента Заказов']")  # Кнопка Лента Заказов на хедере главной страницы
    LIST_OF_ORDERS = (By.XPATH, "//main[@class='App_componentContainer__2JC2W']//div")
    LOCATOR_WITH_CHANGE_TEXT = "//p[text()='{}']"
    LOCATOR_WITH_CHANGE_CONTAIN = "//p[contains(text(), '{}')]"
    WHOLE_ORDERS_HISTORY = (By.XPATH, "//ul[@class='OrderHistory_profileList__374GU OrderHistory_list__KcLDB']")
    FIRST_ORDER = ".//li[contains(@class, 'OrderHistory_listItem')]/a/div/p[contains(@class, 'text_type_digits')]"
    ORDER_DETAILS_MODAL = (By.XPATH, ".//div[contains(@class, 'Modal_orderBox')]")
    ORDER_DETAILS_MODAL_ORDER_ID_XPATH = (By.XPATH, ".//div[contains(@class, 'Modal_orderBox')]/p")
    ORDERS_HISTORY = (By.XPATH, "//a[text()='История заказов']")  # Кнопка секции истории заказов
    TOTAL_COUNT_XPATH = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_COUNT_XPATH = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    FIRST_ORDERS_HISTORY_ORDER = (By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem')]/a/div/p[contains(@class, "
                        "'text_type_digits')]")
    CREATED_ORDER_NUMBER = [By.XPATH, "//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']"]
    MAKED_ORDER = (By.XPATH, "//p[contains(@class,'OrderFeed_number__2MbrQ text')]")
    ORDERS_CONTENT = By.XPATH, '//p[text()="Cостав"]'
