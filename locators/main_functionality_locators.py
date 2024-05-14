from selenium.webdriver.common.by import By

class MainFunctionalityLocators:

    MAIN_PAGE_HEADER = (By.XPATH, ".//h1[text()='Соберите бургер']")  # Заголовок на главной странице
    PRIVATE_AREA = (
    By.XPATH, "//p[text() = 'Личный Кабинет']")  # Главная страница, кнопка перехода в Личный кабинет
    BUTTON_MAKE_ORDER = (By.XPATH, "//button[contains(@class ,'button_button__33qZ0 button_button_type_primary__1O7Bx')]")
    BUTTON_ENTER_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка Войти в аккаунт на гл. странице
    MENU_CONSTRUCTOR = (By.XPATH, "//p[text() = 'Конструктор']")  # Кнопка Конструктор на хедере главной страницы
    ORDER_LINE = (By.XPATH, "//p[text() = 'Лента Заказов']")  # Кнопка Лента Заказов на хедере главной страницы
    FIRST_INGREDIENT = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient_')][1]")
    FIRST_INGREDIENT_COUNTER_XPATH = (By.XPATH, "//ul[1]/a[1]//p[contains(@class, 'num')]")
    FIRST_INGREDIENT_COUNTER = (By.XPATH, "//p[contains(@class, 'counter_counter')][1]")
    INGREDIENT_MODAL_XPATH = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened_')]")
    INGREDIENT_MODAL_NOT_XPATH = "//section[contains(@class, 'Modal_modal_opened_')]"
    CLOSE_MODAL = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    INGREDIENT_MODAL_HEADER = (By.XPATH, "//h2[text()='Детали ингредиента']")
    BASKET = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")  # Общий локатор для корзины
    TEMPORARY_ORDER_MODAL_HEADER = (By.XPATH, "//h2[text()='9999']")
    ORDER_ID_XPATH = "//h2[contains(@class, 'Modal_modal__title')]"
    ORDER_IDENTIFIER = (By.XPATH,"//p[text()='идентификатор заказа']")
    ENTRANCE_HEADER = (By.XPATH, ".//h2[text()='Вход']")  # Заголовок формы логина
    BUTTON_RESTORE_PASSWORD = (By.XPATH, "//a[text()='Восстановить пароль']")  # Гиперссылка для восстановления пароля
    EMAIL_INPUT_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::*")  # Поле ввода e-mail
    PASSWORD_INPUT_FIELD = (By.XPATH, "//label[text()='Пароль']/following-sibling::*")  # Поле ввода пароля
    BUTTON_ENTER = (By.XPATH, "//button[text()='Войти']")  # Кнопка входа на форме логина

