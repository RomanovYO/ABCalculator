# A/B калькулятор

import tkinter as tk

# Создание главного окна
root = tk.Tk()
root.geometry('280x300-400+200')
root.title('A/B калькулятор')

y = 200

# Добавление метки заголовка
lblTitle = tk.Label(text = 'A/B калькулятор', font = ('Helvetica', 16, 'bold'), fg = '#0000cc')
lblTitle.place(x = 55, y = 20)

# Добавление кнопки Рассчитать
y += 50
btnClose = tk.Button(root, text = 'Рассчитать', font = ('Helvetica', 10, 'bold'))
btnClose.place(x = 25, y = y, width = 90, height = 30)

# Функция закрытия программы
def do_close():
  root.destroy()

# Добавление кнопки закрытия программы
btnClose = tk.Button(root, text = 'Закрыть', font = ('Helvetica', 10, 'bold'), command = do_close)
btnClose.place(x = 160, y = y, width = 90, height = 30)

# Запуск цикла mainloop
root.mainloop()
