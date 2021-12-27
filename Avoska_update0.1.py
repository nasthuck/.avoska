#импортирование
import time
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math
import sys
import pyshorteners
import speedtest
import random
import requests
from bs4 import BeautifulSoup
import webbrowser
#Начальное окно
def first_label():
    # функции
    def sait_for_me():
        webbrowser.open_new('https://nasthuck.github.io/zavertkin.github.io/')

    def glavnua():
        privet = Label(
            window_privet,
            text="""И снова привет! Сейчас ты на главной странице ассистента Авоськи 1.0
                Это проект был задуман мной чисто случайно.
                Перед началом работы открой командную строку и напиши следующие команды:
                1)pip install pyshorteners
                2)pip install speedtest-cli""",
        )
        privet.place(x=0, y=5)
        sait_main = Button(window_privet, text="Мой сайт", command=sait_for_me, )
        sait_main.place(x=130, y=100, width=150, height=26)
        close_privet = Button(window_privet, text="Продолжить", command=window_privet.destroy, )
        close_privet.place(x=320, y=100, width=150, height=26)

    # окно и его настройки
    window_privet = Tk()
    window_privet.title("Avoska by Zavertkin")
    window_privet.iconbitmap('D:\проэкты\практика\ico1.ico')
    window_privet.geometry("590x180")
    window_privet.resizable(False, False)
    glavnua()
    window_privet.mainloop()
first_label()
#bycode
print("""Привет, я ассистент Авоська, буду служить тебе верой и правдой,
перед началом работы, ответь на несколько моих вопросов:""")
name_pols=str(input("Как тебя зовут?: "))
brow_pols=str(input("Какой браузер ты используешь?: "))
print("Спасибо за ответ! Начинаю запуск")
polos="█"
for i in range(101):
    time.sleep(0.01)
    print('\r', 'Загрузка', '[', i*polos, ']', str(i), '%', end=' ')
