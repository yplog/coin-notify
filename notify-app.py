from bs4 import BeautifulSoup
import requests
import notify2
import time


while True:

    COIN_LIST = {
        'BTC': 'https://coinmarketcap.com/currencies/bitcoin/',
        'ETH': 'https://coinmarketcap.com/currencies/ethereum/'
    }

    ICON_PATH = "bitcoin-1813507_640.png"

    def fetch_coin():
        coin_li = []

        for k, v in COIN_LIST.items():
            coin_name = k
            url = v

            coin_file = requests.get(url)

            soup = BeautifulSoup(coin_file.text, "html.parser")

            qp = soup.find(id="quote_price")
            cp = qp.text
            coin_li.append(coin_name)
            coin_li.append(cp)

        return coin_li


    def notify():
        coin = fetch_coin()
        notify2.init("BTC ETH")
        n = notify2.Notification("BTC ETH Notifier", icon=ICON_PATH)
        n.set_urgency(notify2.URGENCY_NORMAL)
        n.set_timeout(10000)

        result = " ".join(coin)
        n.update("Current Price", result)
        n.show()

    notify()
    
    time.sleep(60*30)
