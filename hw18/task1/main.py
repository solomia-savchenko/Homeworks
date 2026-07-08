from flask import Flask, jsonify
import requests

app = Flask(__name__)


@app.route("/crypto")
def crypto():
    currency_url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
    currency_data = requests.get(currency_url).json()

    rates = {}

    for item in currency_data:
        if item["cc"] in ["USD", "EUR", "GBP"]:
            rates[item["cc"]] = item["rate"]

    btc_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=uah"
    btc_data = requests.get(btc_url).json()

    btc_uah = btc_data["bitcoin"]["uah"]

    result = {
        "USD": f"{btc_uah / rates['USD']:.2f}",
        "EUR": f"{btc_uah / rates['EUR']:.2f}",
        "GBP": f"{btc_uah / rates['GBP']:.2f}"
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)