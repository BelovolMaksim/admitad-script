import requests
from base64 import b64encode

# Ваши данные для аутентификации
client_id = '2uX4ARWENmasWcC25fz0I7kuZw4h0l'
client_secret = 'akcBDkbFjELx5sNzDZoNuM9tLlc7S8'

# Формируем строку с данными и кодируем её в Base64
credentials = f"{client_id}:{client_secret}"
credentials_b64 = b64encode(credentials.encode()).decode()

# URL для запроса токена
token_url = 'https://api.admitad.com/token/'

# Параметры запроса
data = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'scope': 'advertiser_websites',  # Указываем нужный scope для статистики рекламных кампаний
}

# Заголовки запроса с Basic Authentication
headers = {
    'Authorization': f'Basic {credentials_b64}',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
}

# Отправляем POST-запрос для получения токена
response = requests.post(token_url, data=data, headers=headers)

# Проверяем успешность запроса и выводим результат
if response.status_code == 200:
    token_data = response.json()
    access_token = token_data['access_token']
    token_type = token_data['token_type']
    scope = token_data['scope']
    print(f'Access Token: {access_token}')
    print(f'Token Type: {token_type}')
    print(f'Scope: {scope}')  # Выводим scope
else:
    print(f'Ошибка при запросе: {response.status_code}')
    print(response.text)
