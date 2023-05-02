import random

from PyQt5 import QtGui,QtWidgets, QtCore
from PyQt5.QtCore import QUrl, QSize
from PyQt5.QtMultimedia import QMediaPlaylist, QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton, QInputDialog, QMessageBox, \
    QWidget

music = 'Включенная музыка'
player = None


class SecondWindow(QtWidgets.QWidget):
    def __init__(self,
                 parent=None):  # если собрался передавать аргументы, то не забудь их принять (nameofargument, self, parent=None)
        super().__init__(parent, QtCore.Qt.Window)
        self.build()  # ну и передать в открывающееся окно соответственно (nameofargument, self)

    def build(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('NoTittle')


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('NoTittle')

        self.btn = QPushButton('Butn', self)
        self.btn.resize(100, 100)
        self.btn.move(100, 100)
        self.btn.clicked.connect(self.openWin)

    def openWin(self):
        self.secondWin = SecondWindow(
            self)  # здесь можешь передавать аргументы во второе окно (nameofargument, self)
        self.secondWin.show()


def mousePressEvent():
    global music
    global player
    if music == "Выключенная музыка":
        player.play()
        music_play.setIcon(QtGui.QIcon('Unknown.jpeg'))
        music_play.setStyleSheet('opacity:.3')
        music_play.setIconSize(QSize(100, 100))
        window.layout().addWidget(music_play)

        music="Включенная музыка"
    else:
        player.pause()
        music="Выключенная музыка"
        music_play.setIcon(QtGui.QIcon('i.png'))
        music_play.setIconSize(QSize(100, 100))
        window.layout().addWidget(music_play)


def perevod_deneg():
    transaction = QMessageBox()
    transaction.resize(100,100)
    transaction.setWindowTitle('Перевод денежных средств')
    transaction.setText('Введите номер для перевода')
    transaction.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)

    transaction.setDefaultButton(QMessageBox.Ok)
    transaction.setInformativeText('Перевод')
    transaction.setDetailedText('Введите номер и сумму')

    transaction.exec_()


def dopFunction():
    telephone = QMessageBox()
    telephone.resize(100,100)
    telephone.setWindowTitle('Оплата сотовой связи')
    telephone.setText('Введите номер для оплаты')
    telephone.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)

    telephone.setDefaultButton(QMessageBox.Ok)
    telephone.setInformativeText('Сотовая связь')
    telephone.setDetailedText('Введите номер и сумму')

    telephone.exec_()


def Rashody():
    rashod = QMessageBox()
    rashod.resize(100,100)
    rashod.setWindowTitle('Расход денежных средств')
    rashod.setText('Ваш расход за этот месяц ')
    rashod.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)

    rashod.setDefaultButton(QMessageBox.Ok)
    rashod.setInformativeText('Расход денежных средств')
    rashod.setDetailedText('115,876 Руб')

    rashod.exec_()


def Kredit():
    kreditka = QMessageBox()
    kreditka.resize(100,100)
    kreditka.setWindowTitle('Оформление кредита')
    kreditka.setText('Введите данные для оформления')
    kreditka.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)

    kreditka.setDefaultButton(QMessageBox.Ok)
    kreditka.setInformativeText('Кредитные условия')
    kreditka.setDetailedText('Вам одобрен кредит на 1,000,000 Рублей на срок до 25 лет')

    kreditka.exec_()


def NewKard():
    novaya = QMessageBox()
    novaya.resize(100,100)
    novaya.setWindowTitle('Оформление новой дебетовой карты')
    novaya.setText('Выберете платежную систему')
    novaya.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)

    novaya.setDefaultButton(QMessageBox.Ok)
    novaya.setInformativeText('Условия по новой карте')
    novaya.setDetailedText('Заберите карту в любом удобном офисе нашего банка после 12-00 14 мая 2023г.')

    novaya.exec_()


