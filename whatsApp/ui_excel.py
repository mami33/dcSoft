# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'excel.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1052, 546)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableWidget = QTableWidget(Form)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"color:rgb(255, 85, 127)")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_9)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.chosen_columns_label = QLabel(Form)
        self.chosen_columns_label.setObjectName(u"chosen_columns_label")
        self.chosen_columns_label.setEnabled(True)
        self.chosen_columns_label.setStyleSheet(u"color: rgba(255, 255, 255, 0);")

        self.verticalLayout_2.addWidget(self.chosen_columns_label)

        self.botton_frame = QFrame(Form)
        self.botton_frame.setObjectName(u"botton_frame")
        self.botton_frame.setFrameShape(QFrame.StyledPanel)
        self.botton_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.botton_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.botton_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(25)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ch_name_bn = QPushButton(self.frame)
        self.ch_name_bn.setObjectName(u"ch_name_bn")
        self.ch_name_bn.setMinimumSize(QSize(160, 35))
        self.ch_name_bn.setMaximumSize(QSize(160, 35))
        self.ch_name_bn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ch_name_bn.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(85, 255, 127, 100);\n"
"border-radius:15px;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgba(85, 255, 127, 200);\n"
"border-radius:15px;\n"
"}\n"
"QPushButton::pressed{\n"
"background-color: rgba(85, 255, 127, 75);\n"
"border-radius:15px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.ch_name_bn)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(300, 35))
        self.label.setMaximumSize(QSize(300, 35))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.label.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.label)

        self.name_column_label = QLabel(self.frame)
        self.name_column_label.setObjectName(u"name_column_label")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.name_column_label.setFont(font2)
        self.name_column_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.name_column_label)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(25)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.ch_number_btn = QPushButton(self.frame)
        self.ch_number_btn.setObjectName(u"ch_number_btn")
        self.ch_number_btn.setMinimumSize(QSize(160, 35))
        self.ch_number_btn.setMaximumSize(QSize(160, 35))
        self.ch_number_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ch_number_btn.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(85, 255, 127, 100);\n"
"border-radius:15px;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgba(85, 255, 127, 200);\n"
"border-radius:15px;\n"
"}\n"
"QPushButton::pressed{\n"
"background-color: rgba(85, 255, 127, 75);\n"
"border-radius:15px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.ch_number_btn)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(300, 35))
        self.label_2.setFont(font1)
        self.label_2.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.label_2.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.number_column_label = QLabel(self.frame)
        self.number_column_label.setObjectName(u"number_column_label")
        self.number_column_label.setFont(font2)
        self.number_column_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.number_column_label)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(25)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.ch_cost_btn = QPushButton(self.frame)
        self.ch_cost_btn.setObjectName(u"ch_cost_btn")
        self.ch_cost_btn.setMinimumSize(QSize(160, 35))
        self.ch_cost_btn.setMaximumSize(QSize(160, 35))
        self.ch_cost_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ch_cost_btn.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(85, 255, 127, 100);\n"
"border-radius:15px;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgba(85, 255, 127, 200);\n"
"border-radius:15px;\n"
"}\n"
"QPushButton::pressed{\n"
"background-color: rgba(85, 255, 127, 75);\n"
"border-radius:15px;\n"
"}")

        self.horizontalLayout_4.addWidget(self.ch_cost_btn)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(300, 35))
        self.label_4.setFont(font1)
        self.label_4.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.label_4.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.total_column_label = QLabel(self.frame)
        self.total_column_label.setObjectName(u"total_column_label")
        self.total_column_label.setFont(font2)
        self.total_column_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.total_column_label)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.line_3 = QFrame(self.frame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(25)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.ch_date_btn = QPushButton(self.frame)
        self.ch_date_btn.setObjectName(u"ch_date_btn")
        self.ch_date_btn.setMinimumSize(QSize(160, 35))
        self.ch_date_btn.setMaximumSize(QSize(160, 35))
        self.ch_date_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ch_date_btn.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(85, 255, 127, 100);\n"
"border-radius:15px;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgba(85, 255, 127, 200);\n"
"border-radius:15px;\n"
"}\n"
"QPushButton::pressed{\n"
"background-color: rgba(85, 255, 127, 75);\n"
"border-radius:15px;\n"
"}")

        self.horizontalLayout_5.addWidget(self.ch_date_btn)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(300, 35))
        self.label_3.setMaximumSize(QSize(300, 35))
        self.label_3.setFont(font1)
        self.label_3.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.label_3.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.date_column_label = QLabel(self.frame)
        self.date_column_label.setObjectName(u"date_column_label")
        self.date_column_label.setFont(font2)
        self.date_column_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.date_column_label)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_6.addLayout(self.verticalLayout)


        self.horizontalLayout.addWidget(self.frame)

        self.add_to_opage_btn = QPushButton(self.botton_frame)
        self.add_to_opage_btn.setObjectName(u"add_to_opage_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_to_opage_btn.sizePolicy().hasHeightForWidth())
        self.add_to_opage_btn.setSizePolicy(sizePolicy)
        self.add_to_opage_btn.setMinimumSize(QSize(100, 100))
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        self.add_to_opage_btn.setFont(font3)
        self.add_to_opage_btn.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.889, y2:0.784591, stop:0.329975 rgba(80, 155, 30, 150), stop:0.649874 rgba(170, 255, 127, 150));\n"
