from PyQt5.QtWidgets import *

app = QApplication([])
win = QMainWindow()

win.resize(400, 400)
label = QLabel("라면이 생각나는 밤", win)
label.adjustSize()

win.show()
app.exec()