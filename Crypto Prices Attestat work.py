import requests
import  json
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


def update_cript_label(event):
    code = cript_combobox.get()
    name = cript[code]
    cript_label.config(text=name)


def update_currency_label(event):
    code = currency_combobox.get()
    name = currency[code]
    currency_label.config(text=name)


def exchange():
    cript_code = cript_combobox.get().lower()
    currency_code = currency_combobox.get().lower()

    if cript_code and currency_code:
        try:
            response = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={cript_code}&vs_currencies={currency_code}") # Для получения данных с сервера используется метод `get` библиотеки requests
            response.raise_for_status() # метод `raise_for_status()` в библиотеке requests  Устанавливает статус-код ответа
            data = response.json() # раскладываем в виде обычного python словаря

            if cript_code in data:
                exchange_rate = data[cript_code][currency_code]
                cript_name = cript[cript_code]
                currency_name = currency[currency_code]
                mb.showinfo("Курс обмена", f"Курс: {exchange_rate:.2f} {currency_name} за один {cript_name}")
            else:
                mb.showerror("Ошибка", f"Валюта {cript_code} не найдена!")
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}.")
    else:
        mb.showwarning("Внимание", "Введите код валюты")


currency ={
    'rub': "Российский рубль",
    'EUR': "Евро",
    'GBP': "Британский фунт стерлингов",
    'JPY': "Японская йена",
    'CNY': "Китайский юань",
    'KZT': "Казахский тенге",
    'UZS': "Узбекская сум",
    'CHF': "Швейцарский франк",
    'AED': "Дирхам ОАЭ",
    'CAD': "Канадский доллар",
    'USD': "Американский доллар"
}

cript = {
    "bitcoin": 'BTC',
    "litecoin": 'LTC'
}

window = Tk()
window.title("Курсы обмена криптовалют")
window.geometry("360x300")

Label(text="Базовая валюта").pack(padx=10, pady=10)
currency_combobox = ttk.Combobox(values=list(currency.keys())) # Combobox  виджет в tkinter используется для создания выпадающего списка
currency_combobox.pack(padx=10, pady=10)
currency_combobox.bind("<<ComboboxSelected>>", update_currency_label) # bind()  метод tkinter используется для привязки события к виджету
currency_label = ttk.Label()
currency_label.pack(padx=10, pady=10) # метод `pack()` в tkinter размещает виджеты в окне

Label(text="Криптовалюта").pack(padx=10, pady=10)

cript_combobox = ttk.Combobox(values=list(cript.keys()))
cript_combobox.pack(padx=10, pady=10)
cript_combobox.bind("<<ComboboxSelected>>", update_cript_label)

cript_label = ttk.Label()
cript_label.pack(padx=10, pady=10)

Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)

window.mainloop()



# result = requests.get('https://open.er-api.com/v6/latest/USD')
# data = json.loads(result.text)
# p = pprint.PrettyPrinter(indent=4)
# p.pprint(data)