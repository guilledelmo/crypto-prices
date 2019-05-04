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

def show_labels():
    for i in range(5):
        tkinter.Label(main_win, text=data["data"][i]["id"], font=("Helvetica, 12")).grid(row=i+1, column=0)
        tkinter.Label(main_win, text=data["data"][i]["name"], font=("Helvetica, 12")).grid(row=i+1, column=1)
        tkinter.Label(main_win, text="%.2f" % data["data"][i]["quote"]["USD"]["price"], font=("Helvetica, 12")).grid(row=i+1, column=2)
        tkinter.Label(main_win, text=str(data["data"][i]["quote"]["USD"]["percent_change_24h"]) + "%", font=("Helvetica, 12")).grid(row=i+1, column=3)
    win_timestamp = tkinter.Label(main_win, text=data["status"]["timestamp"], font=("Helvetica", 8))
    win_timestamp.grid(row=6, column=2, columnspan=2)
data = get_prices()

main_win = tkinter.Tk()
main_win.title("Crypto prices")
title_label = tkinter.Label(main_win, text="Crypto top 5", font=("Helvetica", 20))
title_label.grid(row=0, column=0, columnspan=4)
show_labels()
refresh_button = tkinter.Button(main_win, text="Refresh", command=show_labels).grid(row=6, column=0, columnspan=2)
main_win.mainloop()
# TODO: Refresh button that refreshes the window so that the labels need to call the function again to get the data, which should then be updated
