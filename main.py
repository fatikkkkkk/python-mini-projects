import requests
from datetime import datetime

URL = "https://open.er-api.com/v6/latest/USD"

def get_exchange_rates():
    response = requests.get(URL)
    response.raise_for_status()
    data = response.json()
    return data["rates"]

if __name__ == "__main__":
    rates = get_exchange_rates()

    print("📅 Tarih:", datetime.now().strftime("%d-%m-%Y"))
    print("💱 Güncel Döviz Kurları (USD bazlı):\n")

    for currency in ["TRY", "EUR", "GBP"]:
        print(f"{currency}: {rates[currency]}")
