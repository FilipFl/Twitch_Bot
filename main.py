from PySide2.QtWidgets import QMainWindow, QPushButton, QMessageBox, QApplication
from PySide2.QtCore import QThreadPool
import sys
from settings_window import SettingsWindow
from bot import Bot
from worker import Worker

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.threadpool = QThreadPool()
        self.sett_window = None
        self.bot = None
        self.worker = None
        self.start_btn = self.set_button("Start the\n bot!", self.start_bot, 40, 40, True)
        self.set_button("Settings", self.settings, 160, 40)
        self.stop_btn = None
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
            btn1.setGeometry(x,y,80, 80)
        btn1.setVisible(visibility)
        return btn1

    def start_bot(self):
        self.start_btn.setVisible(False)
        self.bot = Bot()
        worker = Worker(self.bot.listen_chat)
        self.worker = worker
        self.threadpool.start(worker)
        self.stop_btn = self.set_button("Stop the bot!", self.worker.kill, 40, 40, True)
        self.stop_btn.clicked.connect(self.stop_bot)

    def settings(self):
        self.sett_window = SettingsWindow()

    def goodbye(self):
        self.bot.networking.send_message("Bot is out!")
        self.stop_btn.setVisible(False)
        self.start_btn.setVisible(True)

    def stop_bot(self):
        self.goodbye()


if __name__ == '__main__':
    myApp = QApplication(sys.argv)
    window = Window()
    sys.exit(myApp.exec_())