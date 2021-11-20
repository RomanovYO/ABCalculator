# A/B калькулятор

import tkinter as tk

# Функция закрытия программы
def do_close():
  root.destroy()

# Функция создания окна результата
def popup_window():
  window = tk.Toplevel()
  window.geometry('280x300-350+250')
  window.title('A/B результат')

  # Добавление кнопки закрытия окна результата
  btnClosePopup = tk.Button(window, text = 'Закрыть', font = ('Helvetica', 10, 'bold'), command = window.destroy)
  btnClosePopup.place(x = 160, y = 250, width = 90, height = 30)

# Создание главного окна
root = tk.Tk()
root.geometry('280x300-400+200')
root.title('A/B калькулятор')

# Добавление метки заголовка
y = 20
lblTitle = tk.Label(text = 'A/B калькулятор', font = ('Helvetica', 16, 'bold'), fg = '#0000cc')
lblTitle.place(x = 55, y = y)

# Добавление метки заголовка контрольной группы
y += 35
lblTitle1 = tk.Label(text = 'Контрольная группа', font = ('Helvetica', 12, 'bold'), fg = '#0066ff')
lblTitle1.place(x = 25, y = y)

# Добавление полей ввода контрольной группы
y += 30
lblVisitors1 = tk.Label(text = 'Посетители:', font = ('Helvetica', 10, 'bold'))
lblVisitors1.place(x = 25, y = y)
entVisitors1 = tk.Entry(font = ('Helvetica', 10, 'bold'))
entVisitors1.place(x = 115, y = y, width = 90, height = 20)
y += 30
lblConversions1 = tk.Label(text = 'Конверсия:', font = ('Helvetica', 10, 'bold'))
lblConversions1.place(x = 25, y = y)
entConversions1 = tk.Entry(font = ('Helvetica', 10, 'bold'))
entConversions1.place(x = 115, y = y, width = 90, height = 20)

# Добавление метки заголовка тестовой группы
y += 35
lblTitle2 = tk.Label(text = 'Тестовая группа', font = ('Helvetica', 12, 'bold'), fg = '#0066ff')
lblTitle2.place(x = 25, y = y)

# Добавление полей ввода тестовой группы
y += 30
lblVisitors2 = tk.Label(text = 'Посетители:', font = ('Helvetica', 10, 'bold'))
lblVisitors2.place(x = 25, y = y)
entVisitors2 = tk.Entry(font = ('Helvetica', 10, 'bold'))
entVisitors2.place(x = 115, y = y, width = 90, height = 20)
y += 30
lblConversions2 = tk.Label(text = 'Конверсия:', font = ('Helvetica', 10, 'bold'))
lblConversions2.place(x = 25, y = y)
entConversions2 = tk.Entry(font = ('Helvetica', 10, 'bold'))
entConversions2.place(x = 115, y = y, width = 90, height = 20)



# Добавление кнопки Рассчитать
y += 40
btnClose = tk.Button(root, text = 'Рассчитать', font = ('Helvetica', 10, 'bold'), command = popup_window)
btnClose.place(x = 25, y = y, width = 90, height = 30)

# Добавление кнопки закрытия программы
btnClose = tk.Button(root, text = 'Закрыть', font = ('Helvetica', 10, 'bold'), command = do_close)
btnClose.place(x = 160, y = y, width = 90, height = 30)

# Запуск цикла mainloop
root.mainloop()
