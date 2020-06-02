from PyQt5.QtWidgets import *

app = QApplication([])
win = QWidget()

form = QFormLayout()
win.setLayout(form)

formEdit = QLineEdit()
btn = QPushButton("push")
form.addRow("name", formEdit)
form.addRow(btn)

win.show()
app.exec()