import requests
import  json
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


def update_t_label(event):
    code = t_combobox.get()
    name = cur[code]
    t_label.config(text=name)


def update_b1_label(event):
    code = b1_combobox.get()
    name = cur[code]
    b1_label.config(text=name)


def update_b2_label(event):
    code = b2_combobox.get()
    name = cur[code]
    b2_label.config(text=name)


def exchange():
    t_code = t_combobox.get()
    b1_code = b1_combobox.get()
    b2_code = b2_combobox.get()

    if t_code and b1_code and b2_code:
        try:
            response = requests.get(f"https://open.er-api.com/v6/latest/{b1_code}")
            response2 = requests.get(f"https://open.er-api.com/v6/latest/{b2_code}")# Для получения данных с сервера используется метод `get` библиотеки requests
            response.raise_for_status() # метод `raise_for_status()` в библиотеке requests  Устанавливает статус-код ответа
            response2.raise_for_status()
            data = response.json() # раскладываем в виде обычного python словаря
            data2 = response2.json()
            if t_code in data["rates"]:
                exchange_rate = data['rates'][t_code]
                exchange2_rate = data2['rates'][t_code]
                t_name = cur[t_code]
                b1_name = cur[b1_code]
                b2_name = cur[b2_code]
                mb.showinfo("Курс обмена", f"Курс: {exchange_rate:.2f} {t_name} за один {b1_name} \n и {exchange2_rate:.2f} {t_name} за один {b2_name}")
            else:
                mb.showerror("Ошибка", f"Валюта {t_code} не найдена!")
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}.")
    else:
        mb.showwarning("Внимание", "Введите код калюты")


cur ={
    'RUB': "Российский рубль",
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

window = Tk()
window.title("Курсы обмена валют")
window.geometry("360x450")

Label(text="Базавая валюта").pack(padx=10, pady=10)
b1_combobox = ttk.Combobox(values=list(cur.keys())) # Combobox  виджет в tkinter используется для создания выпадающего списка
b1_combobox.pack(padx=10, pady=10)
b1_combobox.bind("<<ComboboxSelected>>", update_b1_label) # bind()  метод tkinter используется для привязки события к виджету
b1_label = ttk.Label()
b1_label.pack(padx=10, pady=10)

Label(text="Вторая базавая валюта").pack(padx=10, pady=10)
b2_combobox = ttk.Combobox(values=list(cur.keys()))
b2_combobox.pack(padx=10, pady=10)
b2_combobox.bind("<<ComboboxSelected>>", update_b2_label)
b2_label = ttk.Label()
b2_label.pack(padx=10, pady=10)


Label(text="Целевая валюта").pack(padx=10, pady=10)
t_combobox = ttk.Combobox(values=list(cur.keys()))
t_combobox.pack(padx=10, pady=10)
t_combobox.bind("<<ComboboxSelected>>", update_t_label)
t_label = ttk.Label()
t_label.pack(padx=10, pady=10)

Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)

window.mainloop()



# result = requests.get('https://open.er-api.com/v6/latest/USD')
# data = json.loads(result.text)
# p = pprint.PrettyPrinter(indent=4)
# p.pprint(data)