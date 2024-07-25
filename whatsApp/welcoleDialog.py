import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QDialog, QDialogButtonBox, QVBoxLayout, QLabel
from ui_welcomeDiag import Ui_Dialog


class WelcomeDiag(QWidget, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog
        self.ui.setupUi(self)
        self.setWindowTitle("Excel Seçim Ekranı")
        self.setWindowIcon(QIcon("whatsApp/wpicon.ico"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    diag = QDialog()
    uw = WelcomeDiag(diag)