besconech=1
#function
def bigfunct():
    while besconech>0:
        print("""
        Что тебе нужно,""",name_pols,"?",
        """
        1)Калькулятор
        2)Сократить ссылку
        3)Проверить скорость интернета
        4)Генератор пароля
        5)Камень, ножницы, бумага
        6)Курс доллара""")
        num_potr = eval(input("Введите номер: "))
        if num_potr==1:
            def calcin():
                root = Tk()
                root.title("Кулькулятор инженерный by Zavertkin")
                root.iconbitmap('D:\проэкты\практика\ico1.ico')

                bttn_list = [
                    "Закрыть", "|x|", "xⁿ", "C",
                    "π", "sin", "cos", "√2",
                    "(", ")", "n!", "/",
                    "7", "8", "9", "*",
                    "4", "5", "6", "-",
                    "1", "2", "3", "+",
                    "±", "0", ".", "=", ]

                r = 1
                c = 0
                for i in bttn_list:
                    rel = ""
                    cmd = lambda x=i: calc(x)
                    knop = ttk.Button(root, text=i, command=cmd, width=20).grid(row=r, column=c)
                    c += 1
                    if c > 3:
                        c = 0
                        r += 1

                calc_entry = Entry(root, width=60)
                calc_entry.grid(row=0, column=0, columnspan=15)

                # логика калькулятора
                def calc(key):
                    global memory
                    if key == "=":
                        # исключение написания слов
                        str1 = "-+0123456789.*/)("
                        if calc_entry.get()[0] not in str1:
                            calc_entry.insert(END, "Первый символ - не число!")
                            messagebox.showerror("Ошибка!", "Ты ввел не число!")
                        # исключения чисел
                        try:
                            result = eval(calc_entry.get())
                            calc_entry.insert(END, "=" + str(result))
                        except:
                            calc_entry.insert(END, "Ошибка!")
                            messagebox.showerror("Ошибка!", "Проверь своё число")
                    # очищение поля ввода
                    elif key == "C":
                        calc_entry.delete(0, END)

                    elif key == "±":
                        if "=" in calc_entry.get():
                            calc_entry.delete(0, END)
                        try:
                            if calc_entry.get()[0] == "-":
                                calc_entry.delete(0)
                            else:
                                calc_entry.insert(0, "-")
                        except IndexError:
                            pass
                    elif key == "π":
                        calc_entry.insert(END, math.pi)
                    elif key == "Закрыть":
                        root.after(1, root.destroy)
                        sys.exit
                    elif key == "xⁿ":
                        calc_entry.insert(END, "**")
                    elif key == "sin":
                        calc_entry.insert(END, "=" + str(math.sin(int(calc_entry.get()))))
                    elif key == "cos":
                        calc_entry.insert(END, "=" + str(math.cos(int(calc_entry.get()))))
                    elif key == "(":
                        calc_entry.insert(END, "(")
                    elif key == ")":
                        calc_entry.insert(END, ")")
                    elif key == "n!":
                        calc_entry.insert(END, "=" + str(math.factorial(int(calc_entry.get()))))
                    elif key == "√2":
                        calc_entry.insert(END, "=" + str(math.sqrt(int(calc_entry.get()))))
                    elif key == "|x|":
                        if eval(calc_entry.get()) < 0:
                            chis_num = eval(calc_entry.get())
                            chis_num = chis_num * -1
                            calc_entry.insert(END, "=" + str(chis_num))
                        else:
                            calc_entry.insert(END, "=" + str(calc_entry.get()))
                    else:
                        if "=" in calc_entry.get():
                            calc_entry.delete(0, END)
                        calc_entry.insert(END, key)

                root.mainloop()
            calcin()
        elif num_potr==2:
            def ssilcan():
                ssilk = str(input("Введите ссылку: "))
                s = pyshorteners.Shortener()
                print("Сокращенная ссылка - ", s.tinyurl.short(ssilk))
            ssilcan()
        elif num_potr==3:
            def speeding():
                st = speedtest.Speedtest()
                option = int(input('''
                Выбери тип проверки:   
    
                1 - Скорость принятия(скачать фильм например)  
                2 - Скорость отдачи(загрузить картинку в инстаграмм)   
    
                Твой выбор: '''))

                if option == 1:
                    speed_zag = st.download()
                    speed_zag = speed_zag / 1024 / 1024
                    speed_zag = round(speed_zag, 4)
                    print(speed_zag, "Мбит/с")
                elif option == 2:
                    speed_ot = st.upload()
                    speed_ot = speed_ot / 1024 / 1024
                    speed_ot = round(speed_ot, 4)
                    print(speed_ot, "Мбит/с")
            speeding()
        elif num_potr==4:
            def gen_parola():
                cifr_kol = int(input("Пожалуйста, введите кол-во знаков в пароле:"))
                # большие букавы
                alphabets_in_capital = []
                for i in range(65, 91):
                    alphabets_in_capital.append(chr(i))
                big_simv = alphabets_in_capital
                # маленькие букавы
                alphabets_in_lowercase = []
                for i in range(97, 123):
                    alphabets_in_lowercase.append(chr(i))
                smoll_simv = alphabets_in_lowercase
                cifr_all = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
                all_simvol = big_simv + smoll_simv + cifr_all
                konech_parol = []
                for k in range(1, cifr_kol + 1):
                    rand_simvol = random.choice(all_simvol)
                    konech_parol = konech_parol + [rand_simvol]
                print("Ваш пароль: ", ''.join(konech_parol))
            gen_parola()
        elif num_potr==5:
            def kamennozsh():
                print("<-----------Игра Камень, Ножницы, Бумага----------->")

                def my_game():
                    k_n_b = ["Камень", "Ножницы", "Бумага"]
                    computer = random.choice(k_n_b)
                    # игра
                    player = input("Ваш ход:").lower().capitalize()
                    try:
                        if computer == "Камень":
                            if player == "Камень":
                                print('Ничья')
                            elif player == "Бумага":
                                print('Ты выиграл')
                            elif player == "Ножницы":
                                print('Ты проиграл')
                            # ход2
                        elif computer == "Бумага":
                            if player == "Камень":
                                print('Ты проиграл')
                            elif player == "Бумага":
                                print('Ничья')
                            elif player == "Ножницы":
                                print('Ты проиграл')
                            # ход3
                        elif computer == "Ножницы":
                            if player == "Камень":
                                print('Ты проиграл')
                            elif player == "Бумага":
                                print('Ты выиграл')
                            elif player == "Ножницы":
                                print('Ничья')
                    except:
                        print("Что-то пошло не так")
                    # Заново
                    play_again = input("Вы хотите продолжить?:")
                    kmb_otv = ["ДА", "да", "Да", "дА", "yes", 'yeas', 'Yes']
                    kmb_otv_none = ["нЕТ", "НЕТ", "Нет", "нет", "no", 'No', 'NO']
                    if play_again in kmb_otv:
                        my_game()
                    elif play_again in kmb_otv_none:
                        print("Досвидание")

                my_game()
            kamennozsh()
        elif num_potr==6:
            def einen_dollar():
                class Currency:
                    # Ссылка на google
                    DOLLAR_RUB = 'https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw%3A1584716087546&source=hp&ei=N9l0XtDXHs716QTcuaXoAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131l4.3044.4178..5294...1.0..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4'
                    # Заголовки для передачи вместе с URL
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

                    current_converted_price = 0
                    difference = 1.5

                    def __init__(self):
                        # Установка курса валюты при создании объекта
                        self.current_converted_price = float(self.get_currency_price().replace(",", "."))

                    # Метод для получения курса валюты
                    def get_currency_price(self):
                        # Парсинг
                        full_page = requests.get(self.DOLLAR_RUB, headers=self.headers)

                        # просеивание BeautifulSoup
                        soup = BeautifulSoup(full_page.content, 'html.parser')

                        # Получаем значение
                        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
                        return convert[0].text

                    # Проверка изменения валюты
                    def check_currency(self):
                        currency = float(self.get_currency_price().replace(",", "."))
                        if currency >= self.current_converted_price + self.difference:
                            print("Курс сильно вырос, может пора что-то делать?")
                        elif currency <= self.current_converted_price - self.difference:
                            print("Курс сильно упал, может пора что-то делать?")
                        print("1 доллар = " + str(currency))

                # ВНИМАНИЕ!ДА, ДА, Я ПЛОХОЙ НИКИТА, ПРОГРАММА ДЛЯ АНАЛИЗА КУРСА ВАЛЮТЫ БЫЛА ВЗЯТА И ИЗМЕНЕНА С САЙТА https://itproger.com/news/programma-na-python-dlya-otslezhivaniya-kursa-valyuti
                # Создание объекта и вызов метода
                currency = Currency()
                currency.check_currency()
            einen_dollar()
        exit_none = str(input("Вы хотите выйти(да/нет)?: "))
        exit_spis = ['yes', 'ja', 'ja, wohl', 'да', 'конечно', 'хочу']
        if exit_none in exit_spis:
            print('Всего доброго!')
            break
bigfunct()

