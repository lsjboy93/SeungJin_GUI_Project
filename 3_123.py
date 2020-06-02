from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()

mainLayout = QVBoxLayout()
headLayout = QHBoxLayout()
bodyLayout = QVBoxLayout()
mainLayout.addLayout(headLayout)
mainLayout.addLayout(bodyLayout)

headLayout.addWidget(QPushButton("1"))
headLayout.addWidget(QPushButton("2"))
headLayout.addWidget(QPushButton("3"))

bodyLayout.addWidget(QPushButton("1"))
bodyLayout.addWidget(QPushButton("2"))
bodyLayout.addWidget(QPushButton("3"))

window.setLayout(mainLayout)
window.show()
app.exec()