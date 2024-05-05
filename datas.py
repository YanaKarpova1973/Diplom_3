import requests
import allure

class URLS:
    MAIN_PAGE_URL = "https://stellarburgers.nomoreparties.site/"
    ENTRANCE_PAGE_SUBDIRECTORY = 'login'
    RECOVER_PASSWORD_SUBDIRECTORY = 'forgot-password'
    RESET_PASSWORD_SUBDIRECTORY = 'reset-password'
    PROFILE_PAGE_SUBDIRECTORY = 'account/profile'
    ORDER_HISTORY_SUBDIRECTORY = 'account/order-history'
    ORDER_LINE_SUBDIRECTORY = 'feed'

class BaseRequests:
    host = URLS.MAIN_PAGE_URL

    def exec_post_request(self, url, data):
        response = requests.post(url=url, data=data)
        if 'application/json' in response.headers['Content-Type']:
            return response.json()
        else:
            return response.text

    def exec_delete_request(self, url, token):
        headers = {"Content-Type": "application/json", 'authorization': token}
        response = requests.delete(url=url, headers=headers)
        if 'application/json' in response.headers['Content-Type']:
            return response.json()
        else:
            return response.text

class UserRequests(BaseRequests):
    user_handler = 'api/auth/register'
    manipulate_user_handler = 'api/auth/user'

    @allure.step('Создаем пользователя, отправив запрос POST')
    def post_create_user(self, data=None):
        url = f"{self.host}{self.user_handler}"
        return self.exec_post_request(url, data=data)

    @allure.step('Удаляем пользователя, отправив запрос DELETE')
    def delete_user(self, token=None):
        url = f"{self.host}{self.manipulate_user_handler}"
        return self.exec_delete_request(url, token=token)
