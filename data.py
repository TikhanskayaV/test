headers = {
    "Content-Type": "application/json"
}
headers_for_kit = {
    "Content-Type": "application/json",
    "Authorization": "Bearer {authToken}"
}

user_body = {
    "firstName": "Анатолий",  # Имя пользователя
    "phone": "+79995553322",  # Контактный телефон пользователя
    "address": "г. Москва, ул. Пушкина, д. 10"  # Адрес пользователя
}
kit_body = {
    "cardId": "1",
    "name": "Мой набор"
}