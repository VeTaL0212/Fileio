import requests
import  json
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


def update_cript_label(event):
    code = cript_combobox.get()
    name = cript[code]
    cript_label.config(text=name)


def update_currency1_label(event):
    code = currency1_combobox.get()
    name = currency[code]
    currency1_label.config(text=name)


def update_currency2_label(event):
    code = currency2_combobox.get()
    name = currency[code]
    currency2_label.config(text=name)


def exchange():
    cript_code = cript_combobox.get()
    cript_name = cript[cript_code].lower()
    currency1_code = currency1_combobox.get().lower()
    currency2_code = currency2_combobox.get().lower()

    if cript_code and currency1_code and currency2_code:
        try:
            response = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={cript_name}&vs_currencies={currency1_code},{currency2_code}") # Для получения данных с сервера используется метод `get` библиотеки requests
            response.raise_for_status() # метод `raise_for_status()` в библиотеке requests  Устанавливает статус-код ответа
            data = response.json() # раскладываем в виде обычного python словаря

            if cript_name in data:
                exchange1_rate = data[cript_name][currency1_code]
                exchange2_rate = data[cript_name][currency2_code]
                cript_name = cript_name.capitalize()
                currency1_name = currency[currency1_code.upper()]
                currency2_name = currency[currency2_code.upper()]
                exchange_label.config(text=f"Текущий курс:\n {exchange1_rate:.1f} {currency1_name} за один {cript_name}\n{exchange2_rate:.1f} {currency2_name} за один {cript_name}")
            else:
                mb.showerror("Ошибка", f"Валюта {cript_code} не найдена!")
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}.")
    else:
        mb.showwarning("Внимание", "Введите код валюты")


currency ={
    'USD':'Американский доллар',
    'EUR':'Евро',
    'RUB':'Российский рубль',
    'JPY':'Японская йена',
    'GBP':'Фунт стерлингов',
    'AUD':'Австралийский доллар',
    'ARS':'Аргентийский песо',
    'AED':'Дирхам (ОАЭ)',
    'BDT':'Бангладешская така',
    'BHD':'Динар (Бахрейн)',
    'BMD':'Бермудский доллар',
    'BRL':'Бразильский реал',
    'CAD':'Канадский доллар',
    'CHF':'Швейцарский франк',
    'CLP':'Чилийское песо',
    'CNY':'Китайский юань',
    'CZK':'Чешская крона',
    'DKK':'Датская крона',
    'GEL':'Грузинский лари',
    'HKD':'Гонконгский доллар',
    'HUF':'Форинт (Венгрия)',
    'IDR':'Рупия (Индонезия)',
    'ILS':'Новый израильский шекель',
    'INR':'Индийская рупия',
    'KRW':'Вон (Южная Корея)',
    'KWD':'Кувейтский динар',
    'LKR':'Рупия (Шри-Ланка)',
    'MMK':'Кьят (Мьянма)',
    'MXN':'Мексиканский песо',
    'MYR':'Малайзийский рингит',
    'NGN':'Нигерийская найра',
    'NOK':'Норвежская крона',
    'NZD':'Новозеландский доллар',
    'PHP':'Филиппинский песо',
    'PKR':'Пакистанская рупия',
    'PLN':'Слотый (Польша)',
    'SAR':'Риял (Сайдовская Аравия)',
    'SEK':'Шведская крона',
    'SGD':'Сингапурский доллар',
    'THB':'Бат (Таиланд)',
    'TRY':'Турецкая лира',
    'TWD':'Новый тайваньский доллар',
    'UAH':'Гривна',
    'VEF':'Венесуэльский боливар',
    'VND':'Вьетнамский донг',
    'ZAR':'Южноафриканский рэнд'
}

cript = {
    'BTC':'Bitcoin',
    'ETH':'Ethereum',
    'DOGE':'Dogecoin',
    'LTC':'Litecoin',
    'XLM':'Stellar',
    'SOL':'Solana',
    'XRP':'Ripple',
    'ADA':'Cardano',
    }

window = Tk()
window.title("Курсы обмена криптовалют")
window.geometry("360x500")

Label(text="Выберите код первой валюты").pack(padx=10, pady=10)
currency1_combobox = ttk.Combobox(values=list(currency.keys())) # Combobox  виджет в tkinter используется для создания выпадающего списка
currency1_combobox.pack(padx=10, pady=10)
currency1_combobox.bind("<<ComboboxSelected>>", update_currency1_label) # bind()  метод tkinter используется для привязки события к виджету
currency1_label = ttk.Label()
currency1_label.pack(padx=10, pady=10) # метод `pack()` в tkinter размещает виджеты в окне

Label(text="Выберите код второй валюты").pack(padx=10, pady=10)
currency2_combobox = ttk.Combobox(values=list(currency.keys()))
currency2_combobox.pack(padx=10, pady=10)
currency2_combobox.bind("<<ComboboxSelected>>", update_currency2_label)
currency2_label = ttk.Label()
currency2_label.pack(padx=10, pady=10)

Label(text="Выберите код криптовалюты").pack(padx=10, pady=10)
cript_combobox = ttk.Combobox(values=list(cript.keys()))
cript_combobox.pack(padx=10, pady=10)
cript_combobox.bind("<<ComboboxSelected>>", update_cript_label)

cript_label = ttk.Label()
cript_label.pack(padx=10, pady=10)

exchange_label = Label()
exchange_label.pack(padx=10, pady=10)

Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)

window.mainloop()



# result = requests.get('https://open.er-api.com/v6/latest/USD')
# data = json.loads(result.text)
# p = pprint.PrettyPrinter(indent=4)
# p.pprint(data)