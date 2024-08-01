# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'welcomeDiag.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(564, 419)
        Dialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"")
        self.label.setTextFormat(Qt.RichText)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label.setMargin(0)

        self.verticalLayout.addWidget(self.label)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 170, 0, 100);\n"
"border-radius:15px;\n"
"padding:10px;\n"
"padding-left:20px;\n"
"padding-right:20px;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgba(0, 170, 0, 20);\n"
"border-radius:15px;\n"
"padding:10px;\n"
"padding-left:20px;\n"
"padding-right:20px;\n"
"}")

        self.verticalLayout.addWidget(self.pushButton, 0, Qt.AlignHCenter)


        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.accept)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700; color:#15aa0b;\">Ho\u015fgeldiniz</span><span style=\" font-size:16pt; font-weight:700; color:#15aa0b;\"> !</span></p><p><span style=\" font-size:11pt; font-weight:700; color:#15aa0b;\">Kullanmaya ba\u015flamadan \u00f6nce:</span></p><p><span style=\" font-size:11pt; color:#15aa0b;\">- \u0130nternet ba\u011flant\u0131n\u0131z\u0131 kontrol edin</span></p><p><span style=\" font-size:11pt; color:#15aa0b;\">- Mesaj listesinin oldu\u011fu Excel dosyas\u0131n\u0131 haz\u0131rlay\u0131n</span></p><p><span style=\" font-size:11pt; color:#15aa0b;\">- WhatsApp web kayna\u011f\u0131nda de\u011fi\u015fiklik varsa sistem \u00e7al\u0131\u015fmayacakt\u0131r. </span></p><p><span style=\" font-size:11pt; color:#15aa0b;\">- Kaynaklar\u0131m\u0131z s\u00fcrekli g\u00fcncellenecektir.</span></p><p><span style=\" font-size:11pt; color:#15aa0b;\">** G\u00f6nderimden \u00f6nce b\u00fct\u00fcn Chorome pencerelerini kapat\u0131n </span></p></body>"
                        "</html>", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Kapat", None))
    # retranslateUi

