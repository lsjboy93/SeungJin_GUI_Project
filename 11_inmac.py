from PyQt5.QtWidgets import *

app = QApplication([])
win = QMainWindow()

app.setApplicationName("My Friends")
win.resize(400, 400)
bar = win.statusBar()
bar.showMessage("인맥을 관리합시다.")

mb = win.menuBar()
menu = mb.addMenu("메뉴")

menuAdd = QAction("추가", win)
menuRemove = QAction("제거", win)
bye = QAction("종료", win)

menu.addAction(menuAdd)
menu.addAction(menuRemove)
mb.addAction(bye)

main = QWidget()
win.setCentralWidget(main)

addBtn = QPushButton("추가")
removeBtn = QPushButton("제거")
btnLayout = QHBoxLayout()
btnLayout.addWidget(addBtn)
btnLayout.addWidget(removeBtn)

form = QFormLayout()
name = QLineEdit()
form.addWidget(QLabel("인맥을 관리합시다"))
form.addRow("name", name)
form.addRow(btnLayout)

main.setLayout(form)

def add():
    str = name.text()
    if len(str) == 0 : return
    
    global names
    if names.count(str) == 1 :
        bar.showMessage("이미 친구입니다.")
    else :
        bar.showMessage("환영합니다. 나의 인맥")
        names.append(str)
        print(names)

def remove():
    str = name.text()
    if len(str) == 0 : return
    
    global names
    if names.count(str) == 0:
        bar.showMessage(str + ", 그는 내 친구가 아닙니다.")
    else:
        bar.showMessage(str + ", 더 이상 내 친구가 아닙니다.")
        names.remove(str)
        print(names)
    
def byebye():
    quit()
    
names = ["inho", "donghun", "carrot", "hwan"]

addBtn.clicked.connect(add)
removeBtn.clicked.connect(remove)

menuAdd.triggered.connect(add)
menuRemove.triggered.connect(remove)
bye.triggered.connect(byebye)

win.show()
app.exec()
