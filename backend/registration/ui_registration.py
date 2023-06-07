# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mailxIDYKp.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import asset_rc

class Ui_Registration(object):
    def setupUi(self, Registration):
        if Registration.objectName():
            Registration.setObjectName(u"Registration")
        Registration.resize(600, 720)
        Registration.setMinimumSize(QSize(600, 700))
        Registration.setMaximumSize(QSize(600, 720))
        self.verticalLayout = QVBoxLayout(Registration)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Registration)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius:5px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 40))
        self.frame_3.setMaximumSize(QSize(16777215, 30))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(60, 0))
        self.label.setMaximumSize(QSize(60, 16777215))
        self.label.setPixmap(QPixmap(u":/icons/asset/user-plus.svg"))

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.btn_minimize = QPushButton(self.frame_3)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(16, 16))
        self.btn_minimize.setMaximumSize(QSize(17, 17))
        self.btn_minimize.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 255, 127);\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: rgba(85, 255, 127,150);\n"
"	\n"
"}")

        self.horizontalLayout.addWidget(self.btn_minimize)

        self.btn_maximize = QPushButton(self.frame_3)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setMinimumSize(QSize(16, 16))
        self.btn_maximize.setMaximumSize(QSize(17, 17))
        self.btn_maximize.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(255, 170, 0);\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: rgba(255, 170, 0,150);\n"
"	\n"
"}")

        self.horizontalLayout.addWidget(self.btn_maximize)

        self.btn_close = QPushButton(self.frame_3)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(16, 16))
        self.btn_close.setMaximumSize(QSize(17, 17))
        self.btn_close.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 0, 0);\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: rgba(255, 0, 0,150);\n"
"	\n"
"}")

        self.horizontalLayout.addWidget(self.btn_close)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.reg_firstname = QLineEdit(self.frame_4)
        self.reg_firstname.setObjectName(u"reg_firstname")
        self.reg_firstname.setGeometry(QRect(300, 20, 260, 51))
        self.reg_firstname.setMinimumSize(QSize(260, 0))
        self.reg_firstname.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(10)
        self.reg_firstname.setFont(font1)
        self.reg_firstname.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:10px;\n"
"	padding-left: 7px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.reg_firstname.setClearButtonEnabled(True)
        self.image = QLabel(self.frame_4)
        self.image.setObjectName(u"image")
        self.image.setGeometry(QRect(20, 20, 251, 261))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setWeight(50)
        self.image.setFont(font2)
        self.image.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.image.setPixmap(QPixmap(u":/icons/asset/image.svg"))
        self.image.setAlignment(Qt.AlignCenter)
        self.reg_othername = QLineEdit(self.frame_4)
        self.reg_othername.setObjectName(u"reg_othername")
        self.reg_othername.setGeometry(QRect(300, 90, 260, 51))
        self.reg_othername.setMinimumSize(QSize(260, 0))
        self.reg_othername.setMaximumSize(QSize(16777215, 16777215))
        self.reg_othername.setFont(font1)
        self.reg_othername.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:10px;\n"
"	padding-left: 7px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.reg_othername.setClearButtonEnabled(True)
        self.reg_lastname = QLineEdit(self.frame_4)
        self.reg_lastname.setObjectName(u"reg_lastname")
        self.reg_lastname.setGeometry(QRect(300, 160, 260, 51))
        self.reg_lastname.setMinimumSize(QSize(260, 0))
        self.reg_lastname.setMaximumSize(QSize(16777215, 16777215))
        self.reg_lastname.setFont(font1)
        self.reg_lastname.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:10px;\n"
"	padding-left: 7px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.reg_lastname.setClearButtonEnabled(True)
        self.reg_reference = QLineEdit(self.frame_4)
        self.reg_reference.setObjectName(u"reg_reference")
        self.reg_reference.setGeometry(QRect(300, 230, 260, 51))
        self.reg_reference.setMinimumSize(QSize(260, 0))
        self.reg_reference.setMaximumSize(QSize(16777215, 16777215))
        self.reg_reference.setFont(font1)
        self.reg_reference.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:10px;\n"
"	padding-left: 7px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.reg_reference.setClearButtonEnabled(True)
        self.reg_index = QLineEdit(self.frame_4)
        self.reg_index.setObjectName(u"reg_index")
        self.reg_index.setGeometry(QRect(380, 300, 180, 51))
        self.reg_index.setMinimumSize(QSize(180, 0))
        self.reg_index.setMaximumSize(QSize(16777215, 16777215))
        self.reg_index.setFont(font1)
        self.reg_index.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:10px;\n"
"	padding-left: 7px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.reg_index.setClearButtonEnabled(True)
        self.reg_program = QLineEdit(self.frame_4)
        self.reg_program.setObjectName(u"reg_program")
        self.reg_program.setGeometry(QRect(20, 300, 341, 51))
        self.reg_program.setMinimumSize(QSize(260, 0))
        self.reg_program.setMaximumSize(QSize(16777215, 16777215))
        self.reg_program.setFont(font1)
        self.reg_program.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:10px;\n"
