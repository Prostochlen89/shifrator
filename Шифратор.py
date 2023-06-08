from tkinter import *
import customtkinter
from tkinter import messagebox as mb
from random import randint
import os
import pyAesCrypt
from tkinter import filedialog as fd

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
def optionmenu_callback(choice):
    if choice in "Светлая":
        customtkinter.set_appearance_mode("light")

    if choice in "Тёмная":
        customtkinter.set_appearance_mode("dark")
def kopir():
    tk.clipboard_clear()
    tk.clipboard_append(str(l))
def bufera():
    text = tk.selection_get(selection='CLIPBOARD')
    ent1.insert(0.0, text)
def kopir1():
    tk.clipboard_clear()
    tk.clipboard_append(str(b))
def bufera1():
    text = tk.selection_get(selection='CLIPBOARD')
    ent2.insert(0.0, text)
def kopir2():
    tk.clipboard_clear()
    tk.clipboard_append(str(l))
def bufera2():
    text = tk.selection_get(selection='CLIPBOARD')
    ent3.insert(0.0, text)
def kopir3():
    tk.clipboard_clear()
    tk.clipboard_append(str(b))
def bufera3():
    text = tk.selection_get(selection='CLIPBOARD')
    ent4.insert(0.0, text)
def schifrator():
    global l
    s = ent1.get(1.0, END)
    s = s.lower()
    k = (key1.get())
    if k.isdigit() == False:
        mb.showerror("Ошибка","Должно быть введено число\n              от 1 до 32")
    l = ''
    k = int(k)
    for letter in s:
        position = alphabet.find(letter)
        newPosition = position + k
        if letter in alphabet:
            l = l + alphabet[newPosition]
        else:
            l = l + letter
    l1.delete(1.0, END)
    l1.insert(0.0, l)
def deschifrator():
    global b
    a = ent2.get(1.0, END)
    a = a.lower()
    o = (key2.get())
    if o.isdigit() == False:
        mb.showerror("Ошибка","Должно быть введено число\n              от 1 до 32")
    b = ''
    o = int(o)
    for letter in a:
        position = alphabet.find(letter)
        newPosition = position - o
        if letter in alphabet:
            b = b + alphabet[newPosition]
        else:
            b = b + letter
    l2.delete(1.0, END)
    l2.insert(0.0, b)
def vernam():
    global l
    key = ''
    keys = ''
    l = ''
    mes = ent3.get(1.0, END)
    for symbol in mes:
        key = randint(0, 32)
        keys += str(key) + "/"
        l += chr((ord(symbol) + key - 17) % 33 + ord('А'))
    l3.delete(1.0, END)
    l3.insert(0.0, l)
    key3.delete(1, END)
    key3.insert(0, keys)
def devernam():
    global b
    b = ''
    final = ent4.get(1.0, END)
    keys = key4.get()
    keys = keys.split('/')
    for i, symbol in enumerate(final):
        if keys[i] != '':
            b += chr((ord(symbol) - int(keys[i]) - 17) % 33 + ord('А'))
    l4.delete(1.0, END)
    l4.insert(0.0, b)

def prekol1():
    password = pas1.get()
    file = fd.askdirectory()
    walking_by_dirs1(file, password)
def decryption(file, password):

    # задаём размер буфера
    buffer_size = 512 * 1024

    # вызываем метод расшифровки
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )

    # чтобы видеть результат выводим на печать имя зашифрованного файла
    mb.showinfo('Шифратор', 'Файл ' + str(os.path.splitext(file)[0]) + ' дешифрован')
    if b1.get() == True:
        # удаляем исходный файл
        os.remove(file)

# функция сканирования директорий
def walking_by_dirs1(dir, password):

    # перебираем все поддиректории в указанной директории
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # если находим файл, то дешифруем его
        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)
        # если находим директорию, то повторяем цикл в поисках файлов
        else:
            walking_by_dirs1(path, password)

def prekol():
    password = pas.get()
    file = fd.askdirectory()
    walking_by_dirs(file, password)
def encryption(file, password):

    # задаём размер буфера
    buffer_size = 512 * 1024

    # вызываем метод шифрования
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".crp",
        password,
        buffer_size
    )
    # чтобы видеть результат выводим на печать имя зашифрованного файла
    mb.showinfo('Шифратор', 'Файл ' + str(os.path.splitext(file)[0]) + ' зашифрован')
    if b2.get() == True:
        # удаляем исходный файл
         os.remove(file)

# функция сканирования директорий
def walking_by_dirs(dir, password):

    # перебираем все поддиректории в указанной директории
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # если находим файл, то шифруем его
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)
        # если находим директорию, то повторяем цикл в поисках файлов
        else:
            walking_by_dirs(path, password)
