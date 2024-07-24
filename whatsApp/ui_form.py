# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import rc_res

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(750, 550)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(750, 550))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(750, 110))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(90, 90))
        self.label.setMaximumSize(QSize(90, 90))
        self.label.setStyleSheet(u"padding:1px")
        self.label.setPixmap(QPixmap(u":/what/wpicon.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label, 0, Qt.AlignTop)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"Segoe MDL2 Assets"])
        font.setPointSize(19)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setStyleSheet(u"color: rgb(76, 175, 80);\n"
"padding:1px")
        self.label_2.setLineWidth(-2)
        self.label_2.setTextFormat(Qt.MarkdownText)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_2, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.settings_frame = QFrame(self.frame_2)
        self.settings_frame.setObjectName(u"settings_frame")
        sizePolicy1.setHeightForWidth(self.settings_frame.sizePolicy().hasHeightForWidth())
        self.settings_frame.setSizePolicy(sizePolicy1)
        self.settings_frame.setFrameShape(QFrame.StyledPanel)
        self.settings_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.settings_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.excel_frame = QFrame(self.settings_frame)
        self.excel_frame.setObjectName(u"excel_frame")
        self.excel_frame.setFrameShape(QFrame.StyledPanel)
        self.excel_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.excel_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.excel_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"margin:10px")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setMargin(-5)

        self.verticalLayout_4.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.add_excel_button = QPushButton(self.excel_frame)
        self.add_excel_button.setObjectName(u"add_excel_button")
        sizePolicy.setHeightForWidth(self.add_excel_button.sizePolicy().hasHeightForWidth())
        self.add_excel_button.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.add_excel_button.setFont(font1)
        self.add_excel_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.add_excel_button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border:3px solid;\n"
"border-radius:10px;\n"
"	border-color:rgb(76, 175, 80);\n"
"	color: rgb(21, 48, 22);\n"
"margin:2px;\n"
"padding:2px\n"
"\n"
"	\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgba(255, 255, 255, 50);\n"
"	border-radius:10px;\n"
"	border:5px solid\n"
"	\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/picon/paperclip.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_excel_button.setIcon(icon)
        self.add_excel_button.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.add_excel_button)

        self.add_excel_button_3 = QPushButton(self.excel_frame)
        self.add_excel_button_3.setObjectName(u"add_excel_button_3")
        sizePolicy.setHeightForWidth(self.add_excel_button_3.sizePolicy().hasHeightForWidth())
        self.add_excel_button_3.setSizePolicy(sizePolicy)
        self.add_excel_button_3.setFont(font1)
        self.add_excel_button_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.add_excel_button_3.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border:3px solid;\n"
