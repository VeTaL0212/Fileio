from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
import requests
from tkinter import messagebox as mb
import pyperclip # модуль Python позволяет копировать текст в буфер обмена
import json
import os


history_file = "upload_history.json"


def save_history(file_path, link):
    history = []
    if os.path.exists(history_file):
        with open(history_file, 'r') as f:
            history = json.load(f)
    history.append({'file_path': os.path.basename(file_path), "download_link": link})
    with open(history_file, 'w') as f:
        json.dump(history, f, indent=4) # json.dump(data, file)`  сохранить данные в формате JSON в файл


def upload():
    try:
        filepath = fd.askopenfilename() # filedialog.askopenfilename()` открыть диалог выбора файла
        if filepath:
            with open(filepath, 'rb') as f:
                files = {'file': f}
                response = requests.post('https://file.io', files=files) #  POST - этот HTTP метод используется для отправки файла на сервер
                response.raise_for_status()
                link = response.json()['link']
                entry.delete(0, END) # entry.delete(0, END) очистить Entry виджет
                entry.insert(0, link)
                pyperclip.copy(link)
                save_history(filepath, link)
                mb.showinfo("Ссылка скопированна", f"Ссылка {link} успешно скопирована в буфер обмена")

    except Exception as e:
        mb.showerror("Ошибка", f"Произошла ошибка: {e}")


def show_history():
    if not os.path.exists(history_file):
        mb.showinfo("История", "История загрузок пуста")
        return

    history_window = Toplevel(window) # Toplevel(window) создать дочернее окно
    history_window.title("История загрузок")

    files_listbox = Listbox(history_window, width=50, height=20)
    files_listbox.grid(row=0, column=0, padx=(10, 0), pady=10) # widget.grid(row=1, column=2) в Tkinter использовать Grid для расположения виджетов

    links_listbox = Listbox(history_window, width=50, height=20)
    links_listbox.grid(row=0, column=1, padx=(0, 10), pady=10)

    with open(history_file, 'r') as f:
        history = json.load(f) # `json.load(file)` метод используется для чтения JSON данных из файла
        for item in history:
            files_listbox.insert(END, item['file_path']) # listbox.insert(END, item)` добавить элементы в Listbox в Tkinter
            links_listbox.insert(END, item['download_link'])

window = Tk()
window.title("Сохранение файлов в облаке")
window.geometry("400x200")

button = ttk.Button(text="Загрузить файл", command=upload)
button.pack()

entry = ttk.Entry()
entry.pack()

history_button = ttk.Button(text="Показать историю", command=show_history)
history_button.pack()

window.mainloop()
