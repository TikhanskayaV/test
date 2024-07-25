import data
import requests
import configuration


# Создание пользователя и получение токена
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


response = post_new_user(data.user_body)
authToken = response.json()["authToken"]
print(response.status_code)
print(response.json())

# Создание набора
def post_new_client_kit(authToken):
    return requests.post(configuration.URL_SERVICE + configuration.MAIN_KITS,
                         json=data.kit_body,
                         headers=data.headers_for_kit)


response = post_new_client_kit(authToken)
print(response.status_code)
print(response.json())
