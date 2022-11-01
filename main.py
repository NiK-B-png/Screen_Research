from pynput import mouse
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QFileDialog
from PIL import Image
from PIL import ImageGrab
import re
import pytesseract
import difflib
import PySimpleGUI as sg
import sys
#import pyscreenshot as ImageGrab2
#######################################

#Сохранение результатов сравнения в файл

file_path = 'RESULT.txt'
sys.stdout = open(file_path, "w")
#
#
############################
#Окно с кнопкой №1

sg.theme('DarkAmber')    # Вопрос к пользователю

layout = [[sg.Text('Продолжить запуск Screen Research?                            ')],
          [sg.Button('OK')]]#, sg.Exit()]]

window = sg.Window('Screen Research', layout)
event, values = window.read()
window.close()

if event == sg.WIN_CLOSED or event == 'WIN_CLOSED':

    raise SystemExit(1) # Завершение Screen Research

window.close()


###########################################

###########################################

#Окно №2 Выделите анализируемую область №1
sg.theme('DarkAmber')    # Вопрос к пользователю

layout = [[sg.Text('Готовы выделить анализируемую область №1 ?')],
          [sg.Button('OK')]]#, sg.Exit()]]

window = sg.Window('Screen Research', layout)
event, values = window.read()
window.close()

if event == sg.WIN_CLOSED or event == 'WIN_CLOSED':

    raise SystemExit(1) # Завершение Screen Research

window.close()
#

#Определение координат выделенной области

f = open('Coordinata1.txt', 'w', encoding='utf-8')

def on_click_1(x, y, button, pressed):
    # Сохраняем значения координат
    f = open('Coordinata1.txt', 'a', encoding='utf-8')
    print('{}' '{}'.format('Нажатие |' if pressed else 'Отпуск  |', (x, y)), file = f )
    if not pressed:
        #Останов слежения за курсором
        return False
    f.close()
f.close()

with mouse.Listener(on_click=on_click_1) as listener:
    listener.join()

#Читаем координаты из файла (.txt или .csv)

file = open('Coordinata1.txt')
values = file.read().split("\n")
data = []

for key in values:
    value = re.findall(r"[-+]?\d*\.\d+|\d+", key)
    if value != []:
        data.append(value)
#print(data) #Необязательно печатать

X1 = data[0][0]
Y1 = data[0][1]
X2 = data[1][0]
Y2 = data[1][1]
# Расчёт по сохранённым координатам
def coordstore_1():
    f=open('Coordinata1.txt')
    data.append(value)
    X1 = data[0][0]
    Y1 = data[0][1]
    X2 = data[1][0]
    Y2 = data[1][1]
    #print(X1+',', Y1+',', X2+',', Y2+',') #Необязательно печатать
    return(X1, Y1, X2, Y2)
coordstore_1()

def screenshot_1():
    #import pyscreenshot as ImageGrab2
    # Выбор части экрана
    if __name__ == '__main__':
        im = ImageGrab.grab(bbox=tuple(map(int, coordstore_1())))  # X1,Y1,X2,Y2
        im.save('screen1.png')
        #screenshot_1()
screenshot_1()

#print('Screen OK')

##
########
#############
#################_____Повтор
#############
########
##

#Окно №3 Выделите анализируемую область №3
sg.theme('DarkAmber')    # Вопрос к пользователю

layout = [[sg.Text('Готовы выделить анализируемую область №2 ?')],
          [sg.Button('OK')]]#, sg.Exit()]]

window = sg.Window('Screen Research', layout)
event, values = window.read()
window.close()

if event == sg.WIN_CLOSED or event == 'WIN_CLOSED':

    raise SystemExit(1) # Завершение Screen Research

window.close()
#

f = open('Coordinata2.txt', 'w', encoding='utf-8')

