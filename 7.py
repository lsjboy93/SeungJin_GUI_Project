from PyQt5.QtWidgets import *

app = QApplication([])
win = QWidget()

form = QFormLayout()
win.setLayout(form)

formEdit1 = QLineEdit()
form.addRow("name", formEdit1)

formEdit2 = QLineEdit()
formButton = QPushButton("나이 확인")

formLayout = QHBoxLayout()
formLayout.addWidget(formEdit2)
formLayout.addWidget(formButton)
form.addRow("age", formLayout)

formLabel = QLabel("경고 : 나이가 너무 많습니다.")
form.addWidget(formLabel)

formLabel.setVisible(False)
formButton2 = QPushButton("회원가입")
form.addRow(formButton2)

def checkAge():
    age = formEdit2.text()
    if age.isdigit() == False: return
    age = int(age)
    
    if age >= 25: formLabel.setVisible(True)
    else: formLabel.setVisible(False)

def checkName():
    name = formEdit1.text()
    n = len(name)
    if 1<= n <= 4 : pass
    else:
        msg = QMessageBox()
        msg.setText("이름은 1 ~ 4 글자 필수")
        msg.exec()
        
formButton.clicked.connect(checkAge)
formButton2.clicked.connect(checkName)

app.setApplicationName("MY WORLD")

win.show()
app.exec()