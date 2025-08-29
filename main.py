from dotenv import load_dotenv
import os
import requests


def fetch_holidays(token):
    url = "https://calendarific.com/api/v2/holidays"
    params = {"api_key": token, "country": "RU", "year": 2025}
    response = requests.get(url, params)
    response.raise_for_status()
    return response.json()["response"]["holidays"]


def main():
    load_dotenv(".env")
    token = os.getenv("TOKEN")

    holidays = fetch_holidays(token)
    lines = [
        f"Дата: {h['date']['iso']}\n"
        f"Название: {h.get('name', '—')}\n"
        f"Описание: {h.get('description', '—')}\n"
        for h in holidays
    ]
    print("\n".join(lines))


if __name__ == "__main__":
    main()