def on_click_2(x, y, button, pressed):
    # Сохраняем значения координат
    f = open('Coordinata2.txt', 'a', encoding='utf-8')
    print('{}' '{}'.format('Нажатие |' if pressed else 'Отпуск  |', (x, y)), file = f )
    if not pressed:
        #Останов слежения за курсором
        return False
    f.close()
f.close()

with mouse.Listener(on_click=on_click_2) as listener:
    listener.join()

#Читаем координаты из файла (.txt или .csv)

file = open('Coordinata2.txt')
values = file.read().split("\n")
data = []

for key in values:
    value = re.findall(r"[-+]?\d*\.\d+|\d+", key)
    if value != []:
        data.append(value)
#print(data)#Необязательно печатать

X1 = data[0][0]
Y1 = data[0][1]
X2 = data[1][0]
Y2 = data[1][1]
# Расчёт по сохранённым координатам
def coordstore_2():
    f=open('Coordinata2.txt')
    data.append(value)
    X1 = data[0][0]
    Y1 = data[0][1]
    X2 = data[1][0]
    Y2 = data[1][1]
    #print(X1+',', Y1+',', X2+',', Y2+',')#Необязательно печатать
    return(X1, Y1, X2, Y2)
coordstore_2()
#import pyscreenshot as ImageGrab2
def screenshot_2():
    #import pyscreenshot as ImageGrab2
    # Выбор части экрана
    if __name__ == '__main__':
        im = ImageGrab.grab(bbox=tuple(map(int, coordstore_2())))  # X1,Y1,X2,Y2
        im.save('screen2.png')
        #screenshot_2()
screenshot_2()

#print('Next screen OK')

#
####
###########
######################____________Распознаём
###########
####
#


# Распознаём текст из ".png" файла
img = Image.open('screen1.png')
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

text = pytesseract.image_to_string(img, lang = "rus") #Для текста на русском


with open('text1.txt', 'w') as f:# r'C:\Users\NiK\Downloads\Загруз'
    f.write(text.strip())

img = Image.open('screen2.png')
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

text = pytesseract.image_to_string(img, lang = "rus") #Для текста на русском
#print(text.strip())

with open('text2.txt', 'w') as f:
    f.write(text.strip())

#Сравнение текстов из файлов "text1.txt" и "text2.txt" вариант №1

file1 = "text1.txt"
file2 = "text2.txt"

diff = difflib.ndiff(open(file1).readlines(),open(file2).readlines())
print(''.join(diff))

#######################################


#Окно с кнопкой №4

sg.theme('DarkAmber')    # Сообщение для пользователя

layout = [[sg.Text('Откройте файл RESULT.txt                    '), sg.Button('OK')]]#, sg.Exit()]]#, sg.Exit()]]

window = sg.Window('Screen Research', layout)
event, values = window.read()
window.close()

if event == sg.WIN_CLOSED or event == 'WIN_CLOSED':

    raise SystemExit(1) # Завершение Screen Research
window.close()



def zap_1():
    file_path = 'RESULT.txt'
    sys.stdout = open(file_path, "a")
zap_1()

#############################################################################################

#Открываем RESULT

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Screen Reserch")
        self.setGeometry(300, 250, 1500, 1500)

        self.text_edit = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.createMenuBar()
    def createMenuBar(self):
        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)

        fileMenu = QMenu("&Файл", self)
        self.menuBar.addMenu(fileMenu)

        fileMenu.addAction('Открыть', self.action_clicked)
        fileMenu.addAction('Сохранить', self.action_clicked)

    @QtCore.pyqtSlot()
    def action_clicked(self):
        action = self.sender()
        print("Action: " + action.text())
        if action.text() == "Открыть":
            fname = QFileDialog.getOpenFileName(self)[0]

            f = open(fname, 'r')
            with f:
                data = f.read()
                self.text_edit.setText(data)

        elif action.text() == "Сохранить":
            print("Save")


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())

    if __name__ == "__main__":
        main()
application()

