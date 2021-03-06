# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_design.ui'
##
## Created by: Qt User Interface Compiler version 6.0.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from pyqtgraph import PlotWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1219, 844)
        self.actionExperiment = QAction(MainWindow)
        self.actionExperiment.setObjectName(u"actionExperiment")
        self.actionStimulus_Profile = QAction(MainWindow)
        self.actionStimulus_Profile.setObjectName(u"actionStimulus_Profile")
        self.actionExperiment_2 = QAction(MainWindow)
        self.actionExperiment_2.setObjectName(u"actionExperiment_2")
        self.actionStimulus_Profile_2 = QAction(MainWindow)
        self.actionStimulus_Profile_2.setObjectName(u"actionStimulus_Profile_2")
        self.actionCamera = QAction(MainWindow)
        self.actionCamera.setObjectName(u"actionCamera")
        self.actionSerial_Interface = QAction(MainWindow)
        self.actionSerial_Interface.setObjectName(u"actionSerial_Interface")
        self.actionCurrent_Run_Profile = QAction(MainWindow)
        self.actionCurrent_Run_Profile.setObjectName(u"actionCurrent_Run_Profile")
        self.actionSelected_Experiment = QAction(MainWindow)
        self.actionSelected_Experiment.setObjectName(u"actionSelected_Experiment")
        self.actionAll_Experiments = QAction(MainWindow)
        self.actionAll_Experiments.setObjectName(u"actionAll_Experiments")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout.addWidget(self.label_7)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.listWidget_3 = QListWidget(self.groupBox_4)
        self.listWidget_3.setObjectName(u"listWidget_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.listWidget_3.sizePolicy().hasHeightForWidth())
        self.listWidget_3.setSizePolicy(sizePolicy1)

        self.verticalLayout_5.addWidget(self.listWidget_3)


        self.gridLayout_3.addWidget(self.groupBox_4, 1, 1, 2, 1)

        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.listWidget = QListWidget(self.groupBox_2)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.listWidget, 1, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")

        self.gridLayout_2.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_3.addWidget(self.label_10)

        self.listWidget_2 = QListWidget(self.groupBox_3)
        self.listWidget_2.setObjectName(u"listWidget_2")
        sizePolicy2.setHeightForWidth(self.listWidget_2.sizePolicy().hasHeightForWidth())
        self.listWidget_2.setSizePolicy(sizePolicy2)

        self.verticalLayout_3.addWidget(self.listWidget_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")

        self.verticalLayout_3.addLayout(self.horizontalLayout_6)


        self.gridLayout_3.addWidget(self.groupBox_3, 2, 0, 1, 1)

        self.temp_status_hlayout_2 = QHBoxLayout()
        self.temp_status_hlayout_2.setObjectName(u"temp_status_hlayout_2")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)

        self.temp_status_hlayout_2.addWidget(self.label_3)

        self.current_temp_2 = QLabel(self.groupBox)
        self.current_temp_2.setObjectName(u"current_temp_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.current_temp_2.sizePolicy().hasHeightForWidth())
        self.current_temp_2.setSizePolicy(sizePolicy4)
        palette = QPalette()
        brush = QBrush(QColor(255, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush1 = QBrush(QColor(216, 222, 233, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        brush2 = QBrush(QColor(120, 136, 168, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        self.current_temp_2.setPalette(palette)

        self.temp_status_hlayout_2.addWidget(self.current_temp_2)

        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy5)

        self.temp_status_hlayout_2.addWidget(self.pushButton_2)


        self.gridLayout_3.addLayout(self.temp_status_hlayout_2, 0, 2, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush3 = QBrush(QColor(60, 68, 84, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush3)
        brush4 = QBrush(QColor(30, 34, 42, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush4)
        brush5 = QBrush(QColor(45, 51, 63, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush2)
        brush6 = QBrush(QColor(80, 90, 112, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush1)
        brush7 = QBrush(QColor(255, 255, 255, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush7)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        brush8 = QBrush(QColor(67, 76, 94, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush8)
        brush9 = QBrush(QColor(59, 66, 82, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush9)
        brush10 = QBrush(QColor(118, 118, 118, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        brush11 = QBrush(QColor(143, 188, 187, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Highlight, brush11)
        brush12 = QBrush(QColor(46, 52, 64, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.HighlightedText, brush12)
        brush13 = QBrush(QColor(94, 129, 172, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Link, brush13)
        brush14 = QBrush(QColor(124, 183, 255, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.LinkVisited, brush14)
        brush15 = QBrush(QColor(20, 26, 33, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush15)
        brush16 = QBrush(QColor(0, 0, 0, 255))
        brush16.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.NoRole, brush16)
        brush17 = QBrush(QColor(53, 57, 69, 255))
        brush17.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush17)
        brush18 = QBrush(QColor(211, 218, 227, 255))
        brush18.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush18)
        brush19 = QBrush(QColor(0, 0, 0, 128))
        brush19.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush19)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette1.setBrush(QPalette.Inactive, QPalette.Highlight, brush11)
        palette1.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush12)
        palette1.setBrush(QPalette.Inactive, QPalette.Link, brush13)
        palette1.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush14)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush15)
        brush20 = QBrush(QColor(0, 0, 0, 255))
        brush20.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Inactive, QPalette.NoRole, brush20)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush17)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush18)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush19)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush3)
        brush21 = QBrush(QColor(177, 177, 177, 255))
        brush21.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush21)
        palette1.setBrush(QPalette.Disabled, QPalette.Highlight, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Link, brush13)
        palette1.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush14)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush15)
        brush22 = QBrush(QColor(0, 0, 0, 255))
        brush22.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Disabled, QPalette.NoRole, brush22)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush17)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush18)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush19)
#endif
        self.label.setPalette(palette1)

        self.horizontalLayout_2.addWidget(self.label)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)

        self.groupBox_5 = QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy6)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_8 = QLabel(self.groupBox_5)
        self.label_8.setObjectName(u"label_8")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy7)

        self.verticalLayout_4.addWidget(self.label_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_13 = QLabel(self.groupBox_5)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_9.addWidget(self.label_13)

        self.lineEdit_4 = QLineEdit(self.groupBox_5)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy7.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy7)

        self.horizontalLayout_9.addWidget(self.lineEdit_4)

        self.checkBox = QCheckBox(self.groupBox_5)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_9.addWidget(self.checkBox)

        self.lineEdit_5 = QLineEdit(self.groupBox_5)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.horizontalLayout_9.addWidget(self.lineEdit_5)

        self.pushButton_10 = QPushButton(self.groupBox_5)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.horizontalLayout_9.addWidget(self.pushButton_10)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.label_15 = QLabel(self.groupBox_5)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_4.addWidget(self.label_15)

        self.graphicsView = PlotWidget(self.groupBox_5)
        self.graphicsView.setObjectName(u"graphicsView")
        sizePolicy1.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy1)

        self.verticalLayout_4.addWidget(self.graphicsView)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_16 = QLabel(self.groupBox_5)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_19.addWidget(self.label_16)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_4)

        self.pushButton_6 = QPushButton(self.groupBox_5)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_19.addWidget(self.pushButton_6)


        self.verticalLayout_4.addLayout(self.horizontalLayout_19)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pushButton_7 = QPushButton(self.groupBox_5)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy7.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy7)

        self.gridLayout_4.addWidget(self.pushButton_7, 5, 0, 1, 1)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.pushButton_3 = QPushButton(self.groupBox_5)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_17.addWidget(self.pushButton_3)

        self.pushButton = QPushButton(self.groupBox_5)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_17.addWidget(self.pushButton)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_5)


        self.gridLayout_4.addLayout(self.horizontalLayout_17, 0, 1, 1, 1)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_11 = QLabel(self.groupBox_5)
        self.label_11.setObjectName(u"label_11")
        sizePolicy4.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy4)

        self.horizontalLayout_11.addWidget(self.label_11)

        self.checkBox_3 = QCheckBox(self.groupBox_5)
        self.checkBox_3.setObjectName(u"checkBox_3")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.checkBox_3.sizePolicy().hasHeightForWidth())
        self.checkBox_3.setSizePolicy(sizePolicy8)
        self.checkBox_3.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_11.addWidget(self.checkBox_3)

        self.lineEdit = QLineEdit(self.groupBox_5)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy7.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy7)

        self.horizontalLayout_11.addWidget(self.lineEdit)


        self.horizontalLayout_16.addLayout(self.horizontalLayout_11)


        self.gridLayout_4.addLayout(self.horizontalLayout_16, 0, 0, 1, 1)

        self.pushButton_9 = QPushButton(self.groupBox_5)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy8.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy8)

        self.gridLayout_4.addWidget(self.pushButton_9, 7, 1, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.pushButton_4 = QPushButton(self.groupBox_5)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy9)

        self.horizontalLayout_12.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.groupBox_5)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_12.addWidget(self.pushButton_5)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_2)


        self.gridLayout_4.addLayout(self.horizontalLayout_12, 1, 1, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_12 = QLabel(self.groupBox_5)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_8.addWidget(self.label_12)

        self.checkBox_2 = QCheckBox(self.groupBox_5)
        self.checkBox_2.setObjectName(u"checkBox_2")
        sizePolicy8.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy8)
        self.checkBox_2.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_8.addWidget(self.checkBox_2)

        self.lineEdit_2 = QLineEdit(self.groupBox_5)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy7.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy7)

        self.horizontalLayout_8.addWidget(self.lineEdit_2)


        self.gridLayout_4.addLayout(self.horizontalLayout_8, 1, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.groupBox_5)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy8.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy8)

        self.gridLayout_4.addWidget(self.pushButton_8, 7, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(self.groupBox_5)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_7.addWidget(self.label_5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.label_14 = QLabel(self.groupBox_5)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_7.addWidget(self.label_14)

        self.lineEdit_3 = QLineEdit(self.groupBox_5)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy9.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy9)
        self.lineEdit_3.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_7.addWidget(self.lineEdit_3)


        self.gridLayout_4.addLayout(self.horizontalLayout_7, 4, 0, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSlider = QSlider(self.groupBox_5)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        sizePolicy8.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy8)
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_13.addWidget(self.horizontalSlider)


        self.gridLayout_4.addLayout(self.horizontalLayout_13, 4, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_4)


        self.gridLayout_3.addWidget(self.groupBox_5, 1, 2, 2, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1219, 23))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuNew = QMenu(self.menuFile)
        self.menuNew.setObjectName(u"menuNew")
        self.menuOpen = QMenu(self.menuFile)
        self.menuOpen.setObjectName(u"menuOpen")
        self.menuSave = QMenu(self.menuFile)
        self.menuSave.setObjectName(u"menuSave")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuRun = QMenu(self.menubar)
        self.menuRun.setObjectName(u"menuRun")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.menuNew.menuAction())
        self.menuFile.addAction(self.menuOpen.menuAction())
        self.menuFile.addAction(self.menuSave.menuAction())
        self.menuNew.addAction(self.actionExperiment)
        self.menuNew.addAction(self.actionStimulus_Profile)
        self.menuOpen.addSeparator()
        self.menuOpen.addSeparator()
        self.menuOpen.addAction(self.actionExperiment_2)
        self.menuOpen.addAction(self.actionStimulus_Profile_2)
        self.menuSave.addAction(self.actionCurrent_Run_Profile)
        self.menuSettings.addAction(self.actionCamera)
        self.menuSettings.addAction(self.actionSerial_Interface)
        self.menuRun.addSeparator()
        self.menuRun.addAction(self.actionSelected_Experiment)
        self.menuRun.addAction(self.actionAll_Experiments)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionExperiment.setText(QCoreApplication.translate("MainWindow", u"Experiment", None))
        self.actionStimulus_Profile.setText(QCoreApplication.translate("MainWindow", u"Stimulus Profile", None))
        self.actionExperiment_2.setText(QCoreApplication.translate("MainWindow", u"Experiment", None))
        self.actionStimulus_Profile_2.setText(QCoreApplication.translate("MainWindow", u"Stimulus Profile", None))
        self.actionCamera.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.actionSerial_Interface.setText(QCoreApplication.translate("MainWindow", u"Serial Interface", None))
        self.actionCurrent_Run_Profile.setText(QCoreApplication.translate("MainWindow", u"Current Run Profile", None))
        self.actionSelected_Experiment.setText(QCoreApplication.translate("MainWindow", u"Selected Experiment", None))
        self.actionAll_Experiments.setText(QCoreApplication.translate("MainWindow", u"All Experiments", None))
        self.groupBox.setTitle("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Working dir: C:/PATH_TO_EXP_FILES", None))
        self.groupBox_4.setTitle("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Experiements to Run", None))
        self.groupBox_2.setTitle("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Experiments", None))
        self.groupBox_3.setTitle("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Stimulus Profiles", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.current_temp_2.setText(QCoreApplication.translate("MainWindow", u"STATUSTEXT", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Current Temp in Chamber: ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TEMP_VAL", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.groupBox_5.setTitle("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"EXP NAME", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Full Duration", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Save log", None))
        self.lineEdit_5.setText(QCoreApplication.translate("MainWindow", u"\"Path to logs\"", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Set path", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Stimulus Profile: PROFILE NAME", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Add Stimulus", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Center Graph", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"From", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Save as", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"To", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"End", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Load Stim Profile", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"LED Intensity", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuNew.setTitle(QCoreApplication.translate("MainWindow", u"New", None))
        self.menuOpen.setTitle(QCoreApplication.translate("MainWindow", u"Open", None))
        self.menuSave.setTitle(QCoreApplication.translate("MainWindow", u"Save", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuRun.setTitle(QCoreApplication.translate("MainWindow", u"Run", None))
    # retranslateUi

