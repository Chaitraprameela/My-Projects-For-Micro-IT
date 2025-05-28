import requests

def currency_converter():
    base_currency = input("Enter base currency (e.g., USD): ").upper()
    target_currency = input("Enter target currency (e.g., INR): ").upper()
    amount = float(input(f"Enter amount in {base_currency}: "))

    try:
        # Fetch exchange rate
        url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
        response = requests.get(url)
        data = response.json()

        if "rates" in data and target_currency in data["rates"]:
            rate = data["rates"][target_currency]
            converted = amount * rate
            print(f"{amount:.2f} {base_currency} = {converted:.2f} {target_currency}")
        else:
            print("❌ Invalid currency code.")

    except Exception as e:
        print("Error fetching exchange rates:", e)

currency_converter()