"	padding-left: 7px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.reg_program.setClearButtonEnabled(True)
        self.reg_filename = QLineEdit(self.frame_4)
        self.reg_filename.setObjectName(u"reg_filename")
        self.reg_filename.setGeometry(QRect(20, 370, 341, 51))
        self.reg_filename.setMinimumSize(QSize(260, 0))
        self.reg_filename.setMaximumSize(QSize(16777215, 16777215))
        self.reg_filename.setFont(font1)
        self.reg_filename.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:10px;\n"
"	padding-left: 7px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.reg_filename.setClearButtonEnabled(True)
        self.btn_reg_browse = QPushButton(self.frame_4)
        self.btn_reg_browse.setObjectName(u"btn_reg_browse")
        self.btn_reg_browse.setGeometry(QRect(380, 370, 181, 51))
        self.btn_reg_browse.setFont(font1)
        self.btn_reg_browse.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_reg_browse.setIconSize(QSize(30, 30))
        self.btn_reg_browse.setFlat(True)
        self.btn_reg_register = QPushButton(self.frame_4)
        self.btn_reg_register.setObjectName(u"btn_reg_register")
        self.btn_reg_register.setGeometry(QRect(210, 440, 161, 51))
        self.btn_reg_register.setFont(font1)
        self.btn_reg_register.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/asset/user-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_reg_register.setIcon(icon)
        self.btn_reg_register.setIconSize(QSize(30, 30))
        self.btn_reg_register.setFlat(True)
        self.btn_reg_delete = QPushButton(self.frame_4)
        self.btn_reg_delete.setObjectName(u"btn_reg_delete")
        self.btn_reg_delete.setGeometry(QRect(400, 440, 161, 51))
        self.btn_reg_delete.setFont(font1)
        self.btn_reg_delete.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/asset/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_reg_delete.setIcon(icon1)
        self.btn_reg_delete.setIconSize(QSize(30, 30))
        self.btn_reg_delete.setFlat(True)
        self.label_notification = QLabel(self.frame_4)
        self.label_notification.setObjectName(u"label_notification")
        self.label_notification.setGeometry(QRect(20, 520, 541, 111))
        font3 = QFont()
        font3.setFamily(u"MS Shell Dlg 2")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setWeight(50)
        self.label_notification.setFont(font3)
        self.label_notification.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.label_notification.setAlignment(Qt.AlignCenter)
        self.label_notification.setWordWrap(True)
        self.btn_reg_search = QPushButton(self.frame_4)
        self.btn_reg_search.setObjectName(u"btn_reg_search")
        self.btn_reg_search.setGeometry(QRect(20, 440, 161, 51))
        self.btn_reg_search.setFont(font1)
        self.btn_reg_search.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/asset/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_reg_search.setIcon(icon2)
        self.btn_reg_search.setIconSize(QSize(30, 30))
        self.btn_reg_search.setFlat(True)

        self.verticalLayout_2.addWidget(self.frame_4)


        self.verticalLayout_4.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Registration)

        QMetaObject.connectSlotsByName(Registration)
    # setupUi

    def retranslateUi(self, Registration):
        Registration.setWindowTitle(QCoreApplication.translate("Registration", u"Dialog", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Registration", u"Registration", None))
        self.btn_minimize.setText("")
        self.btn_maximize.setText("")
        self.btn_close.setText("")
        self.reg_firstname.setPlaceholderText(QCoreApplication.translate("Registration", u"Firstname", None))
        self.image.setText("")
        self.reg_othername.setPlaceholderText(QCoreApplication.translate("Registration", u"Othername", None))
        self.reg_lastname.setPlaceholderText(QCoreApplication.translate("Registration", u"Lastname", None))
        self.reg_reference.setPlaceholderText(QCoreApplication.translate("Registration", u"Reference", None))
        self.reg_index.setPlaceholderText(QCoreApplication.translate("Registration", u"Index", None))
        self.reg_program.setPlaceholderText(QCoreApplication.translate("Registration", u"Program", None))
        self.reg_filename.setPlaceholderText(QCoreApplication.translate("Registration", u"Filename", None))
        self.btn_reg_browse.setText(QCoreApplication.translate("Registration", u"Browse Images", None))
        self.btn_reg_register.setText(QCoreApplication.translate("Registration", u"Register", None))
        self.btn_reg_delete.setText(QCoreApplication.translate("Registration", u"Delete", None))
        self.label_notification.setText(QCoreApplication.translate("Registration", u"Notification", None))
        self.btn_reg_search.setText(QCoreApplication.translate("Registration", u"Search", None))
    # retranslateUi