def frame1():
    frame_4.place_forget()
    frame_3.place_forget()
    frame_5.place_forget()
    g2.place_forget()
    g3.place_forget()
    frame.place(x=207, y=5)
    frame_2.place(x=207, y=255)
    g1.place(x=40, y=10)
def frame2():
    frame_2.place_forget()
    frame_5.place_forget()
    frame.place_forget()
    g1.place_forget()
    g3.place_forget()
    frame_3.place(x=207, y=5)
    frame_4.place(x=207, y=255)
    g2.place(x=35, y=10)
def frame3 () :
    frame_2.place_forget()
    frame.place_forget()
    g1.place_forget()
    g2.place_forget()
    g3.place(x=20, y=10)
    frame_5.place(x=207, y=5)

tk = customtkinter.CTk()
tk.geometry("1000x500")
tk.title("Шифратор")
tk.resizable(False, False)
frame = customtkinter.CTkFrame(master=tk, width=787, height=240)
frame.place(x=207, y=5)
frame_1 = customtkinter.CTkFrame(master=tk, width=200, height=510)
frame_1.place(x=0, y=-1)
frame_2 = customtkinter.CTkFrame(master=tk, width=787, height=240)
frame_2.place(x=207, y=255)
frame_3 = customtkinter.CTkFrame(master=tk, width=787, height=240)
frame_4 = customtkinter.CTkFrame(master=tk, width=787, height=240)
frame_5 = customtkinter.CTkFrame(master=tk, width=787, height=490)
optionmenu = customtkinter.CTkOptionMenu(master=frame_1, values=["Светлая", "Тёмная"],
                                         command=optionmenu_callback, fg_color="#2724fb")\
                                         .place(x=35, y=450)

g1 = customtkinter.CTkLabel(master=frame_1, text="Шифр Цезаря", font=('', 20))
g1.place(x=40, y=10)
g2 = customtkinter.CTkLabel(master=frame_1, text="Шифр Вернама", font=('', 20))
g3 = customtkinter.CTkLabel(master=frame_1, text="Шифратор файлов", font=('', 20))
c1 = customtkinter.CTkLabel(master=frame, text="Введите слово для шифровки")
c1.place(x=115, y=3)
c2 = customtkinter.CTkLabel(master=frame, text="Результат")
c2.place(x=560, y=3)
c3 = customtkinter.CTkLabel(master=frame_2, text="Результат")
c3.place(x=560, y=3)
c4 = customtkinter.CTkLabel(master=frame, text="Ключ")
c4.place(x=185, y=180)
but3 = customtkinter.CTkButton(master=frame_1, text="ШИФР ЦЕЗАРЯ", command=frame1,
                               text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                               corner_radius=0, fg_color="transparent", height=50, width=200)
but3.place(x=0, y=50)
but4 = customtkinter.CTkButton(master=frame_1, text="ШИФР ВЕРНАМА", command=frame2,
                               text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                               corner_radius=0, fg_color="transparent", height=50, width=200)
but4.place(x=0, y=100)
but5 = customtkinter.CTkButton(master=frame_1, text="ШИФРАТОР ФАЙЛОВ", command=frame3,
                               text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                               corner_radius=0, fg_color="transparent", height=50, width=200)
but5.place(x=0, y=150)
ent1 = customtkinter.CTkTextbox(master=frame, width=380, height=150)
ent1.place(x=5, y=30)
key1 = customtkinter.CTkEntry(master=frame, width=380)
key1.place(x=5, y=205)
l1 = customtkinter.CTkTextbox(master=frame, width=380, height=150)
l1.place(x=400, y=30)
but1 = customtkinter.CTkButton(master=frame, text="Зашифровать",
                               command=schifrator, height=40,
                               width=120, fg_color="#2724fb")
but1.place(x=400, y=190)
kop1 = customtkinter.CTkButton(master=frame, text="Скопировать",
                               command=kopir, height=40,
                               width=120, fg_color="#2724fb")
kop1.place(x=530, y=190)
kop2 = customtkinter.CTkButton(master=frame, text="Вставить текст",
                               command=bufera, height=40,
                               width=120, fg_color="#2724fb")
kop2.place(x=660, y=190)
kop3 = customtkinter.CTkButton(master=frame_2, text="Скопировать",
                               command=kopir1, height=40,
                               width=120, fg_color="#2724fb")
kop3.place(x=530, y=190)
kop4 = customtkinter.CTkButton(master=frame_2, text="Вставить текст",
                               command=bufera1, height=40,
                               width=120, fg_color="#2724fb")
kop4.place(x=660, y=190)
customtkinter.CTkLabel(master=frame_2, text="Введите слово для дешифровки").place(x=115, y=3)
customtkinter.CTkLabel(master=frame_2, text="Ключ").place(x=185, y=180)
ent2 = customtkinter.CTkTextbox(master=frame_2, width=380, height=150)
ent2.place(x=5, y=30)
key2 = customtkinter.CTkEntry(master=frame_2, width=380)
key2.place(x=5, y=205)
l2 = customtkinter.CTkTextbox(master=frame_2, width=380, height=150)
l2.place(x=400, y=30)
but2 = customtkinter.CTkButton(master=frame_2, text="Дешифровать",
                               command=deschifrator, height=40,
                               width=120, fg_color="#2724fb")
