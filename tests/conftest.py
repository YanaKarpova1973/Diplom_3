import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from faker import Faker
from datas import UserRequests, URLS

fake = Faker()

@pytest.fixture(scope='function', params=['chrome', 'firefox'])
def driver(request):
    driver = None
    if request.param == 'chrome':
        chrome_options = Options()
        chrome_options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=chrome_options)
    elif request.param == 'firefox':
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    driver.get(URLS.MAIN_PAGE_URL)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def make_user():
    user = {}

    def _make_user(data):
        nonlocal user
        user_requests = UserRequests()
        user = user_requests.post_create_user(data=data)
        return user

    yield _make_user
    UserRequests().delete_user(token=user['accessToken'])

@pytest.fixture      # Создание payload для пользователя
def create_user_payload():

    def _create_user_payload(name=None, email=None, password=None):
        payload = {}
        if name == 'rand':
            payload["name"] = fake.name()
        elif name is not None:
            payload["name"] = name
        if password == 'rand':
            payload["password"] = fake.name()
        elif password is not None:
            payload["password"] = password
        if email == 'rand':
            payload["email"] = fake.email()
        elif email is not None:
            payload["email"] = email
        return payload
    return _create_user_payload
