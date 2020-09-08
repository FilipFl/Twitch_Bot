from PySide2.QtWidgets import QMainWindow, QPushButton, QApplication, QLineEdit
import os

class SettingsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.set_button("Save", self.save_data, 40, 150)
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(40, 30)
        self.textbox1.resize(200, 20)
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(40, 75)
        self.textbox2.resize(200, 20)
        self.textbox3 = QLineEdit(self)
        self.textbox3.move(40, 120)
        self.textbox3.resize(200, 20)
        self.read_data()
        self.init_window()

    def init_window(self):
        self.setWindowTitle("Settings")
        self.setGeometry(300,200,300,300)
        self.show()

    def read_data(self):
        if os.path.exists("./data/settings.txt"):
            f = open("./data/settings.txt", "r")
            read = f.readlines()
            self.textbox1.setText(read[0])
            self.textbox2.setText(read[1])
            self.textbox3.setText(read[2])
            f.close()
        else:
            self.textbox1.setText("OAuth Token")
            self.textbox2.setText("Account name")
            self.textbox3.setText("Channel")

    def set_button(self, msg, action, x, y, visibility=True):
        btn1 = QPushButton(msg, self)
        btn1.move(x, y)
        btn1.clicked.connect(action)
        btn1.setVisible(visibility)
        return btn1

    def save_data(self):
        f = open("data/settings.txt", "w")
        f.write(self.textbox1.text()+"\n")
        f.write(self.textbox2.text()+"\n")
        f.write(self.textbox3.text()+"\n")
        f.close()
        self.close()
