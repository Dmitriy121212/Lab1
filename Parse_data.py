import requests
import csv
from datetime import datetime, timedelta

# Функція для отримання курсу з API НБУ
def get_exchange_rate(date):
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&date={date}&json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]["rate"]
    return None

def get_usd_to_uah_rates(year):
    start_date = datetime(year, 1, 1)
    end_date = datetime(year, 12, 9)
    current_date = start_date

    rates = []
    while current_date <= end_date:
        date_str = current_date.strftime("%Y%m%d")
        rate = get_exchange_rate(date_str)
        if rate is not None:
            rates.append({"date": current_date.strftime("%Y-%m-%d"), "rate": rate})
        current_date += timedelta(days=1)

    # Збереження даних у CSV
    with open("usd_to_uah_rates.csv", "w", newline="") as csvfile:
        fieldnames = ["date", "rate"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rates)

    print(f"Дані збережено в usd_to_uah_rates.csv")

# Виклик функції
get_usd_to_uah_rates(2024)
