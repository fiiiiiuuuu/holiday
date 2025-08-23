from dotenv import load_dotenv
import os
import requests

def get_data(api_key):
    url = 'https://calendarific.com/api/v2/holidays'
    params = {
        'api_key': api_key,
        'country': 'RU',
        'year': 2025
    }
    response = requests.get(url, params)
    response.raise_for_status()
    data = response.json()
    return data

def main():
    load_dotenv('.env')
    api_key = os.getenv('TOKEN')

    holidays = get_data(api_key)['response']['holidays']
    for holiday in holidays:
        name = holiday.get('name', 'no name')
        description = holiday.get('description', 'no desc')
        date = holiday.get('date', {}).get('iso', 'no date')
        print(f'Дата: {date}')
        print(f'Название: {name}')
        print(f'Описание: {description}')
        print()

if __name__ == '__main__':
    main()