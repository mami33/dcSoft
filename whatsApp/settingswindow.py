import sys
import os
import time

this_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.split(this_path)[0])
print(os.path.split(this_path)[0])
from configparser import ConfigParser
from PySide6 import QtCore
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QDialog, QDialogButtonBox, QVBoxLayout, QLabel, \
    QSizePolicy
from ui_settings import Ui_Form

class SettingsWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.i = 0
        self.setupUi(self)
        self.setWindowTitle('Ayarlar')
        self.setWindowIcon(QIcon('wpicon.ico'))
        self.con  = ConfigParser()
        self.con.read(os.path.split(this_path)[0]+'\\whatsapp_config.ini')
        self.con.sections()
        self.name_label.setPlaceholderText("İsmin açıklayıcı olması yeterlidir.(Fatura baş. değil) ")
        self.name_label.setFocus()
        self.iban_label.setPlaceholderText("IBAN bilgilerini eksiksiz giriniz")
        self.number_label.setPlaceholderText("Şirket numarası yada ceptelefonunu girin")
        self.isim.setText(self.isim.text() + " ("+ self.con.get("comp_name", 'name')+ ")")
        self.numara.setText(self.numara.text() + " (" + self.con.get("comp_name", 'number') + ")")
        self.iban.setText(self.iban.text() + " (" + self.con.get("comp_name", 'iban') + ")")

        self.reset_btn.clicked.connect(self.reset_button)
        self.show()
        self.save_btn.clicked.connect(self.save)
        self.cancel_btn.clicked.connect(self.cancel)
    def reset_button(self,event):
        self.i += 1
        self.reset_btn.setText("Sıfırla :" + str(3 - self.i))
        if self.i == 3:
            self.name_label.clear()
            self.iban_label.clear()
            self.number_label.clear()
            self.i = 0
            self.con["comp_name"]["name"] = ""
            self.con["comp_name"]["alici"] = ""
            self.con["comp_name"]["iban"] = ""
            self.con["comp_name"]["number"] = ""
            self.con["version"]["firstlog"] = ""
            with open(os.path.split(this_path)[0] + '\\whatsapp_config.ini', 'w') as configfile:
                self.con.write(configfile)

            self.close()
            sys.exit()
    def save(self):
        if self.name_label.toPlainText() == '' or self.iban_label.toPlainText() == '' or self.number_label.toPlainText() == '':
            dialog = QDialog(self)
            dialog.setWindowTitle("Eksik Bilgiler Var")
            label =QLabel("Tüm bilgileri eksiksiz girin !")
            layout = QVBoxLayout()
            label.setStyleSheet("background-color: rgb(255, 255, 255);")
            layout.addWidget(label)
            dialog.setLayout(layout)
            dialog.exec()
        else:

            self.con["comp_name"]["name"] = self.name_label.toPlainText()
            self.con["comp_name"]["alici"] = self.name_label.toPlainText()
            self.con["comp_name"]["iban"] = self.iban_label.toPlainText()
            self.con["comp_name"]["number"] = self.number_label.toPlainText()
            import connectSql as csql
            data = self.number_label.toPlainText()+";"+self.iban_label.toPlainText()+";" + csql.gmaa + ";" + self.name_label.toPlainText()
            response = csql.newUser(data)
            if  response == "Timeout":
                d=KayitDialog(m = "Bağlantı(Server) problemi var kayıt sadece yerel yapıldı")
                d.exec()
            else:
                d = KayitDialog()
                d.exec()

            with open(os.path.split(this_path)[0] + '\\whatsapp_config.ini', 'w') as configfile:
                self.con.write(configfile)
            self.close()


    def cancel(self):
        self.close()



class KayitDialog(QDialog):
    def __init__(self,m=""):
        super().__init__()
        self.setWindowTitle("Tebrikler")
        self.setWindowIcon(QIcon("whatsApp/wpicon.ico"))
        self.layout = QVBoxLayout()
        message = QLabel("Kayıt Başarılı  "+m)

        message.setStyleSheet("padding: 20px;background-color: rgb(255, 255, 255);")
        message.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(message)
        self.setLayout(self.layout)
        time.sleep(1)
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SettingsWindow()
    sys.exit(app.exec())



