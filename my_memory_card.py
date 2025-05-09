#создай приложение для запоминания информации

#подключение библиотек
from random import*
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QGroupBox,
QButtonGroup)

# класс, хранящий свойства вопросов
class Question ():
    def __init__(self, question, right, wrong1, wrong2, wrong3):
        self.question = question
        self.right = right
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

# делаем заготовки вопросов
q_list = []
q_list.append(Question ("Какого цвета нет на флаге России?", "Зеленый","Красный","Синий","Белый"))
q_list.append(Question ("Какой национальности не существует?", 'Смурфы', 'Энцы', 'Татары', 'Финны'))
q_list.append(Question ("Национальная хижина якутов", "Ураса","Юрта","Иглу","Хата"))
q_list.append(Question ("Какой столицы не существует?", "Нью-Йорк","Москва","Лондон","Бразилиа"))
q_list.append(Question ("Какого моря не существует?", "Синее","Красное","Чёрное","Белое"))
#создание приложения и главного окна
my_app = QApplication([])
window = QWidget()
window.setWindowTitle ("Memory Card")
window.move(750, 200)
window.resize(1000, 700)

# создание виджетов главного окна
questtext = QLabel ("Самый сложный вопрос") #текст вопроса
ans = QPushButton ("Ответить") # кнопка ответа и далее

# бокс для показа вопросов Group_q
Group_q = QGroupBox ("Варианты ответов") # объединение (визуальное) вариантов ответа
b1 = QRadioButton ("В1") # радиокнопки варинатов
b2 = QRadioButton ("В2")
b3 = QRadioButton ("В3")
b4 = QRadioButton ("В4")
# в группбоксе делаем линии и добавляем туда радиокнопки
V1 = QVBoxLayout ()
h1 = QHBoxLayout ()
h2 = QHBoxLayout ()
h1.addStretch (1)
h1.addWidget (b1, alignment=Qt.AlignCenter, stretch=3)
h1.addWidget (b3, alignment=Qt.AlignCenter, stretch=3)
h1.addStretch (1)
h2.addStretch (1)
h2.addWidget (b2, alignment=Qt.AlignCenter, stretch=3)
h2.addWidget (b4, alignment=Qt.AlignCenter, stretch=3)
h2.addStretch (1)
V1.addLayout(h1)
V1.addLayout(h2)
Group_q.setLayout (V1)
# бокс для показа ответов Group_a
Group_a = QGroupBox ("Результат теста")
result = QLabel ("Правильно/Неправильно")
answer_right = QLabel ("Смурфы")
lineV1 = QVBoxLayout()
lineV1.addWidget (result, alignment = Qt.AlignLeft)
lineV1.addWidget (answer_right, alignment = Qt.AlignCenter)
Group_a.setLayout (lineV1)
# объединение кнопок в группу
RadioGroup = QButtonGroup()
RadioGroup.addButton(b1)
RadioGroup.addButton(b2)
RadioGroup.addButton(b3)
RadioGroup.addButton(b4)

answers = [b1, b2, b3, b4]
def ask (q: Question):
    shuffle(answers)
    answers[0].setText(q.right)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    questtext.setText(q.question)
    answer_right.setText(q.right)
    show_question()
def show_correct(res):
    result.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked():
        show_correct("Правильно")
        window.score += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct("Неверно")
    print ("Статистика")
    print ("-Всего вопросов:", window.count)
    print ("-Правильных ответов:", window.score)
    print ("Рейтинг:", window.score/window.count*100, "%")
def show_question():
    Group_a.hide()
    Group_q.show()
    ans.setText("Ответить")
    RadioGroup.setExclusive(False)
    b1.setChecked(False)
    b2.setChecked(False)
    b3.setChecked(False)
    b4.setChecked(False)
    RadioGroup.setExclusive(True)
def show_result():
    Group_a.show()
    Group_q.hide()
    ans.setText("Следующий вопрос")
def start_test():    #!!!это click_ok()
    txt = ans.text()
    if txt == "Ответить":
        check_answer()
    else:
        next_question()
def next_question():
    window.count += 1
    window.count_q = randint(0, len(q_list)-1)
    # if window.count_q >= len(q_list):
    #     window.count_q = 0
    q = q_list[window.count_q]
    ask(q)





# расположение виджетов по лэйаутам главного окна
line_main = QVBoxLayout() # главная линия
lineH1 = QHBoxLayout() # линия текста вопроса
lineH2 = QHBoxLayout() # линия боксов варианты или ответ
lineH3 = QHBoxLayout() # линия кнопки
# на первую линию добавляем вопрос
lineH1.addWidget (questtext, alignment=Qt.AlignCenter)
# на вторую бокс вариантов
lineH2.addStretch (1)
# Group_q.show() # не нужно
Group_a.hide() # скрываем бокс ответов, чтобы не показать раньше времени
# line_main.setSpacing(4) # не нужно
lineH2.addWidget (Group_q, stretch=4)
lineH2.addWidget (Group_a, stretch=4)
lineH2.addStretch (1)
# на третью - кнопку ответа
lineH3.addWidget (ans, alignment=Qt.AlignCenter)
# добавляем линии на главную
line_main.addLayout (lineH1)
line_main.addLayout (lineH2)
line_main.addLayout(lineH3)
# применяем к окну
window.setLayout(line_main)





