from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,  QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
from random import*




class Main():
    def __init__(self, question, right_answer, answer2, answer3, answer4):
        self.question=question
        self.right_answer=right_answer
        self.answer2=answer2
        self.answer3=answer3
        self.answer4=answer4

one=Main('Какая страна больше',  'Россия', 'Португалия', 'Франция', 'Канада')
two=Main('В каком году произошло восстание Пугачева', '1773', '1647', '1835', '1947')
three=Main('Сколько клеток на шахматной доске', '64', '32', '41', '95')
four=Main('Сколько дней в году', '365', '654', '746', '678')
five=Main('К какому отряду относятся киты', 'Парнокопытные', 'Непарнокопытные', 'Млекопитающие', 'Хищные')
six=Main('Где находится Бразилия?', 'Южная Америка', 'Россия', 'Северная Америка', 'Европа')
seven=Main('В это озеро нашей страны впадает множество рек, а вытекает из него только одна — Ангара?', 'Байкал', 'Ладожское', 'Онежское', 'Селигер')
eight=Main('Какое государство самое маленькое в мире?', 'Ватикан', 'Панама', 'Израиль', 'Москва')
nine=Main('Как давно, по мнению большинства учёных, появились время, материя и энергия?', '13,7 миллиардов лет назад', '20 миллиардов', '10 миллиардов', '34 миллиардов')
ten=Main('Масса какой из планет в списке в 2,47 раза превышает суммарную массу всех остальных планет Солнечной системы?', 'Юпитер', 'Сатурн', 'Венера', 'Марс')

list2=[one, two, three, four, five, six, seven, eight, nine, ten]
main_list=list2.copy()
shuffle(main_list)
rights=0
 
def change_variants():
    variants.hide()
    check.show()
    btn_ok.setText('Следующий вопрос')

def change_check():
    check.hide()
    variants.show()
    btn_ok.setText('Ответить')
    btns.setExclusive(False)
    btn1.setChecked(False)
    btn2.setChecked(False)
    btn3.setChecked(False)
    btn4.setChecked(False)
    btns.setExclusive(True)

def test():
    if btn_ok.text()=='Ответить':
        check_answer()
    else:
        next_question()

def ask(question:Main):
    shuffle(answers)
    answers[0].setText(question.right_answer)
    answers[1].setText(question.answer2) 
    answers[2].setText(question.answer3)
    answers[3].setText(question.answer4)
    text.setText(question.question)
    correct.setText(question.right_answer)
    main_list.remove(question)

def check_answer():
    global rights
    if answers[0].isChecked():
        show_correct('Правильно')
        rights+=1
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('Неправильно')


def show_correct(logic):
    right.setText(logic)
    change_variants()


def next_question():
    if len(main_list)==0:
        stata(rights)

    else:    
        ask(main_list[randint(0, len(main_list)-1)])
        change_check()


def stata(rights):
    statistics=QMessageBox()
    statistics.setWindowTitle('Результаты')
    statistics.setText(f'Количество вопросов {len(list2)}\nКоличество правильно ответов: {rights}\nПроцент правильных ответов: {rights/len(list2)*100}%')
    statistics.exec_()


app=QApplication([])
main_win=QWidget()
main_win.setWindowTitle('Memory Card')
text=QLabel('Вопрос')
btn_ОK = QPushButton( 'Ответить')
variants=QGroupBox('варианты ответов')
btns=QButtonGroup()
check=QGroupBox('Результаты')
right=QLabel('Правильно/Неправильно')
correct=QLabel('Правильно')
btn1=QRadioButton('11')
btn2=QRadioButton('12')
btn3=QRadioButton('13')
btn4=QRadioButton('27')
btns.addButton(btn1)
btns.addButton(btn2)
btns.addButton(btn3)
btns.addButton(btn4)
answers=[btn1, btn2, btn3, btn4]
btn_ok=QPushButton('Ответить')
line1=QHBoxLayout()

line2=QHBoxLayout()
line_ok=QHBoxLayout()
line_right=QVBoxLayout()
main_layout=QVBoxLayout()
text_layout=QHBoxLayout()


card_layout=QVBoxLayout()

line1.addWidget(btn1, alignment=Qt.AlignCenter)
line1.addWidget(btn2, alignment=Qt.AlignCenter)
line2.addWidget(btn3, alignment=Qt.AlignCenter)
line2.addWidget(btn4, alignment=Qt.AlignCenter)

line_ok.addStretch(1)
line_ok.addWidget(btn_ok, stretch=70)
line_ok.addStretch(1)

line_right.addWidget(right, alignment=Qt.AlignLeft|Qt.AlignTop)
line_right.addWidget(correct, alignment=Qt.AlignCenter)

line_checking=QHBoxLayout()
line_checking.addLayout(line_right)
check.setLayout(line_checking)
line30=QHBoxLayout()
line30.addWidget(check)

text_layout.addWidget(text, alignment=Qt.AlignCenter)

main_layout.addLayout(line1)
main_layout.addLayout(line2)

variants.setLayout(main_layout)

line40=QVBoxLayout()
line40.addWidget(variants)

card_layout.addLayout(text_layout)
card_layout.addLayout(line40)
card_layout.addLayout(line30)
card_layout.addLayout(line_ok)


main_win.setLayout(card_layout)

btn_ok.clicked.connect(test)

ask(main_list[0])

check.hide()

main_win.show()
app.exec_()