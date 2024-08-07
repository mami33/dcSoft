# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)
import rc_res

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(320, 549)
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 0, 10, 0)
        self.top_frame = QFrame(Form)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setMinimumSize(QSize(0, 110))
        self.top_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.top_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(100, 100))
        self.label_4.setMaximumSize(QSize(100, 100))
        self.label_4.setPixmap(QPixmap(u":/what/wpicon.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setWordWrap(False)

        self.horizontalLayout_2.addWidget(self.label_4, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_6 = QLabel(self.top_frame)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.label_5 = QLabel(self.top_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setPixmap(QPixmap(u":/icons/picon/user.svg"))
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_5)


        self.verticalLayout.addWidget(self.top_frame)

        self.isim = QLabel(Form)
        self.isim.setObjectName(u"isim")
        self.isim.setMinimumSize(QSize(250, 40))
        self.isim.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.isim.setFont(font)

        self.verticalLayout.addWidget(self.isim)

        self.name_label = QTextEdit(Form)
        self.name_label.setObjectName(u"name_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_label.sizePolicy().hasHeightForWidth())
        self.name_label.setSizePolicy(sizePolicy)
        self.name_label.setMinimumSize(QSize(0, 30))
        self.name_label.setMaximumSize(QSize(1500, 30))
        font1 = QFont()
        font1.setBold(True)
        self.name_label.setFont(font1)
#if QT_CONFIG(whatsthis)
        self.name_label.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.name_label.setStyleSheet(u"color: rgb(76, 175, 80);")
        self.name_label.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.name_label.setFrameShape(QFrame.Shape.StyledPanel)
        self.name_label.setLineWidth(1)
        self.name_label.setAcceptRichText(False)
        self.name_label.setPlaceholderText(u"")

        self.verticalLayout.addWidget(self.name_label)

        self.iban = QLabel(Form)
        self.iban.setObjectName(u"iban")
        self.iban.setMinimumSize(QSize(0, 50))
        self.iban.setMaximumSize(QSize(16777215, 40))
        self.iban.setFont(font)

        self.verticalLayout.addWidget(self.iban)

        self.iban_label = QTextEdit(Form)
        self.iban_label.setObjectName(u"iban_label")
        self.iban_label.setMinimumSize(QSize(0, 30))
        self.iban_label.setMaximumSize(QSize(1500, 30))
        self.iban_label.setFont(font1)
        self.iban_label.setStyleSheet(u"color: rgb(76, 175, 80);")

        self.verticalLayout.addWidget(self.iban_label)

        self.numara = QLabel(Form)
        self.numara.setObjectName(u"numara")
        self.numara.setMinimumSize(QSize(250, 40))
        self.numara.setMaximumSize(QSize(16777215, 40))
        self.numara.setFont(font)

        self.verticalLayout.addWidget(self.numara)

        self.number_label = QTextEdit(Form)
        self.number_label.setObjectName(u"number_label")
        self.number_label.setMinimumSize(QSize(0, 30))
        self.number_label.setMaximumSize(QSize(1500, 30))
        self.number_label.setFont(font1)
        self.number_label.setStyleSheet(u"color: rgb(76, 175, 80);")

        self.verticalLayout.addWidget(self.number_label)

        self.button_frame = QFrame(Form)
        self.button_frame.setObjectName(u"button_frame")
        self.button_frame.setMinimumSize(QSize(300, 0))
        self.button_frame.setMaximumSize(QSize(350, 100))
        self.button_frame.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding:5px")
        self.button_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.button_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.button_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cancel_btn = QPushButton(self.button_frame)
        self.cancel_btn.setObjectName(u"cancel_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cancel_btn.sizePolicy().hasHeightForWidth())
        self.cancel_btn.setSizePolicy(sizePolicy1)
        self.cancel_btn.setMinimumSize(QSize(80, 40))
        self.cancel_btn.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"background-color: rgba(189, 189, 189, 50);\n"
"}\n"
"QPushButton:hover{\n"
"border-radius:10px;\n"
"background-color:rgba(189, 189, 189, 170);\n"
"}\n"
"QPushButton:pressed{\n"
"border-radius:10px;\n"
"background-color:rgba(189, 189, 189, 150);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.cancel_btn, 0, Qt.AlignmentFlag.AlignHCenter)

        self.save_btn = QPushButton(self.button_frame)
        self.save_btn.setObjectName(u"save_btn")
        sizePolicy1.setHeightForWidth(self.save_btn.sizePolicy().hasHeightForWidth())
        self.save_btn.setSizePolicy(sizePolicy1)
        self.save_btn.setMinimumSize(QSize(80, 40))
        self.save_btn.setMaximumSize(QSize(80, 40))
        self.save_btn.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"background-color:rgba(76, 175, 80, 70);\n"
"}\n"
"QPushButton:hover{\n"
"border-radius:10px;\n"
"background-color:rgba(76, 175, 80, 170);\n"
"}\n"
"QPushButton:pressed{\n"
"border-radius:10px;\n"
"background-color:rgba(76, 175, 80, 50);\n"
"}")

        self.horizontalLayout.addWidget(self.save_btn, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout.addWidget(self.button_frame, 0, Qt.AlignmentFlag.AlignLeft)

        self.reset_btn = QPushButton(Form)
        self.reset_btn.setObjectName(u"reset_btn")
        self.reset_btn.setMaximumSize(QSize(50, 20))

        self.verticalLayout.addWidget(self.reset_btn, 0, Qt.AlignmentFlag.AlignRight)

        QWidget.setTabOrder(self.name_label, self.iban_label)
        QWidget.setTabOrder(self.iban_label, self.number_label)
        QWidget.setTabOrder(self.number_label, self.save_btn)
        QWidget.setTabOrder(self.save_btn, self.cancel_btn)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_4.setText("")
        self.label_6.setText("")
        self.label_5.setText("")
        self.isim.setText(QCoreApplication.translate("Form", u"Firma \u0130smi Giriniz", None))
        self.name_label.setDocumentTitle("")
        self.name_label.setMarkdown("")
        self.iban.setText(QCoreApplication.translate("Form", u"Firma IBAN Giriniz", None))
        self.numara.setText(QCoreApplication.translate("Form", u"Firma \u0130rtibat Numaras\u0131 Giriniz", None))
        self.cancel_btn.setText(QCoreApplication.translate("Form", u"Vazge\u00e7", None))
        self.save_btn.setText(QCoreApplication.translate("Form", u"Kaydet", None))
        self.reset_btn.setText(QCoreApplication.translate("Form", u"S\u0131f\u0131rla", None))
    # retranslateUi

