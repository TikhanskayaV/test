import sender_stand_request
import data


# Функция для изменения значения в параметре name в теле запроса
def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body


# Функция для позитивной проверки
def positive_assert(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    assert kit_response.status_code == 201

    assert kit_response.json()["name"] != ""


# Функция для негативной проверки
def negative_assert_code_400(name):
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(kit_body)

    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "Не все необходимые параметры были переданы"


# Тест 1. Успешное создание набора. Параметр name состоит из 1 символа

def test_main_kits_1_letter_in_name_get_success_response():
    positive_assert("a")


# Тест 2. Успешное создание набора. Параметр name состоит из 511 символов

def test_main_kits_511_letter_in_name_get_success_response():
    positive_assert(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


# Тест 3. Количество символов параметра name меньше допустимого (0)

def test_main_kits_0_letter_in_name_error_response():
    negative_assert_code_400("")


# Тест 4. Количество символов параметра name меньше допустимого (512)

def test_main_kits_512_letter_in_name_error_response():
    negative_assert_code_400(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


# Тест 5. Разрешены английские буквы в параметре name

def test_main_kits_english_letters_in_name_get_success_response():
    positive_assert("QWErty")


# Тест 6. Разрешены русские буквы в параметре name

def test_main_kits_russian_letters_in_name_get_success_response():
    positive_assert("Мария")


# Тест 7. Разрешены спецсимволы в параметре name

def test_main_kits_special_letters_in_name_get_success_response():
    positive_assert("\"N%@\",")


# Тест 8. Разрешены пробелы в параметре name

def test_main_kits_spaces_in_name_get_success_response():
    positive_assert(" Человек и КО ")


# Тест 9. Разрешены цифры в параметре name

def test_main_kits_numbers_in_name_get_success_response():
    positive_assert("123")


# Тест 10. Параметр name не передан в запросе

def test_main_kits_null_in_name_error_response():
    negative_assert_code_400(None)


# Тест 11. Передан другой тип параметра name (число)
def test_main_kits_other_type_in_name_error_response():
    negative_assert_code_400(123)
