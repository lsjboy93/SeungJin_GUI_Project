from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QPushButton('top'))
layout.addWidget(QPushButton('jgl'))
layout.addWidget(QPushButton('mid'))
layout.addWidget(QPushButton('bot'))
layout.addWidget(QPushButton('sup'))
window.setLayout(layout)
window.show()
app.exec()