"border-radius:20px;\n"
"	\n"
"	color: rgb(0, 85, 0);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"border-radius:20px;\n"
"background-color: rgba(165, 165, 165,200);\n"
"color: rgb(85, 255, 0);}\n"
"\n"
"QPushButton::pressed{\n"
"border-radius:20px;\n"
"background-color: rgba(165, 165, 165,100);\n"
"color: rgb(85, 255, 0);}\n"
"")

        self.horizontalLayout.addWidget(self.add_to_opage_btn)

        self.clear_colselection_btn = QPushButton(self.botton_frame)
        self.clear_colselection_btn.setObjectName(u"clear_colselection_btn")
        self.clear_colselection_btn.setMinimumSize(QSize(100, 100))
        self.clear_colselection_btn.setMaximumSize(QSize(100, 100))
        self.clear_colselection_btn.setFont(font1)
        self.clear_colselection_btn.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.889, y2:0.784591, stop:0.329975 rgba(80, 155, 30, 150), stop:0.649874 rgba(170, 255, 127, 150));\n"
"border-radius:20px;\n"
"	\n"
"	color: rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"border-radius:20px;\n"
"background-color: rgba(165, 165, 165,200);\n"
"color: rgb(85, 255, 0);}\n"
"\n"
"QPushButton::pressed{\n"
"border-radius:20px;\n"
"background-color: rgba(165, 165, 165,100);\n"
"color: rgb(85, 255, 0);}\n"
"")

        self.horizontalLayout.addWidget(self.clear_colselection_btn)


        self.verticalLayout_2.addWidget(self.botton_frame)


        self.retranslateUi(Form)
        Form.windowIconTextChanged.connect(Form.hide)
        self.clear_colselection_btn.clicked.connect(self.name_column_label.clear)
        self.clear_colselection_btn.clicked.connect(self.number_column_label.clear)
        self.clear_colselection_btn.clicked.connect(self.total_column_label.clear)
        self.clear_colselection_btn.clicked.connect(self.date_column_label.clear)
        self.ch_name_bn.clicked["bool"].connect(self.frame_2.setHidden)
        self.ch_number_btn.clicked["bool"].connect(self.frame_2.setHidden)
        self.ch_cost_btn.clicked["bool"].connect(self.frame_2.setHidden)
        self.ch_date_btn.clicked["bool"].connect(self.frame_2.setHidden)
        Form.customContextMenuRequested.connect(self.chosen_columns_label.hide)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"^   \u00d6NCE \u0130LG\u0130L\u0130 S\u00dcTUNU YA DA \u0130LG\u0130L\u0130 H\u00dcCREY\u0130 TABLODAN TIKLAYIN  SONRA A\u015eA\u011eIDAN \u0130LG\u0130L\u0130 BUTONU TIKLAYIN ^", None))
        self.chosen_columns_label.setText(QCoreApplication.translate("Form", u"none", None))
        self.ch_name_bn.setText(QCoreApplication.translate("Form", u"\u0130sim S\u00fctunu Belirle", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0130sim S\u00fctunu  ->", None))
        self.name_column_label.setText(QCoreApplication.translate("Form", u"-", None))
        self.ch_number_btn.setText(QCoreApplication.translate("Form", u"Numara S\u00fctunu Belirle", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Numara S\u00fctunu ->", None))
        self.number_column_label.setText(QCoreApplication.translate("Form", u"-", None))
        self.ch_cost_btn.setText(QCoreApplication.translate("Form", u"Tutar S\u00fctunu Belirle", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Tutar S\u00fctunu ->", None))
        self.total_column_label.setText(QCoreApplication.translate("Form", u"-", None))
        self.ch_date_btn.setText(QCoreApplication.translate("Form", u"Tutar Tarihi Belirle", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Opsiyonel  ->", None))
        self.date_column_label.setText(QCoreApplication.translate("Form", u"-", None))
        self.add_to_opage_btn.setText(QCoreApplication.translate("Form", u"Ekle", None))
        self.clear_colselection_btn.setText(QCoreApplication.translate("Form", u"Temizle", None))
    # retranslateUi

