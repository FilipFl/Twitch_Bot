from PySide2.QtWidgets import QMainWindow, QPushButton, QApplication, QLineEdit


class SettingsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.set_button("Save", self.save_data, 40, 150)
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(40, 30)
        self.textbox1.resize(200, 20)
        self.init_window()

    def init_window(self):
        self.setWindowTitle("Settings")
        self.setGeometry(300,200,300,300)
        self.show()

    def set_button(self, msg, action, x, y, visibility=True):
        btn1 = QPushButton(msg, self)
        btn1.move(x, y)
        btn1.clicked.connect(action)
        btn1.setVisible(visibility)
        return btn1

    def save_data(self):
        pass