def Valuta():
    kurs = QMessageBox()
    kurs.resize(100,100)
    kurs.setWindowTitle('Курс валют')
    kurs.setText('Узнайте курс валют, которые предлагает Вам наш банк')
    kurs.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)

    kurs.setDefaultButton(QMessageBox.Ok)
    kurs.setInformativeText('Курс валют')
    kurs.setDetailedText('По состоянию на 14 мая 2023г.    USD - 80.00, EUR - 88.62, GBP - 100.10, CNY - 12.20')

    kurs.exec_()


def Bonus_Programm():
    kurs = QMessageBox()
    kurs.resize(100, 100)
    kurs.setWindowTitle('Бонусная программа')
    kurs.setText('Узнайте сколько у вас баллов')
    kurs.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)

    kurs.setDefaultButton(QMessageBox.Ok)
    kurs.setInformativeText('Бонусная программа')
    kurs.setDetailedText('По состоянию на 14 мая 2023г.  1234 баллов')

    kurs.exec_()


def Adress():
    kurs = QMessageBox()
    kurs.resize(100, 100)
    kurs.setWindowTitle('Адреса офисов')
    kurs.setText('Узнайте близлежащие к Вашему менстоположению адреса')
    kurs.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)

    kurs.setDefaultButton(QMessageBox.Ok)
    kurs.setInformativeText('Адреса')
    kurs.setDetailedText('Улица Земляной Вал 27 стр2, 29 стр14 ;Улица Матросская Тишина 16Б стр6')

    kurs.exec_()


def Vault():
    password, ok = QInputDialog.getText(None, 'Auth', 'Введите пароль:', QLineEdit.Password)
    if not ok:
        QMessageBox.warning(None, 'Warning', 'Need input password!')
        quit()

    if password != '4321':
        QMessageBox.warning(None, 'Warning', 'Ошибка!Неверный пароль!')
        quit()

    kurs = QMessageBox()
    kurs.resize(100, 100)
    kurs.setWindowTitle('Ваши счета в иностранной валюте')
    kurs.setText('Узнайте сколько у Вас лежит денежных средств в иностранной валюте')
    kurs.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)

    kurs.setDefaultButton(QMessageBox.Ok)
    kurs.setInformativeText('Иностранная валюта')
    kurs.setDetailedText('По состоянию на 14 мая 2023г.    USD - 800.00, EUR - 3,210.00, GBP - 1400.00, CNY - 12500.00')

    kurs.exec_()


