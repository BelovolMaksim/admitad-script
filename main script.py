import requests

# access_token
access_token = 'xAi6EfvbBuK2tWDzjbyeh6PURb721b'

# URL для запроса информации о профиле
profile_url = 'https://api.admitad.com/me/'

# Заголовки с авторизацией
headers = {
    'Authorization': f'Bearer {access_token}',
}

try:
    # Отправляем GET-запрос для получения информации о профиле
    response = requests.get(profile_url, headers=headers)

    # Проверяем успешность запроса и выводим результат
    if response.status_code == 200:
        profile_data = response.json()
        # токен действителен, данные профиля здесь
        print('Токен действителен:')
        print(profile_data)
    else:
        print(f'Ошибка при запросе: {response.status_code}')
        print(response.text)
except Exception as e:
    # Вывод сообщения об ошибке
    print(f'Произошла ошибка: {e}')
