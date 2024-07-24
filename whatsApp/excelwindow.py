# This Python file uses the following encoding: utf-8
import sys
import os


from PySide6 import QtCore
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QDialog, QDialogButtonBox, QVBoxLayout, QLabel
from ui_excel import Ui_Form


chosen_columns=[]
chars = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
class ExcelMainWindow(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Excel Seçim Ekranı")
        self.setWindowIcon(QIcon("whatsApp/wpicon.ico"))

        self.ui.ch_name_bn.clicked.connect(self.getName)
        self.ui.ch_number_btn.clicked.connect(self.getNumber)
        self.ui.ch_cost_btn.clicked.connect(self.getCost)
        self.ui.ch_date_btn.clicked.connect(self.getDate)
        self.ui.tableWidget.clicked.connect(self.tableCick)
        self.ui.add_to_opage_btn.clicked.connect(self.addClicked)
        self.ui.add_to_opage_btn.clicked.connect(self.clearData)




    def addClicked(self):
        chosen_columns1 = self.ui.name_column_label.text()+";"+self.ui.number_column_label.text()+";"+self.ui.total_column_label.text()+";"+self.ui.date_column_label.text()

        if len(chosen_columns1) < 4 or "-" in chosen_columns1:
            dg = CustomDialog2()
            dg.exec()
        else:
            self.ui.chosen_columns_label.setText(chosen_columns1)
            chosen_columns = chosen_columns1.split(";")
            self.close()
            return chosen_columns1



    def clearData(self):
        chosen_columns.clear()
    def tableCick(self):
        return self.ui.tableWidget.currentColumn()



    def getName(self):

        nameColunm = chars[self.ui.tableWidget.currentColumn()]

        self.ui.name_column_label.setText(str(nameColunm))
        if not nameColunm in chosen_columns:
            chosen_columns.append(nameColunm)
        else:
            dlg = CustomDialog()
            dlg.exec()
    def getNumber(self):
        nameColunm = chars[self.ui.tableWidget.currentColumn()]

        self.ui.number_column_label.setText(str(nameColunm))
        if not nameColunm in chosen_columns:
            chosen_columns.append(nameColunm)
        else:
            dlg = CustomDialog()
            dlg.exec()
    def getCost(self):
        nameColunm = chars[self.ui.tableWidget.currentColumn()]

        self.ui.total_column_label.setText(str(nameColunm))
        if not nameColunm in chosen_columns:
            chosen_columns.append(nameColunm)
            self.ui.date_column_label.setText("NONE")
        else:
            self.ui.date_column_label.setText("NONE")
            dlg = CustomDialog()
            dlg.exec()
    def getDate(self):
        nameColunm = chars[self.ui.tableWidget.currentColumn()]

        self.ui.date_column_label.setText(str(nameColunm))
        if not nameColunm in chosen_columns:
            chosen_columns.append(nameColunm)
        else:
            dlg = CustomDialog()
            dlg.exec()




    def closem(self):
        print("kapandı")




class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hatalı Seçim Yapınz !")
        self.setWindowIcon(QIcon("whatsApp/wpicon.ico"))
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()

        message = QLabel("Aynı Kolonu Seçemezsiniz")
        message.setStyleSheet("padding: 10px")
        message.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

class CustomDialog2(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Eksik Bilgi Mevcut !")
        self.setWindowIcon(QIcon("whatsApp/wpicon.ico"))
        self.layout = QVBoxLayout()
        message = QLabel("Lütfen Bilgileri içeren bütün kolonları seçin")
        message.setStyleSheet("padding: 20px")
        message.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(message)

        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = ExcelMainWindow()
    widget.show()
    sys.exit(app.exec())