"border-radius:10px;\n"
"	border-color:rgb(76, 175, 80);\n"
"color: rgb(21, 48, 22);\n"
"	margin:2px;\n"
"padding:2px\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgba(255, 255, 255, 50);\n"
"	border-radius:10px;\n"
"	border:5px solid\n"
"	\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/picon/chevrons-left.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_excel_button_3.setIcon(icon1)
        self.add_excel_button_3.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.add_excel_button_3)


        self.horizontalLayout_2.addWidget(self.excel_frame, 0, Qt.AlignLeft)

        self.label_4 = QLabel(self.settings_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background-color: rgba(84, 193, 88, 50);\n"
"border-radius:25px;\n"
"padding:15px\n"
"")

        self.horizontalLayout_2.addWidget(self.label_4, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.groupBox = QGroupBox(self.settings_frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(True)

        self.verticalLayout_3.addWidget(self.checkBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setChecked(True)

        self.verticalLayout_3.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.groupBox)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout_3.addWidget(self.radioButton_3)

        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEnabled(False)

        self.verticalLayout_3.addWidget(self.comboBox)


        self.horizontalLayout_2.addWidget(self.groupBox, 0, Qt.AlignRight)


        self.gridLayout.addWidget(self.settings_frame, 0, 0, 1, 2)

        self.tableWidget = QTableWidget(self.frame_2)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        icon2 = QIcon()
        icon2.addFile(u":/icons/picon/user.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setIcon(icon2);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        icon3 = QIcon()
        icon3.addFile(u":/icons/picon/phone-call.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setIcon(icon3);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        icon4 = QIcon()
        icon4.addFile(u":/icons/picon/credit-card.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem2.setIcon(icon4);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 50):
            self.tableWidget.setRowCount(50)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(False)
        self.tableWidget.setStyleSheet(u"background-color: rgba(232, 255, 233, 50);")
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setGridStyle(Qt.DashLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setRowCount(50)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setVisible(True)

        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)

        self.sendFrame = QFrame(self.frame_2)
        self.sendFrame.setObjectName(u"sendFrame")
        sizePolicy.setHeightForWidth(self.sendFrame.sizePolicy().hasHeightForWidth())
        self.sendFrame.setSizePolicy(sizePolicy)
        self.sendFrame.setFrameShape(QFrame.StyledPanel)
        self.sendFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.sendFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.selectAllButton = QPushButton(self.sendFrame)
        self.selectAllButton.setObjectName(u"selectAllButton")
        sizePolicy.setHeightForWidth(self.selectAllButton.sizePolicy().hasHeightForWidth())
        self.selectAllButton.setSizePolicy(sizePolicy)
        self.selectAllButton.setMinimumSize(QSize(165, 30))
        self.selectAllButton.setMaximumSize(QSize(165, 30))
        self.selectAllButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.selectAllButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border:3px solid;\n"
"border-radius:10px;\n"
"	border-color:rgb(76, 175, 80);\n"
"color: rgb(21, 48, 22);\n"
"margin:2px;\n"
"padding:2px\n"
"	\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgba(255, 255, 255, 50);\n"
"	border-radius:10px;\n"
"	border:3px solid\n"
"	\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/picon/align-justify.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.selectAllButton.setIcon(icon5)
        self.selectAllButton.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.selectAllButton)

        self.sendButton = QPushButton(self.sendFrame)
        self.sendButton.setObjectName(u"sendButton")
        sizePolicy.setHeightForWidth(self.sendButton.sizePolicy().hasHeightForWidth())
        self.sendButton.setSizePolicy(sizePolicy)
        self.sendButton.setMinimumSize(QSize(165, 100))
        self.sendButton.setMaximumSize(QSize(165, 100))
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(True)
        self.sendButton.setFont(font2)
        self.sendButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.sendButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border:3px solid;\n"
"border-radius:10px;\n"
"	border-color:rgb(76, 175, 80);\n"
"color: rgb(21, 48, 22);\n"
"margin:2px;\n"
"padding:2px\n"
"	\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgba(255, 255, 255, 50);\n"
"	border-radius:10px;\n"
"	border-color:rgb(76, 175, 80);\n"
"	border:5px solid\n"
"	\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/picon/send.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.sendButton.setIcon(icon6)
        self.sendButton.setIconSize(QSize(40, 40))

        self.verticalLayout_2.addWidget(self.sendButton)


        self.gridLayout.addWidget(self.sendFrame, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.add_excel_button.clicked["bool"].connect(self.tableWidget.setDisabled)
        self.add_excel_button_3.clicked["bool"].connect(self.tableWidget.setEnabled)
        self.radioButton_3.toggled.connect(self.comboBox.setEnabled)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"WhatsApp Mesaj Otomasyonu", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Mesaj \u0130\u00e7erik Bilgisi i\u00e7in </p><p><span style=\" font-weight:700;\">Excel</span> dosyas\u0131 y\u00fckleyin</p><p><br/></p></body></html>", None))
        self.add_excel_button.setText(QCoreApplication.translate("MainWindow", u"Dosya Ekle", None))
        self.add_excel_button_3.setText(QCoreApplication.translate("MainWindow", u"Temizle     ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">\u0130\u00e7eri\u011fi Elle D\u00fczenle </span></p><p>se\u00e7ilmedi\u011finde</p><p><span style=\" font-weight:700;\">A</span> S\u00fctunu -&gt; Y\u00f6netici \u0130sim-Soyisim</p><p><span style=\" font-weight:700;\">B</span> S\u00fctunu -&gt; Cep Numaras\u0131</p><p><span style=\" font-weight:700;\">C</span> S\u00fctunu -&gt; Direkt mesaj i\u00e7eri\u011fi</p></body></html>", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Mesaj \u0130\u00e7eri\u011fi D\u00fczenle", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u0130\u00e7eri\u011fi Elle Gir", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Bakiye Hat\u0131rlatma", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Bayram/Tebrik/\u00d6zel G\u00fcn", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Kurban Bayram\u0131", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Ramazan Bayram\u0131", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Mira\u00e7 Kandili", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Regaip Kandili", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Kadir Gecesi", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"23 Nisan Ulusal Egemenlik Bayram\u0131", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"19 May\u0131s Gen\u00e7lik Ve Spor Bayram\u0131", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"29 Ekim Cumhuriyet Bayram\u0131", None))
        self.comboBox.setItemText(8, "")

        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Y\u00f6netici \u0130sim", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Numara", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Bakiye/Mesaj \u0130\u00e7eri\u011fi", None));
        self.selectAllButton.setText(QCoreApplication.translate("MainWindow", u"Hepsini Se\u00e7", None))
        self.sendButton.setText(QCoreApplication.translate("MainWindow", u"G\u00f6nder", None))
    # retranslateUi