but2.place(x=400, y=190)

customtkinter.CTkLabel(master=frame_3, text="Введите слово для шифровки").place(x=115, y=3)
customtkinter.CTkLabel(master=frame_3, text="Результат").place(x=560, y=3)
customtkinter.CTkLabel(master=frame_4, text="Результат").place(x=560, y=3)
customtkinter.CTkLabel(master=frame_3, text="Ключ").place(x=185, y=180)
ent3 = customtkinter.CTkTextbox(master=frame_3, width=380, height=150)
ent3.place(x=5, y=30)
key3 = customtkinter.CTkEntry(master=frame_3, width=380)
key3.place(x=5, y=205)
l3 = customtkinter.CTkTextbox(master=frame_3, width=380, height=150)
l3.place(x=400, y=30)
but3 = customtkinter.CTkButton(master=frame_3, text="Зашифровать",
                               command=vernam, height=40,
                               width=120, fg_color="#2724fb")
but3.place(x=400, y=190)
kop5 = customtkinter.CTkButton(master=frame_3, text="Скопировать",
                               command=kopir2, height=40,
                               width=120, fg_color="#2724fb")
kop5.place(x=530, y=190)
kop6 = customtkinter.CTkButton(master=frame_3, text="Вставить текст",
                               command=bufera2, height=40,
                               width=120, fg_color="#2724fb")
kop6.place(x=660, y=190)
kop7 = customtkinter.CTkButton(master=frame_4, text="Скопировать",
                               command=kopir3, height=40,
                               width=120, fg_color="#2724fb")
kop7.place(x=530, y=190)
kop8 = customtkinter.CTkButton(master=frame_4, text="Вставить текст",
                               command=bufera3, height=40,
                               width=120, fg_color="#2724fb")
kop8.place(x=660, y=190)
customtkinter.CTkLabel(master=frame_4, text="Введите слово для дешифровки").place(x=115, y=3)
customtkinter.CTkLabel(master=frame_4, text="Ключ").place(x=185, y=180)
ent4 = customtkinter.CTkTextbox(master=frame_4, width=380, height=150)
ent4.place(x=5, y=30)
key4 = customtkinter.CTkEntry(master=frame_4, width=380)
key4.place(x=5, y=205)
l4 = customtkinter.CTkTextbox(master=frame_4, width=380, height=150)
l4.place(x=400, y=30)
but4 = customtkinter.CTkButton(master=frame_4, text="Дешифровать",
                               command=devernam, height=40,
                               width=120, fg_color="#2724fb")
but4.place(x=400, y=190)

pas = customtkinter.CTkEntry(master=frame_5, width=600)
pas.place(x=5, y=190)
jk = customtkinter.CTkButton(master=frame_5, text="Зашифровать",
                             command=prekol, height=40,
                             width=120, fg_color="#2724fb")
jk.place(x=630, y=180)
pas1 = customtkinter.CTkEntry(master=frame_5, width=600)
pas1.place(x=5, y=450)
dk = customtkinter.CTkButton(master=frame_5, text="Дешифровать",
                             command=prekol1, height=40,
                             width=120, fg_color="#2724fb")
dk.place(x=630, y=440)
da = customtkinter.CTkLabel(master=frame_5, text="Чтобы зашифровать файл создайте папку\n с файлами которые хотите зашифровать"
                                                 "\n после чего введите в поле ключ \nи нажмите на кнопку 'Зашифровать' \n"
                                                 "и выберете папку с файлами.\n(Инструмент шифрования AesCrypt)", font=('', 20))
da.place(x=100, y=25)
dd = customtkinter.CTkLabel(master=frame_5, text="Чтобы дешифровать файл введите ключ\n в поле и нажмите на кнопку 'Дешифровать'\n"
                                                 " и выберете паку с файлами \nкоторую хотите дешифровать.\n (Инструмент шифрования AesCrypt)", font=('', 20))
dd.place(x=100, y=270)
b1 = BooleanVar()
b1.set(0)
bb = customtkinter.CTkCheckBox(master=frame_5, text="  Удалить\n  зашифрованные\n  файлы", variable=b1, onvalue=1, offvalue=0)
bb.place(x=630, y=380)
b2 = BooleanVar()
b2.set(0)
bg = customtkinter.CTkCheckBox(master=frame_5, text="  Удалить\n  исходные\n  файлы", variable=b2, onvalue=1, offvalue=0)
bg.place(x=630, y=120)

tk.mainloop()