import sys
import time
import win32gui
from PySide2.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QLineEdit,
    QProgressBar,
    QSystemTrayIcon,
    QMenu,
)
from PySide2.QtGui import QIcon
from PySide2.QtUiTools import QUiLoader, loadUiType
from PySide2.QtCore import SIGNAL, QObject, QCoreApplication, Qt

from events.ui.load_ui import loadUi
from events.backup import copia_pastas


class SystemTrayIcon(
    QSystemTrayIcon,
):
    def __init__(self, icon, parent=None):
        QSystemTrayIcon.__init__(self, icon, parent)
        self.menu = QMenu(parent)
        restoreAction = self.menu.addAction("Restaurar Janela")
        exitAction = self.menu.addAction("Exit")
        self.setContextMenu(self.menu)
        QObject.connect(restoreAction, SIGNAL("triggered()"), self.restore)
        QObject.connect(exitAction, SIGNAL("triggered()"), self.exit)

    def exit(self):
        QCoreApplication.exit()

    def restore(self):
        self.parent().show()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("user_interface/form.ui", self)
        self.setWindowIcon(QIcon("assets/icon.ico"))
        self.setWindowTitle("Simple BackUp")
        self.resize(650, 200)

        self.tray_icon = SystemTrayIcon(QIcon("assets/icon.ico"), self)

        self.input_origem = self.findChild(QLineEdit, "lineEdit")
        self.input_destino = self.findChild(QLineEdit, "lineEdit_2")

        self.progresso = self.findChild(QProgressBar, "progressBar")

        self.btn_realiza = self.findChild(QPushButton, "pushButton")
        self.btn_realiza.clicked.connect(self.realiza_copia)

        self.btn_minimiza = self.findChild(QPushButton, "pushButton_2")
        self.btn_minimiza.clicked.connect(self.minimiza_bandeja)

        self.tray_icon.show()
        self.show()

    def realiza_copia(self, msg):
        self.btn_realiza.setEnabled(False)
        origem = self.input_origem.text()
        destino = self.input_destino.text()
        self.define_progresso()
        copia_pastas(origem, destino)

    def define_progresso(self):
        for i in range(1, 101):
            self.progresso.setValue(i)
            QApplication.processEvents()
            time.sleep(0.1)
        self.progresso.setValue(0)
        self.btn_realiza.setEnabled(True)

    def minimiza_bandeja(self):
        self.hide()
        self.setWindowFlags(self.windowFlags() & ~Qt.Tool)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()

    sys.exit(app.exec_())
