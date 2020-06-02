from PyQt5.QtWidgets import *

app = QApplication([])
win = QMainWindow()

win.resize(300, 300)
menu = win.menuBar()
menuFile = menu.addMenu('MENU')
menuExit = menu.addMenu('BYE')

def run():
    bar.showMessage("메뉴 버튼을 눌렀습니다")

bar = win.statusBar()
menuFile.triggered.connect(run)

bye = QAction("NEW", win)
menuFile.addAction(bye)

win.show()
app.exec()
