from PySide2.QtWidgets import QMainWindow, QPushButton, QMessageBox, QApplication
from PySide2.QtCore import QThreadPool
import sys
from settings_window import SettingsWindow

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.threadpool = QThreadPool()
        self.sett_window = None
        self.set_button("Start the\n bot!", self.start_bot, 40, 40, True)
        self.set_button("Settings", self.settings, 160, 40)
        self.init_window()

    def init_window(self):
        self.setWindowTitle("Twitch Chat bot by FF")
        self.setGeometry(100,100,600,400)
        self.show()

    def set_button(self, msg, action, x, y, increase=False, visibility=True):
        btn1 = QPushButton(msg, self)
        btn1.move(x, y)
        btn1.clicked.connect(action)
        if increase:
            btn1.setGeometry(x,y,100, 100)
        btn1.setVisible(visibility)
        return btn1

    def start_bot(self):
        pass

    def settings(self):
        self.sett_window = SettingsWindow()

if __name__ == '__main__':
    myApp = QApplication(sys.argv)
    window = Window()
    sys.exit(myApp.exec_())