#обработка нажатий на переключатели
window.count = 0 #общий счет
window.score = 0 #личный счет
ans.clicked.connect(start_test) # исправил с next_question на start_test
next_question()
#отображение окна приложения
window.show()
my_app.exec_()





# #создай приложение для запоминания информации

# #подключение библиотек
# from random import*
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
# QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QGroupBox,
# QButtonGroup)

# #
# class Question ():
#     def __init__(self, question, right, wrong1, wrong2, wrong3):
#         self.question = question
#         self.right = right
#         self.wrong1 = wrong1
#         self.wrong2 = wrong2
#         self.wrong3 = wrong3

# def ask (q: Question):
#     shuffle(answers)
#     answers[0].setText(q.right)
#     answers[1].setText(q.wrong1)
#     answers[2].setText(q.wrong2)
#     answers[3].setText(q.wrong3)
#     questtext.setText(q.question)
#     answer_right.setText(q.right)
#     show_question()
# def show_correct(res):
#     result.setText(res)
#     show_result()
# def check_answer():
#     if answers[0].isChecked():
#         show_correct("Правильно")
#     else:
#         if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
#             show_correct("Неверно")
# def show_question():
#     Group_a.hide()
#     Group_q.show()
#     ans.setText("Ответить")
#     RadioGroup.setExclusive(False)
#     b1.setChecked(False)
#     b2.setChecked(False)
#     b3.setChecked(False)
#     b4.setChecked(False)
#     RadioGroup.setExclusive(True)
# def show_result():
#     Group_a.show()
#     Group_q.hide()
#     ans.setText("Следующий вопрос")
# def start_test():    #!!!это click_ok()
#     txt = ans.text()
#     if txt == "Ответить":
#         check_answer()
#     else:
#         next_question()
# def next_question():
#     window.count_q = window.count_q + 1
#     if window.count_q >= len(q_list):
#         window.count_q = 0
#     q = q_list[window.count_q]
#     ask(q)

# #создание приложения и главного окна
# my_app = QApplication([])
# window = QWidget()
# window.setWindowTitle ("Memory Card")
# window.move(750, 200)
# window.resize(1000, 700)
# #создание виджетов главного окна
# questtext = QLabel ("Самый сложный вопрос")
# ans = QPushButton ("Ответить") #!

# Group_q = QGroupBox ("Варианты ответов")
# b1 = QRadioButton ("В1")
# b2 = QRadioButton ("В2")
# b3 = QRadioButton ("В3")
# b4 = QRadioButton ("В4")

# V1 = QVBoxLayout ()
# h1 = QHBoxLayout ()
# h2 = QHBoxLayout ()
# h1.addStretch (1)
# h1.addWidget (b1, alignment=Qt.AlignCenter, stretch=3)
# h1.addWidget (b3, alignment=Qt.AlignCenter, stretch=3)
# h1.addStretch (1)
# h2.addStretch (1)
# h2.addWidget (b2, alignment=Qt.AlignCenter, stretch=3)
# h2.addWidget (b4, alignment=Qt.AlignCenter, stretch=3)
# h2.addStretch (1)
# V1.addLayout(h1)
# V1.addLayout(h2)
# Group_q.setLayout (V1)

# Group_a = QGroupBox ("Результат теста")
# result = QLabel ("Правильно/Неправильно")
# answer_right = QLabel ("Смурфы")
# lineV1 = QVBoxLayout()
# lineV1.addWidget (result, alignment = Qt.AlignLeft)
# lineV1.addWidget (answer_right, alignment = Qt.AlignCenter)
# Group_a.setLayout (lineV1)

# #расположение виджетов по лэйаутам

# line_main = QVBoxLayout()
# lineH1 = QHBoxLayout()
# lineH2 = QHBoxLayout()
# lineH3 = QHBoxLayout()

# lineH1.addWidget (questtext, alignment=Qt.AlignCenter)
# lineH2.addWidget (ans, alignment=Qt.AlignCenter)


# line_main.addLayout (lineH1)
# lineH3.addStretch (1)
# Group_q.show()
# Group_a.hide()
# line_main.setSpacing(4)
# lineH3.addWidget (Group_q, stretch=4)
# lineH3.addWidget (Group_a, stretch=4)
# lineH3.addStretch (1)
# line_main.addLayout(lineH3)
# line_main.addLayout (lineH2)

# window.setLayout(line_main)

# RadioGroup = QButtonGroup()
# RadioGroup.addButton(b1)
# RadioGroup.addButton(b2)
# RadioGroup.addButton(b3)
# RadioGroup.addButton(b4)
# #обработка нажатий на переключатели
# window.count_q = -1
# q_list = []
# q_list.append(Question ("Какого цвета нет на флаге России?", "Зеленый","Красный","Синий","Белый"))
# q_list.append(Question ("Какой национальности не существует?", 'Смурфы', 'Энцы', 'Татары', 'Финны'))
# q_list.append(Question ("Национальная хижина якутов", "Ураса","Юрта","Иглу","Хата"))
# answers = [b1, b2, b3, b4]
# ans.clicked.connect(next_question)
# #отображение окна приложения
# window.show()
# my_app.exec_()