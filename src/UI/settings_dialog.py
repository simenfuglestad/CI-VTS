# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.0.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from pyqtgraph import ImageView


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(898, 685)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalSlider_4 = QSlider(self.groupBox_2)
        self.horizontalSlider_4.setObjectName(u"horizontalSlider_4")
        self.horizontalSlider_4.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.horizontalSlider_4, 0, 2, 1, 1)

        self.lineEdit = QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)

        self.gridLayout_4.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label_14 = QLabel(self.groupBox_2)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_4.addWidget(self.label_14, 0, 0, 1, 1)

        self.label_15 = QLabel(self.groupBox_2)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_4.addWidget(self.label_15, 1, 0, 1, 1)

        self.checkBox = QCheckBox(self.groupBox_2)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_4.addWidget(self.checkBox, 1, 1, 1, 1)

        self.label_16 = QLabel(self.groupBox_2)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_4.addWidget(self.label_16, 1, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_4)

        self.graphicsView = ImageView(self.groupBox_2)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout_5.addWidget(self.graphicsView)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_2)


        self.verticalLayout_3.addWidget(self.groupBox_2)


        self.gridLayout.addLayout(self.verticalLayout_3, 1, 2, 1, 1)

        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 1, 1, 1, 1)

        self.label_11 = QLabel(Dialog)
        self.label_11.setObjectName(u"label_11")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy3)
        font = QFont()
        font.setPointSize(18)
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 2, 2, 1, 1)

        self.label_13 = QLabel(Dialog)
        self.label_13.setObjectName(u"label_13")
        sizePolicy3.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy3)
        self.label_13.setFont(font)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_13, 0, 2, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")
        sizePolicy3.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy3)
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_12, 1, 2, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        font1 = QFont()
        font1.setPointSize(12)
        self.label.setFont(font1)

        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_3)

        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_4.addWidget(self.comboBox)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.label_7, 5, 0, 1, 1)

        self.spinBox_4 = QSpinBox(self.groupBox)
        self.spinBox_4.setObjectName(u"spinBox_4")

        self.gridLayout_2.addWidget(self.spinBox_4, 3, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.spinBox = QSpinBox(self.groupBox)
        self.spinBox.setObjectName(u"spinBox")

        self.gridLayout_2.addWidget(self.spinBox, 0, 1, 1, 1)

        self.spinBox_3 = QSpinBox(self.groupBox)
        self.spinBox_3.setObjectName(u"spinBox_3")

        self.gridLayout_2.addWidget(self.spinBox_3, 2, 1, 1, 1)

        self.horizontalSlider_3 = QSlider(self.groupBox)
        self.horizontalSlider_3.setObjectName(u"horizontalSlider_3")
        self.horizontalSlider_3.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider_3, 1, 2, 1, 1)

        self.horizontalSlider = QSlider(self.groupBox)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 3, 2, 1, 1)

        self.spinBox_2 = QSpinBox(self.groupBox)
        self.spinBox_2.setObjectName(u"spinBox_2")

        self.gridLayout_2.addWidget(self.spinBox_2, 1, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        sizePolicy3.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)

        self.horizontalSlider_2 = QSlider(self.groupBox)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider_2, 2, 2, 1, 1)

        self.comboBox_2 = QComboBox(self.groupBox)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_2.addWidget(self.comboBox_2, 5, 2, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy4)
        self.label_9.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_9)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        sizePolicy4.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy4)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_8)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.comboBox_3 = QComboBox(self.groupBox)
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.verticalLayout_4.addWidget(self.comboBox_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_3 = QPushButton(self.groupBox)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_4.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.groupBox)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_4.addWidget(self.pushButton_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        sizePolicy3.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy3)

        self.verticalLayout_4.addWidget(self.label_10)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        self.pushButton_5 = QPushButton(Dialog)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy5)

        self.gridLayout.addWidget(self.pushButton_5, 2, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox_2.setTitle("")
        self.label_14.setText(QCoreApplication.translate("Dialog", u"LED Intesity", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"Infrared", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"Disabled", None))
        self.label_16.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"NOTE: Any adjustmens made in this window will not be carried over in an experiment   ", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Adjust Setup", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"Live Camera View", None))
        self.groupBox.setTitle("")
        self.label_12.setText(QCoreApplication.translate("Dialog", u"CONNECTED_STATUS", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Camera", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"(no camera selected)", None))

        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Scan", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Disconnect", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Exposure", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Framerate", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Brightness", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Framerate", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Gamma", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Serial Interface", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"CONNECTED_STATUS", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("Dialog", u"(no serial device selected)", None))

        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Scan", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"Disconnect", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Serial Device: DEVICE_NAME_AND_TYPE", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"Save Changes", None))
    # retranslateUi