if __name__ == "__main__":
    app = QApplication([])
    window = QMainWindow()
    window.setFixedSize(800, 800)

    password, ok = QInputDialog.getText(None, 'Auth', 'Здравствуйте,Даниил! Введите пароль:', QLineEdit.Password)
    if not ok:
        QMessageBox.warning(None, 'Warning', 'Need input password!')
        quit()

    if password != '1234':
        QMessageBox.warning(None, 'Warning', 'Ошибка!Неверный пароль!')
        quit()

    playlist = QMediaPlaylist()
    tracks = [QMediaContent(QUrl.fromLocalFile("/Users/lureterio/PycharmProjects/BankApp/1.mp3")),
              QMediaContent(QUrl.fromLocalFile("/Users/lureterio/PycharmProjects/BankApp/2.mp3")),
              QMediaContent(QUrl.fromLocalFile("/Users/lureterio/PycharmProjects/BankApp/3.mp3")),
              QMediaContent(QUrl.fromLocalFile("/Users/lureterio/PycharmProjects/BankApp/4.mp3")),
              QMediaContent(QUrl.fromLocalFile("/Users/lureterio/PycharmProjects/BankApp/5.mp3")),

    ]
    random.shuffle(tracks)

    for track in tracks:
        playlist.addMedia(track)

    player = QMediaPlayer()
    player.setPlaylist(playlist)
    player.playlist().setCurrentIndex(0)
    player.play()

    menu = QLabel()
    menu.move(0,0)
    menu.setFixedSize(800, 800)
    menu.setStyleSheet("background-color:#E0FFFF")
    window.layout().addWidget(menu)

    logo = QPushButton()
    logo.move(600,0)
    logo.setFixedSize(200,100)
    logo.setIcon(QtGui.QIcon('logo.png'))
    logo.setIconSize(QSize(200, 100))
    window.layout().addWidget(logo)

    balans = QLabel()
    balans.setText('Карта Mir Gold      1234,56 Руб')
    balans.move(0,100)
    balans.setFixedSize(230,100)
    balans.setStyleSheet("background-color:#3441DA")
    window.layout().addWidget(balans)

    balans2 = QLabel()
    balans2.setText('Карта VISA Classic     1234,56 Руб')
    balans2.move(0,210)
    balans2.setFixedSize(230,100)
    balans2.setStyleSheet("background-color:#3441DA")
    window.layout().addWidget(balans2)

    perevod = QPushButton()
    perevod.setText('Перевод денежных средств')
    perevod.move(0,400)
    perevod.setFixedSize(230,100)
    perevod.setStyleSheet("background-color:#423C63")
    window.layout().addWidget(perevod)
    perevod.clicked.connect(lambda: perevod_deneg())

    spec = QPushButton()
    spec.setText('Оплата сотовой связи')
    spec.move(280,400)
    spec.setFixedSize(230,100)
    spec.setStyleSheet("background-color:#423C63")
    window.layout().addWidget(spec)
    spec.clicked.connect(lambda: dopFunction())

    rashody = QPushButton()
    rashody.setText('Оцените свои расходы за месяц')
    rashody.move(550,400)
    rashody.setFixedSize(230,100)
    rashody.setStyleSheet("background-color:#423C63")
    window.layout().addWidget(rashody)
    rashody.clicked.connect(lambda: Rashody())

    kredit = QPushButton()
    kredit.setText('Кредитная карта')
    kredit.move(0,510)
    kredit.setFixedSize(230,100)
    kredit.setStyleSheet("background-color:#423C63")
    window.layout().addWidget(kredit)
    kredit.clicked.connect(lambda: Kredit())

    newkards = QPushButton()
    newkards.setText('Новая дебетовая карта')
    newkards.move(280,510)
    newkards.setFixedSize(230,100)
    newkards.setStyleSheet("background-color:#423C63")
    window.layout().addWidget(newkards)
    newkards.clicked.connect(lambda: NewKard())

    kursvalut = QPushButton()
    kursvalut.setText('Курс валют')
    kursvalut.move(550,510)
    kursvalut.setFixedSize(230,100)
    kursvalut.setStyleSheet("background-color:#423C63")
    window.layout().addWidget(kursvalut)
    kursvalut.clicked.connect(lambda: Valuta())

    bonus = QPushButton()
    bonus.setText('Бонусная программа')
    bonus.move(0, 620)
    bonus.setFixedSize(230, 100)
    bonus.setStyleSheet("background-color:#423C63")
    window.layout().addWidget(bonus)
    bonus.clicked.connect(lambda: Bonus_Programm())

    adres = QPushButton()
    adres.setText('Близлежащие офисы банка')
    adres.move(280, 620)
    adres.setFixedSize(230, 100)
    adres.setStyleSheet("background-color:#423C63")
    window.layout().addWidget(adres)
    adres.clicked.connect(lambda: Adress())

    vault = QPushButton()
    vault.setText('Счета в иностранной валюте')
    vault.move(550, 620)
    vault.setFixedSize(230, 100)
    vault.setStyleSheet("background-color:#423C63")
    window.layout().addWidget(vault)
    vault.clicked.connect(lambda: Vault())

    music_play = QPushButton()
    music_play.move(0,0)
    music_play.setFixedSize(50,50)
    music_play.setIcon(QtGui.QIcon('Unknown.jpeg'))
    music_play.setIconSize(QSize(225, 225))
    window.layout().addWidget(music_play)
    music_play.clicked.connect(lambda: mousePressEvent())

    window.show()
    app.exec_()