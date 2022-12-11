# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_uikpvvXk.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        self.main_vertical_layout = QWidget(MainWindow)
        self.main_vertical_layout.setObjectName(u"main_vertical_layout")
        self.gridLayout_4 = QGridLayout(self.main_vertical_layout)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_top = QFrame(self.main_vertical_layout)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMaximumSize(QSize(16777215, 200))
        self.frame_top.setStyleSheet(u"")
        self.frame_top.setFrameShape(QFrame.Panel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_far_left = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_far_left)

        self.label_logo = QLabel(self.frame_top)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setMinimumSize(QSize(192, 64))
        self.label_logo.setFrameShape(QFrame.NoFrame)
        self.label_logo.setFrameShadow(QFrame.Plain)
        self.label_logo.setText(u"")
        self.label_logo.setPixmap(QPixmap(u"LOGO.png"))
        self.label_logo.setScaledContents(False)

        self.horizontalLayout_2.addWidget(self.label_logo)

        self.horizontalSpacer_logo_right = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(self.horizontalSpacer_logo_right)

        self.label_price = QLabel(self.frame_top)
        self.label_price.setObjectName(u"label_price")
        self.label_price.setMinimumSize(QSize(64, 64))
        self.label_price.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_price)

        self.label_euro = QLabel(self.frame_top)
        self.label_euro.setObjectName(u"label_price")
        self.label_euro.setMinimumSize(QSize(48, 64))
        self.label_euro.setAlignment(Qt.AlignCenter)
        self.label_euro.setText("€")

        self.horizontalLayout_2.addWidget(self.label_euro)

        self.horizontalSpacer_price_right = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(self.horizontalSpacer_price_right)

        self.button_top_minus = QPushButton(self.frame_top)
        self.button_top_minus.setObjectName(u"button_top_minus")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_top_minus.sizePolicy().hasHeightForWidth())
        self.button_top_minus.setSizePolicy(sizePolicy)
        self.button_top_minus.setMinimumSize(QSize(64, 64))
        self.button_top_minus.setMaximumSize(QSize(64, 64))
        self.button_top_minus.setStyleSheet(u"background-color: rgb(50, 50, 50);")

        self.horizontalLayout_2.addWidget(self.button_top_minus)

        self.label_top = QLabel(self.frame_top)
        self.label_top.setObjectName(u"label_top")
        self.label_top.setMinimumSize(QSize(350, 64))
        self.label_top.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_top)

        self.button_top_plus = QPushButton(self.frame_top)
        self.button_top_plus.setObjectName(u"button_top_plus")
        sizePolicy.setHeightForWidth(self.button_top_plus.sizePolicy().hasHeightForWidth())
        self.button_top_plus.setSizePolicy(sizePolicy)
        self.button_top_plus.setMinimumSize(QSize(64, 64))
        self.button_top_plus.setMaximumSize(QSize(64, 64))
        self.button_top_plus.setStyleSheet(u"background-color: rgb(50, 50, 50);")

        self.horizontalLayout_2.addWidget(self.button_top_plus)

        self.horizontalSpacer_far_right = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_far_right)


        self.gridLayout_4.addWidget(self.frame_top, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_buttons = QFrame(self.main_vertical_layout)
        self.frame_buttons.setObjectName(u"frame_buttons")
        self.frame_buttons.setMaximumSize(QSize(200, 16777215))
        self.frame_buttons.setStyleSheet(u"")
        self.frame_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_buttons.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_buttons)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.buttons_layout = QVBoxLayout()
        self.buttons_layout.setObjectName(u"buttons_layout")
        self.buttons_layout.setContentsMargins(6, 6, 6, 6)
        self.button_open = QPushButton(self.frame_buttons)
        self.button_open.setObjectName(u"button_open")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.button_open.sizePolicy().hasHeightForWidth())
        self.button_open.setSizePolicy(sizePolicy1)
        self.button_open.setMinimumSize(QSize(0, 128))

        self.buttons_layout.addWidget(self.button_open)

        self.frame_print_size = QFrame(self.frame_buttons)
        self.frame_print_size.setObjectName(u"frame_print_size")
        self.frame_print_size.setFrameShape(QFrame.StyledPanel)
        self.frame_print_size.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_print_size)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setContentsMargins(6, 6, 6, 6)
        self.print_size_layout = QVBoxLayout()
        self.print_size_layout.setObjectName(u"print_size_layout")
        self.print_size_layout.setContentsMargins(6, 0, 6, 0)

        self.gridLayout.addLayout(self.print_size_layout, 0, 0, 1, 1)


        self.buttons_layout.addWidget(self.frame_print_size)

        self.button_validate = QPushButton(self.frame_buttons)
        self.button_validate.setObjectName(u"button_validate")
        sizePolicy1.setHeightForWidth(self.button_validate.sizePolicy().hasHeightForWidth())
        self.button_validate.setSizePolicy(sizePolicy1)
        self.button_validate.setMinimumSize(QSize(0, 128))

        self.buttons_layout.addWidget(self.button_validate)


        self.verticalLayout_3.addLayout(self.buttons_layout)


        self.horizontalLayout.addWidget(self.frame_buttons)

        self.frame_images = QFrame(self.main_vertical_layout)
        self.frame_images.setObjectName(u"frame_images")
        self.frame_images.setFrameShape(QFrame.StyledPanel)
        self.frame_images.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_images)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.scrollArea = QScrollArea(self.frame_images)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignCenter)
        self.scrollArea_widget = QWidget()
        self.scrollArea_widget.setObjectName(u"scrollArea_widget")
        self.scrollArea_widget.setGeometry(QRect(0, 0, 1672, 948))
        self.scrollArea_images = QGridLayout(self.scrollArea_widget)
        self.scrollArea_images.setObjectName(u"scrollArea_images")
        self.scrollArea.setWidget(self.scrollArea_widget)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame_images)


        self.gridLayout_4.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.main_vertical_layout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.button_top_minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_top.setText(QCoreApplication.translate("MainWindow", u"Impressions de toutes les images", None))
        self.button_top_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.button_open.setText(QCoreApplication.translate("MainWindow", u"OUVRIR", None))
        self.button_validate.setText(QCoreApplication.translate("MainWindow", u"VALIDER", None))
    # retranslateUi