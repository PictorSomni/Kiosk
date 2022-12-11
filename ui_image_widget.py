# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'image_widgetHNoBSe.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Form(QWidget):
    def setupUi(self, parent=None):
        self.verticalLayout_2 = QVBoxLayout(self)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(7, 7, 7, 7)
        self.label_image = QLabel(self.frame)
        self.label_image.setObjectName(u"label_image")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_image.sizePolicy().hasHeightForWidth())
        self.label_image.setSizePolicy(sizePolicy)
        self.label_image.setFrameShape(QFrame.StyledPanel)
        self.label_image.setText(u"")
        self.label_image.setPixmap(QPixmap(u"C:/Users/charl/Documents/PYTHON/Image manipulation/GUI/NZ6_4204.jpg"))
        self.label_image.setScaledContents(False)
        self.label_image.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_image)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_remove = QPushButton(self.frame)
        self.button_remove.setObjectName(u"button_remove")
        self.button_remove.setMinimumSize(QSize(64, 64))
        self.button_remove.setMaximumSize(QSize(64, 64))
        font = QFont()
        font.setPointSize(21)
        self.button_remove.setFont(font)

        self.horizontalLayout.addWidget(self.button_remove)

        self.spinBox = QSpinBox(self.frame)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimumSize(QSize(0, 64))
        self.spinBox.setFont(font)
        self.spinBox.setAlignment(Qt.AlignCenter)
        self.spinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox.setMaximum(1000)

        self.horizontalLayout.addWidget(self.spinBox)

        self.button_add = QPushButton(self.frame)
        self.button_add.setObjectName(u"button_add")
        self.button_add.setMinimumSize(QSize(64, 64))
        self.button_add.setMaximumSize(QSize(64, 64))
        self.button_add.setFont(font)

        self.horizontalLayout.addWidget(self.button_add)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.frame)

