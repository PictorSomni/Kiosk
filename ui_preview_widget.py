# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preview_widgetacmcfM.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Preview(QDialog):
    def setupUi(self, parent=None):
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(13, 13, 13, 13)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.button_close = QPushButton(self)
        self.button_close.setObjectName(u"button_close")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_close.sizePolicy().hasHeightForWidth())
        self.button_close.setSizePolicy(sizePolicy)
        self.button_close.setMinimumSize(QSize(64, 64))
        self.button_close.setBaseSize(QSize(64, 64))        
        font = QFont()
        font.setPointSize(18)
        self.button_close.setFont(font)
        self.button_close.setText("X")

        self.horizontalLayout.addWidget(self.button_close)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.big_image = QLabel(self)
        self.big_image.setObjectName(u"big_image")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.big_image.sizePolicy().hasHeightForWidth())
        self.big_image.setSizePolicy(sizePolicy1)
        self.big_image.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.big_image)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        # self.button_previous = QPushButton(self)
        # self.button_previous.setObjectName(u"button_previous")
        # self.button_previous.setText("Image precedente")

        # self.horizontalLayout_2.addWidget(self.button_previous)

        # self.button_next = QPushButton(self)
        # self.button_next.setObjectName(u"button_next")
        # self.button_next.setText("Image suivante")

        # self.horizontalLayout_2.addWidget(self.button_next)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

    # setupUi


