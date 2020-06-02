from PyQt5.QtWidgets import *

app = QApplication([])
win = QMainWindow()

menu = win.menuBar()
menu.addMenu("ABC")
menu.addMenu("BTS")

main = QWidget()
win.setCentralWidget(main)

label = QLabel("HI", main)

win.show()
app.exec()
