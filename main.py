from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton

app = QApplication([])

main_win = QWidget()

main_win.show()
main_win.setWindowTitle('Цікава назва')
main_win.resize(500, 500)

q = QLabel('Як звали першого ютуб-блогера, який набрав 100000000 підписників?')

a1 = QRadioButton('SlivkiShow,')
a2 = QRadioButton('Рет і Лінк')
a3 = QRadioButton('PewDiePie')
a4 = QRadioButton('TheBrianMaps')
a5 = QRadioButton('EeOneGuy')
a6 = QRadioButton('Mister Max')

Hline1 = QHBoxLayout()
HLine2 = QHBoxLayout()
HLine3 = QHBoxLayout()
HLine4 = QHBoxLayout()
VLine = QVBoxLayout()

Hline1.addWidget(q,alignment=Qt.AlignCenter)
HLine2.addWidget(a1,alignment=Qt.AlignCenter)
HLine2.addWidget(a2,alignment=Qt.AlignCenter)
HLine3.addWidget(a3,alignment=Qt.AlignCenter)
HLine3.addWidget(a4,alignment=Qt.AlignCenter)
HLine4.addWidget(a5,alignment=Qt.AlignCenter)
HLine4.addWidget(a6,alignment=Qt.AlignCenter)
VLine.addLayout(Hline1)
VLine.addLayout(HLine2)
VLine.addLayout(HLine3)
VLine.addLayout(HLine4)

main_win.setLayout(VLine)

def win():
    molodec = QMessageBox()
    molodec.setText('Правильно!!! Ви виграли зустріч з творцями нашого каналу!!!')
    molodec.exec_()

def lose():
    nemolodec = QMessageBox()
    nemolodec.setText('Ні, це PewDiePie, ти виграв фірм. плакат')
    nemolodec.exec_()

a1.clicked.connect(lose)
a2.clicked.connect(lose)
a3.clicked.connect(win)
a4.clicked.connect(lose)
a5.clicked.connect(lose)
a6.clicked.connect(lose)

app.exec_()