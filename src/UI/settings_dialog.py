# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(898, 685)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_13 = QLabel(Dialog)
        self.label_13.setObjectName(u"label_13")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(18)
        self.label_13.setFont(font)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_13, 0, 2, 1, 1)

        self.label_11 = QLabel(Dialog)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.label_camera_status = QLabel(self.groupBox)
        self.label_camera_status.setObjectName(u"label_camera_status")
        sizePolicy.setHeightForWidth(self.label_camera_status.sizePolicy().hasHeightForWidth())
        self.label_camera_status.setSizePolicy(sizePolicy)
        self.label_camera_status.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_camera_status, 1, 2, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(12)
        self.label.setFont(font1)

        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.combo_camera = QComboBox(self.groupBox)
        self.combo_camera.addItem("")
        self.combo_camera.setObjectName(u"combo_camera")

        self.horizontalLayout_6.addWidget(self.combo_camera)

        self.btn_scan_camera = QPushButton(self.groupBox)
        self.btn_scan_camera.setObjectName(u"btn_scan_camera")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_scan_camera.sizePolicy().hasHeightForWidth())
        self.btn_scan_camera.setSizePolicy(sizePolicy2)

        self.horizontalLayout_6.addWidget(self.btn_scan_camera)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.btn_connect_camera = QPushButton(self.groupBox)
        self.btn_connect_camera.setObjectName(u"btn_connect_camera")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_connect_camera.sizePolicy().hasHeightForWidth())
        self.btn_connect_camera.setSizePolicy(sizePolicy3)

        self.horizontalLayout_2.addWidget(self.btn_connect_camera)

        self.btn_disc_camera = QPushButton(self.groupBox)
        self.btn_disc_camera.setObjectName(u"btn_disc_camera")

        self.horizontalLayout_2.addWidget(self.btn_disc_camera)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_18 = QLabel(self.groupBox)
        self.label_18.setObjectName(u"label_18")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy4)
        font2 = QFont()
        font2.setPointSize(14)
        self.label_18.setFont(font2)

        self.gridLayout_2.addWidget(self.label_18, 0, 0, 1, 1)

        self.combo_framerate = QComboBox(self.groupBox)
        self.combo_framerate.addItem("")
        self.combo_framerate.addItem("")
        self.combo_framerate.addItem("")
        self.combo_framerate.addItem("")
        self.combo_framerate.setObjectName(u"combo_framerate")
        self.combo_framerate.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_2.addWidget(self.combo_framerate, 1, 2, 1, 1)

        self.spin_IR_left = QSpinBox(self.groupBox)
        self.spin_IR_left.setObjectName(u"spin_IR_left")

        self.gridLayout_2.addWidget(self.spin_IR_left, 7, 1, 1, 1)

        self.hslider_IR_right = QSlider(self.groupBox)
        self.hslider_IR_right.setObjectName(u"hslider_IR_right")
        self.hslider_IR_right.setMaximum(100)
        self.hslider_IR_right.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.hslider_IR_right, 8, 2, 1, 1)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 7, 0, 1, 1)

        self.spin_framerate = QSpinBox(self.groupBox)
        self.spin_framerate.setObjectName(u"spin_framerate")
        self.spin_framerate.setMaximum(100)

        self.gridLayout_2.addWidget(self.spin_framerate, 1, 1, 1, 1)

        self.hslider_gamma = QSlider(self.groupBox)
        self.hslider_gamma.setObjectName(u"hslider_gamma")
        self.hslider_gamma.setEnabled(False)
        self.hslider_gamma.setMaximum(100)
        self.hslider_gamma.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.hslider_gamma, 3, 2, 1, 1)

        self.spin_IR_bottom = QSpinBox(self.groupBox)
        self.spin_IR_bottom.setObjectName(u"spin_IR_bottom")
        self.spin_IR_bottom.setMaximum(100)

        self.gridLayout_2.addWidget(self.spin_IR_bottom, 6, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.label_6, 6, 0, 1, 1)

        self.spin_gamma = QSpinBox(self.groupBox)
        self.spin_gamma.setObjectName(u"spin_gamma")
        self.spin_gamma.setEnabled(False)
        self.spin_gamma.setMaximum(100)

        self.gridLayout_2.addWidget(self.spin_gamma, 3, 1, 1, 1)

        self.hslider_IR_left = QSlider(self.groupBox)
        self.hslider_IR_left.setObjectName(u"hslider_IR_left")
        self.hslider_IR_left.setMaximum(100)
        self.hslider_IR_left.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.hslider_IR_left, 7, 2, 1, 1)

        self.hslider_brightness = QSlider(self.groupBox)
        self.hslider_brightness.setObjectName(u"hslider_brightness")
        self.hslider_brightness.setEnabled(False)
        self.hslider_brightness.setMaximum(100)
        self.hslider_brightness.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.hslider_brightness, 2, 2, 1, 1)

        self.label_17 = QLabel(self.groupBox)
        self.label_17.setObjectName(u"label_17")
        sizePolicy4.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy4)
        self.label_17.setFont(font2)

        self.gridLayout_2.addWidget(self.label_17, 5, 0, 1, 1)

        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 8, 0, 1, 1)

        self.hslider_IR_bottom = QSlider(self.groupBox)
        self.hslider_IR_bottom.setObjectName(u"hslider_IR_bottom")
        self.hslider_IR_bottom.setMaximum(100)
        self.hslider_IR_bottom.setTracking(True)
        self.hslider_IR_bottom.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.hslider_IR_bottom, 6, 2, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)

        self.spin_brightness = QSpinBox(self.groupBox)
        self.spin_brightness.setObjectName(u"spin_brightness")
        self.spin_brightness.setEnabled(False)
        self.spin_brightness.setMaximum(100)

        self.gridLayout_2.addWidget(self.spin_brightness, 2, 1, 1, 1)

        self.spin_IR_right = QSpinBox(self.groupBox)
        self.spin_IR_right.setObjectName(u"spin_IR_right")

        self.gridLayout_2.addWidget(self.spin_IR_right, 8, 1, 1, 1)

        self.combo_exposure = QComboBox(self.groupBox)
        self.combo_exposure.setObjectName(u"combo_exposure")
        self.combo_exposure.setEnabled(False)

        self.gridLayout_2.addWidget(self.combo_exposure, 4, 2, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.label_7, 4, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        sizePolicy4.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy4)
        self.label_9.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label_9)

        self.label_serial_status = QLabel(self.groupBox)
        self.label_serial_status.setObjectName(u"label_serial_status")
        sizePolicy4.setHeightForWidth(self.label_serial_status.sizePolicy().hasHeightForWidth())
        self.label_serial_status.setSizePolicy(sizePolicy4)
        self.label_serial_status.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_serial_status)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.combo_serial = QComboBox(self.groupBox)
        self.combo_serial.addItem("")
        self.combo_serial.setObjectName(u"combo_serial")
        sizePolicy.setHeightForWidth(self.combo_serial.sizePolicy().hasHeightForWidth())
        self.combo_serial.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.combo_serial)

        self.btn_scan_serial = QPushButton(self.groupBox)
        self.btn_scan_serial.setObjectName(u"btn_scan_serial")
        sizePolicy2.setHeightForWidth(self.btn_scan_serial.sizePolicy().hasHeightForWidth())
        self.btn_scan_serial.setSizePolicy(sizePolicy2)

        self.horizontalLayout_5.addWidget(self.btn_scan_serial)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_connect_serial = QPushButton(self.groupBox)
        self.btn_connect_serial.setObjectName(u"btn_connect_serial")

        self.horizontalLayout_4.addWidget(self.btn_connect_serial)

        self.btn_disc_serial = QPushButton(self.groupBox)
        self.btn_disc_serial.setObjectName(u"btn_disc_serial")

        self.horizontalLayout_4.addWidget(self.btn_disc_serial)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout.addWidget(self.label_8)

        self.label_serial_info = QLabel(self.groupBox)
        self.label_serial_info.setObjectName(u"label_serial_info")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_serial_info.sizePolicy().hasHeightForWidth())
        self.label_serial_info.setSizePolicy(sizePolicy5)

        self.horizontalLayout.addWidget(self.label_serial_info)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 2, 2, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.checkbox_infrared_live = QCheckBox(self.groupBox_2)
        self.checkbox_infrared_live.setObjectName(u"checkbox_infrared_live")
        self.checkbox_infrared_live.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.checkbox_infrared_live.sizePolicy().hasHeightForWidth())
        self.checkbox_infrared_live.setSizePolicy(sizePolicy2)

        self.gridLayout_4.addWidget(self.checkbox_infrared_live, 0, 1, 1, 1)

        self.label_16 = QLabel(self.groupBox_2)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_4.addWidget(self.label_16, 0, 2, 1, 1)

        self.label_15 = QLabel(self.groupBox_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setEnabled(False)
        sizePolicy6 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy6)

        self.gridLayout_4.addWidget(self.label_15, 0, 0, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_4)

        self.label_live_video_feed = QLabel(self.groupBox_2)
        self.label_live_video_feed.setObjectName(u"label_live_video_feed")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_live_video_feed.sizePolicy().hasHeightForWidth())
        self.label_live_video_feed.setSizePolicy(sizePolicy7)

        self.verticalLayout_5.addWidget(self.label_live_video_feed)


        self.verticalLayout_3.addWidget(self.groupBox_2)


        self.gridLayout.addLayout(self.verticalLayout_3, 1, 2, 1, 1)

        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 1, 1, 1, 1)


        self.retranslateUi(Dialog)

        self.combo_framerate.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"Live Camera View", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Adjust Setup", None))
        self.groupBox.setTitle("")
        self.label_camera_status.setText(QCoreApplication.translate("Dialog", u"CONNECTED_STATUS", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Camera", None))
        self.combo_camera.setItemText(0, QCoreApplication.translate("Dialog", u"No cameras available", None))

        self.btn_scan_camera.setText(QCoreApplication.translate("Dialog", u"Scan", None))
        self.btn_connect_camera.setText(QCoreApplication.translate("Dialog", u"Connect", None))
        self.btn_disc_camera.setText(QCoreApplication.translate("Dialog", u"Disconnect", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"Camera Settings", None))
        self.combo_framerate.setItemText(0, QCoreApplication.translate("Dialog", u"20", None))
        self.combo_framerate.setItemText(1, QCoreApplication.translate("Dialog", u"30", None))
        self.combo_framerate.setItemText(2, QCoreApplication.translate("Dialog", u"60", None))
        self.combo_framerate.setItemText(3, QCoreApplication.translate("Dialog", u"90", None))

        self.label_10.setText(QCoreApplication.translate("Dialog", u"IR Left", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"IR Bottom", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"Infrared Lights", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"IR Right", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Framerate", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Exposure", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Gamma", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Brightness", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Serial Interface", None))
        self.label_serial_status.setText(QCoreApplication.translate("Dialog", u"CONNECTED_STATUS", None))
        self.combo_serial.setItemText(0, QCoreApplication.translate("Dialog", u"(no serial device selected)", None))

        self.btn_scan_serial.setText(QCoreApplication.translate("Dialog", u"Scan", None))
        self.btn_connect_serial.setText(QCoreApplication.translate("Dialog", u"Connect", None))
        self.btn_disc_serial.setText(QCoreApplication.translate("Dialog", u"Disconnect", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Serial Info:", None))
        self.label_serial_info.setText(QCoreApplication.translate("Dialog", u"DEVICE_NAME_AND_TYPE", None))
        self.groupBox_2.setTitle("")
        self.checkbox_infrared_live.setText(QCoreApplication.translate("Dialog", u"Enabled", None))
        self.label_16.setText("")
        self.label_15.setText(QCoreApplication.translate("Dialog", u"Infrared", None))
        self.label_live_video_feed.setText("")
    # retranslateUi

