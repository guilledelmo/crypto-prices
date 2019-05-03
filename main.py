import requests
from datetime import time
import tkinter
import json

def get_prices():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {'start':'1', 'limit':'5', 'convert':'USD'}
    headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': 'KEY'}
    session = requests.Session()
    session.headers.update(headers)
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    return data


data = get_prices()

main_win = tkinter.Tk()
main_win.title("Crypto prices")
title_label = tkinter.Label(main_win, text="Crypto top 5", font=("Helvetica", 20))
title_label.pack()
first_label_id = tkinter.Label(main_win, text=data["data"][0]["id"], font=("Helvetica", 12))
first_label_id.pack()
first_label_name = tkinter.Label(main_win, text=data["data"][0]["name"], font=("Helvetica", 12))
first_label_name.pack()
first_label_price = tkinter.Label(main_win, text=data["data"][0]["quote"]["USD"]["price"], font=("Helvetica", 12))
first_label_price.pack()
first_label_change = tkinter.Label(main_win, text=str(data["data"][0]["quote"]["USD"]["percent_change_24h"]) + "%", font=("Helvetica", 12))
first_label_change.pack()
win_timestamp = tkinter.Label(main_win, text=data["status"]["timestamp"], font=("Helvetica", 8))
win_timestamp.pack()
main_win.mainloop()
# TODO: Refresh button that refreshes the window so that the labels need to call the function again to get the data, which should then be updated
