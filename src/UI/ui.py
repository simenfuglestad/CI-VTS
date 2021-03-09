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
        MainWindow.resize(1219, 760)
        self.actionExperiment = QAction(MainWindow)
        self.actionExperiment.setObjectName(u"actionExperiment")
        self.actionStimulus_Profile = QAction(MainWindow)
        self.actionStimulus_Profile.setObjectName(u"actionStimulus_Profile")
        self.actionExperiment_2 = QAction(MainWindow)
        self.actionExperiment_2.setObjectName(u"actionExperiment_2")
        self.actionStimulus_Profile_2 = QAction(MainWindow)
        self.actionStimulus_Profile_2.setObjectName(u"actionStimulus_Profile_2")
        self.actionSetup = QAction(MainWindow)
        self.actionSetup.setObjectName(u"actionSetup")
        self.actionGeneral = QAction(MainWindow)
        self.actionGeneral.setObjectName(u"actionGeneral")
        self.actionCurrent_Run_Profile = QAction(MainWindow)
        self.actionCurrent_Run_Profile.setObjectName(u"actionCurrent_Run_Profile")
        self.actionSelected_Experiment = QAction(MainWindow)
        self.actionSelected_Experiment.setObjectName(u"actionSelected_Experiment")
        self.actionAll_Experiments = QAction(MainWindow)
        self.actionAll_Experiments.setObjectName(u"actionAll_Experiments")
        self.actionSelected_Experiments = QAction(MainWindow)
        self.actionSelected_Experiments.setObjectName(u"actionSelected_Experiments")
        self.actionAll_Experiments_2 = QAction(MainWindow)
        self.actionAll_Experiments_2.setObjectName(u"actionAll_Experiments_2")
        self.actionView = QAction(MainWindow)
        self.actionView.setObjectName(u"actionView")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_main = QGroupBox(self.centralwidget)
        self.groupBox_main.setObjectName(u"groupBox_main")
        self.gridLayout_3 = QGridLayout(self.groupBox_main)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox_3 = QGroupBox(self.groupBox_main)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_8 = QGridLayout(self.groupBox_3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.list_stim_profiles = QListWidget(self.groupBox_3)
        self.list_stim_profiles.setObjectName(u"list_stim_profiles")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_stim_profiles.sizePolicy().hasHeightForWidth())
        self.list_stim_profiles.setSizePolicy(sizePolicy)

        self.gridLayout_8.addWidget(self.list_stim_profiles, 1, 0, 1, 2)

        self.pushButton_4 = QPushButton(self.groupBox_3)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_8.addWidget(self.pushButton_4, 3, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.groupBox_3)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_8.addWidget(self.pushButton_3, 3, 1, 1, 1)

        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_8.addWidget(self.label_10, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_3, 4, 0, 1, 1)

        self.temp_status_hlayout_2 = QHBoxLayout()
        self.temp_status_hlayout_2.setObjectName(u"temp_status_hlayout_2")
        self.label_status = QLabel(self.groupBox_main)
        self.label_status.setObjectName(u"label_status")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_status.sizePolicy().hasHeightForWidth())
        self.label_status.setSizePolicy(sizePolicy1)

        self.temp_status_hlayout_2.addWidget(self.label_status)

        self.label_status_value = QLabel(self.groupBox_main)
        self.label_status_value.setObjectName(u"label_status_value")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_status_value.sizePolicy().hasHeightForWidth())
        self.label_status_value.setSizePolicy(sizePolicy2)
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
        self.label_status_value.setPalette(palette)
        self.label_status_value.setLayoutDirection(Qt.LeftToRight)

        self.temp_status_hlayout_2.addWidget(self.label_status_value)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.temp_status_hlayout_2.addItem(self.horizontalSpacer_6)

        self.btn_run = QPushButton(self.groupBox_main)
        self.btn_run.setObjectName(u"btn_run")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_run.sizePolicy().hasHeightForWidth())
        self.btn_run.setSizePolicy(sizePolicy3)

        self.temp_status_hlayout_2.addWidget(self.btn_run)


        self.gridLayout_3.addLayout(self.temp_status_hlayout_2, 1, 2, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_working_dir = QLabel(self.groupBox_main)
        self.label_working_dir.setObjectName(u"label_working_dir")

        self.horizontalLayout_5.addWidget(self.label_working_dir)


        self.gridLayout_3.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox_main)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_temp_val = QLabel(self.groupBox_main)
        self.label_temp_val.setObjectName(u"label_temp_val")
        sizePolicy1.setHeightForWidth(self.label_temp_val.sizePolicy().hasHeightForWidth())
        self.label_temp_val.setSizePolicy(sizePolicy1)
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
        self.label_temp_val.setPalette(palette1)

        self.horizontalLayout_2.addWidget(self.label_temp_val)

        self.label_4 = QLabel(self.groupBox_main)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)

        self.groupBox_2 = QGroupBox(self.groupBox_main)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 3, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)

        self.list_exp_profiles = QListWidget(self.groupBox_2)
        self.list_exp_profiles.setObjectName(u"list_exp_profiles")
        sizePolicy.setHeightForWidth(self.list_exp_profiles.sizePolicy().hasHeightForWidth())
        self.list_exp_profiles.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.list_exp_profiles, 2, 0, 1, 2)

        self.pushButton_2 = QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_2.addWidget(self.pushButton_2, 3, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_2, 2, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.groupBox_main)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy2.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy2)
        self.gridLayout_9 = QGridLayout(self.groupBox_4)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.pushButton_5 = QPushButton(self.groupBox_4)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_9.addWidget(self.pushButton_5, 3, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout.addWidget(self.label_7)


        self.gridLayout_9.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.groupBox_4)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_9.addWidget(self.pushButton_6, 3, 1, 1, 1)

        self.list_experiments_to_run = QListWidget(self.groupBox_4)
        self.list_experiments_to_run.setObjectName(u"list_experiments_to_run")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.list_experiments_to_run.sizePolicy().hasHeightForWidth())
        self.list_experiments_to_run.setSizePolicy(sizePolicy4)

        self.gridLayout_9.addWidget(self.list_experiments_to_run, 1, 0, 1, 2)


        self.gridLayout_3.addWidget(self.groupBox_4, 2, 1, 3, 1)

        self.tabWidget = QTabWidget(self.groupBox_main)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_exp_profile = QWidget()
        self.tab_exp_profile.setObjectName(u"tab_exp_profile")
        self.horizontalLayout_3 = QHBoxLayout(self.tab_exp_profile)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox_5 = QGroupBox(self.tab_exp_profile)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy5)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.line_edit_duration = QLineEdit(self.groupBox_5)
        self.line_edit_duration.setObjectName(u"line_edit_duration")
        sizePolicy3.setHeightForWidth(self.line_edit_duration.sizePolicy().hasHeightForWidth())
        self.line_edit_duration.setSizePolicy(sizePolicy3)

        self.horizontalLayout_4.addWidget(self.line_edit_duration)

        self.spin_duration_hour = QSpinBox(self.groupBox_5)
        self.spin_duration_hour.setObjectName(u"spin_duration_hour")

        self.horizontalLayout_4.addWidget(self.spin_duration_hour)

        self.spin_duration_min = QSpinBox(self.groupBox_5)
        self.spin_duration_min.setObjectName(u"spin_duration_min")
        self.spin_duration_min.setMaximum(59)

        self.horizontalLayout_4.addWidget(self.spin_duration_min)

        self.spin_duration_sec = QSpinBox(self.groupBox_5)
        self.spin_duration_sec.setObjectName(u"spin_duration_sec")
        self.spin_duration_sec.setMaximum(59)

        self.horizontalLayout_4.addWidget(self.spin_duration_sec)


        self.gridLayout_5.addLayout(self.horizontalLayout_4, 0, 1, 1, 1)

        self.checkbox_save_video = QCheckBox(self.groupBox_5)
        self.checkbox_save_video.setObjectName(u"checkbox_save_video")
        sizePolicy3.setHeightForWidth(self.checkbox_save_video.sizePolicy().hasHeightForWidth())
        self.checkbox_save_video.setSizePolicy(sizePolicy3)
        self.checkbox_save_video.setLayoutDirection(Qt.RightToLeft)
        self.checkbox_save_video.setChecked(True)

        self.gridLayout_5.addWidget(self.checkbox_save_video, 3, 0, 1, 1)

        self.line_edit_video_path = QLineEdit(self.groupBox_5)
        self.line_edit_video_path.setObjectName(u"line_edit_video_path")

        self.gridLayout_5.addWidget(self.line_edit_video_path, 3, 1, 1, 1)

        self.label_13 = QLabel(self.groupBox_5)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_5.addWidget(self.label_13, 0, 0, 1, 1)

        self.checkbox_save_log = QCheckBox(self.groupBox_5)
        self.checkbox_save_log.setObjectName(u"checkbox_save_log")
        self.checkbox_save_log.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_5.addWidget(self.checkbox_save_log, 4, 0, 1, 1)

        self.btn_set_video_path = QPushButton(self.groupBox_5)
        self.btn_set_video_path.setObjectName(u"btn_set_video_path")

        self.gridLayout_5.addWidget(self.btn_set_video_path, 3, 2, 1, 1)

        self.btn_set_duration = QPushButton(self.groupBox_5)
        self.btn_set_duration.setObjectName(u"btn_set_duration")

        self.gridLayout_5.addWidget(self.btn_set_duration, 0, 2, 1, 1)

        self.line_edit_log_path = QLineEdit(self.groupBox_5)
        self.line_edit_log_path.setObjectName(u"line_edit_log_path")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.line_edit_log_path.sizePolicy().hasHeightForWidth())
        self.line_edit_log_path.setSizePolicy(sizePolicy6)

        self.gridLayout_5.addWidget(self.line_edit_log_path, 4, 1, 1, 1)

        self.btn_set_log_path = QPushButton(self.groupBox_5)
        self.btn_set_log_path.setObjectName(u"btn_set_log_path")

        self.gridLayout_5.addWidget(self.btn_set_log_path, 4, 2, 1, 1)

        self.checkbox_view_live = QCheckBox(self.groupBox_5)
        self.checkbox_view_live.setObjectName(u"checkbox_view_live")
        self.checkbox_view_live.setLayoutDirection(Qt.RightToLeft)
        self.checkbox_view_live.setCheckable(True)
        self.checkbox_view_live.setChecked(False)

        self.gridLayout_5.addWidget(self.checkbox_view_live, 5, 0, 1, 1)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.checkbox_live_ir = QCheckBox(self.groupBox_5)
        self.checkbox_live_ir.setObjectName(u"checkbox_live_ir")
        sizePolicy3.setHeightForWidth(self.checkbox_live_ir.sizePolicy().hasHeightForWidth())
        self.checkbox_live_ir.setSizePolicy(sizePolicy3)
        palette2 = QPalette()
        brush23 = QBrush(QColor(100, 103, 108, 255))
        brush23.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush23)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Midlight, brush5)
        palette2.setBrush(QPalette.Active, QPalette.Dark, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush6)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette2.setBrush(QPalette.Active, QPalette.BrightText, brush7)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette2.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette2.setBrush(QPalette.Active, QPalette.Highlight, brush11)
        palette2.setBrush(QPalette.Active, QPalette.HighlightedText, brush12)
        palette2.setBrush(QPalette.Active, QPalette.Link, brush13)
        palette2.setBrush(QPalette.Active, QPalette.LinkVisited, brush14)
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush15)
        palette2.setBrush(QPalette.Active, QPalette.NoRole, brush16)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipBase, brush17)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipText, brush18)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush19)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Midlight, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.BrightText, brush7)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette2.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette2.setBrush(QPalette.Inactive, QPalette.Highlight, brush11)
        palette2.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush12)
        palette2.setBrush(QPalette.Inactive, QPalette.Link, brush13)
        palette2.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush14)
        palette2.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush15)
        brush24 = QBrush(QColor(0, 0, 0, 255))
        brush24.setStyle(Qt.NoBrush)
        palette2.setBrush(QPalette.Inactive, QPalette.NoRole, brush24)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush17)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush18)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush19)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Midlight, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.BrightText, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Shadow, brush21)
        palette2.setBrush(QPalette.Disabled, QPalette.Highlight, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Link, brush13)
        palette2.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush14)
        palette2.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush15)
        brush25 = QBrush(QColor(0, 0, 0, 255))
        brush25.setStyle(Qt.NoBrush)
        palette2.setBrush(QPalette.Disabled, QPalette.NoRole, brush25)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush17)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush18)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush19)
#endif
        self.checkbox_live_ir.setPalette(palette2)
        font = QFont()
        font.setStrikeOut(False)
        self.checkbox_live_ir.setFont(font)
        self.checkbox_live_ir.setLayoutDirection(Qt.RightToLeft)
        self.checkbox_live_ir.setCheckable(False)
        self.checkbox_live_ir.setChecked(False)

        self.horizontalLayout_20.addWidget(self.checkbox_live_ir)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_3)


        self.gridLayout_5.addLayout(self.horizontalLayout_20, 5, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_5)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")

        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_17 = QLabel(self.groupBox_5)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_6.addWidget(self.label_17)

        self.label_15 = QLabel(self.groupBox_5)
        self.label_15.setObjectName(u"label_15")
        sizePolicy5.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy5)

        self.horizontalLayout_6.addWidget(self.label_15)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.stim_profile_view = PlotWidget(self.groupBox_5)
        self.stim_profile_view.setObjectName(u"stim_profile_view")
        sizePolicy4.setHeightForWidth(self.stim_profile_view.sizePolicy().hasHeightForWidth())
        self.stim_profile_view.setSizePolicy(sizePolicy4)

        self.verticalLayout_4.addWidget(self.stim_profile_view)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_16 = QLabel(self.groupBox_5)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_19.addWidget(self.label_16)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_4)

        self.btn_center_graph = QPushButton(self.groupBox_5)
        self.btn_center_graph.setObjectName(u"btn_center_graph")

        self.horizontalLayout_19.addWidget(self.btn_center_graph)


        self.verticalLayout_4.addLayout(self.horizontalLayout_19)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.btn_add_stim = QPushButton(self.groupBox_5)
        self.btn_add_stim.setObjectName(u"btn_add_stim")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.btn_add_stim.sizePolicy().hasHeightForWidth())
        self.btn_add_stim.setSizePolicy(sizePolicy7)

        self.gridLayout_4.addWidget(self.btn_add_stim, 5, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(self.groupBox_5)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)

        self.horizontalLayout_7.addWidget(self.label_5)

        self.label_14 = QLabel(self.groupBox_5)
        self.label_14.setObjectName(u"label_14")
        sizePolicy5.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy5)

        self.horizontalLayout_7.addWidget(self.label_14)

        self.spinBox_2 = QSpinBox(self.groupBox_5)
        self.spinBox_2.setObjectName(u"spinBox_2")
        sizePolicy3.setHeightForWidth(self.spinBox_2.sizePolicy().hasHeightForWidth())
        self.spinBox_2.setSizePolicy(sizePolicy3)
        self.spinBox_2.setMaximum(100)

        self.horizontalLayout_7.addWidget(self.spinBox_2)


        self.gridLayout_4.addLayout(self.horizontalLayout_7, 4, 0, 1, 1)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.btn_inc_start = QPushButton(self.groupBox_5)
        self.btn_inc_start.setObjectName(u"btn_inc_start")

        self.horizontalLayout_17.addWidget(self.btn_inc_start)

        self.btn_dec_start = QPushButton(self.groupBox_5)
        self.btn_dec_start.setObjectName(u"btn_dec_start")

        self.horizontalLayout_17.addWidget(self.btn_dec_start)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_5)


        self.gridLayout_4.addLayout(self.horizontalLayout_17, 0, 1, 1, 1)

        self.btn_load_stim = QPushButton(self.groupBox_5)
        self.btn_load_stim.setObjectName(u"btn_load_stim")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.btn_load_stim.sizePolicy().hasHeightForWidth())
        self.btn_load_stim.setSizePolicy(sizePolicy8)

        self.gridLayout_4.addWidget(self.btn_load_stim, 7, 0, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.btn_inc_end = QPushButton(self.groupBox_5)
        self.btn_inc_end.setObjectName(u"btn_inc_end")
        sizePolicy6.setHeightForWidth(self.btn_inc_end.sizePolicy().hasHeightForWidth())
        self.btn_inc_end.setSizePolicy(sizePolicy6)

        self.horizontalLayout_12.addWidget(self.btn_inc_end)

        self.btn_dec_end = QPushButton(self.groupBox_5)
        self.btn_dec_end.setObjectName(u"btn_dec_end")

        self.horizontalLayout_12.addWidget(self.btn_dec_end)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_2)


        self.gridLayout_4.addLayout(self.horizontalLayout_12, 1, 1, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_12 = QLabel(self.groupBox_5)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_8.addWidget(self.label_12)

        self.checkbox_end = QCheckBox(self.groupBox_5)
        self.checkbox_end.setObjectName(u"checkbox_end")
        sizePolicy8.setHeightForWidth(self.checkbox_end.sizePolicy().hasHeightForWidth())
        self.checkbox_end.setSizePolicy(sizePolicy8)
        self.checkbox_end.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_8.addWidget(self.checkbox_end)

        self.line_edit_end = QLineEdit(self.groupBox_5)
        self.line_edit_end.setObjectName(u"line_edit_end")
        sizePolicy7.setHeightForWidth(self.line_edit_end.sizePolicy().hasHeightForWidth())
        self.line_edit_end.setSizePolicy(sizePolicy7)

        self.horizontalLayout_8.addWidget(self.line_edit_end)


        self.gridLayout_4.addLayout(self.horizontalLayout_8, 1, 0, 1, 1)

        self.btn_save_stim = QPushButton(self.groupBox_5)
        self.btn_save_stim.setObjectName(u"btn_save_stim")
        sizePolicy8.setHeightForWidth(self.btn_save_stim.sizePolicy().hasHeightForWidth())
        self.btn_save_stim.setSizePolicy(sizePolicy8)

        self.gridLayout_4.addWidget(self.btn_save_stim, 7, 1, 1, 1)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_11 = QLabel(self.groupBox_5)
        self.label_11.setObjectName(u"label_11")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy9)

        self.horizontalLayout_11.addWidget(self.label_11)

        self.checkbox_start = QCheckBox(self.groupBox_5)
        self.checkbox_start.setObjectName(u"checkbox_start")
        sizePolicy8.setHeightForWidth(self.checkbox_start.sizePolicy().hasHeightForWidth())
        self.checkbox_start.setSizePolicy(sizePolicy8)
        self.checkbox_start.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_11.addWidget(self.checkbox_start)

        self.line_edit_start = QLineEdit(self.groupBox_5)
        self.line_edit_start.setObjectName(u"line_edit_start")
        sizePolicy7.setHeightForWidth(self.line_edit_start.sizePolicy().hasHeightForWidth())
        self.line_edit_start.setSizePolicy(sizePolicy7)

        self.horizontalLayout_11.addWidget(self.line_edit_start)


        self.horizontalLayout_16.addLayout(self.horizontalLayout_11)


        self.gridLayout_4.addLayout(self.horizontalLayout_16, 0, 0, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.hslider_exp_LED = QSlider(self.groupBox_5)
        self.hslider_exp_LED.setObjectName(u"hslider_exp_LED")
        sizePolicy8.setHeightForWidth(self.hslider_exp_LED.sizePolicy().hasHeightForWidth())
        self.hslider_exp_LED.setSizePolicy(sizePolicy8)
        self.hslider_exp_LED.setOrientation(Qt.Horizontal)

        self.horizontalLayout_13.addWidget(self.hslider_exp_LED)


        self.gridLayout_4.addLayout(self.horizontalLayout_13, 4, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_4)


        self.horizontalLayout_3.addWidget(self.groupBox_5)

        self.tabWidget.addTab(self.tab_exp_profile, "")
        self.tab_exp_settings = QWidget()
        self.tab_exp_settings.setObjectName(u"tab_exp_settings")
        self.gridLayout_6 = QGridLayout(self.tab_exp_settings)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setVerticalSpacing(12)
        self.label_8 = QLabel(self.tab_exp_settings)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_8, 6, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_7.addItem(self.verticalSpacer_3, 5, 2, 1, 1)

        self.spinBox = QSpinBox(self.tab_exp_settings)
        self.spinBox.setObjectName(u"spinBox")
        sizePolicy3.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy3)

        self.gridLayout_7.addWidget(self.spinBox, 6, 3, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_7.addItem(self.verticalSpacer_2, 3, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_7.addItem(self.verticalSpacer, 1, 2, 1, 1)

        self.label_6 = QLabel(self.tab_exp_settings)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_6, 4, 2, 1, 1)

        self.checkBox_2 = QCheckBox(self.tab_exp_settings)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_7.addWidget(self.checkBox_2, 4, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.tab_exp_settings)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy6.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy6)

        self.gridLayout_7.addWidget(self.lineEdit_2, 4, 3, 1, 1)

        self.lineEdit = QLineEdit(self.tab_exp_settings)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy6.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy6)

        self.gridLayout_7.addWidget(self.lineEdit, 2, 3, 1, 1)

        self.label_3 = QLabel(self.tab_exp_settings)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_3, 2, 2, 1, 1)

        self.checkBox = QCheckBox(self.tab_exp_settings)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_7.addWidget(self.checkBox, 2, 1, 1, 1)

        self.comboBox = QComboBox(self.tab_exp_settings)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy10 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy10)

        self.gridLayout_7.addWidget(self.comboBox, 0, 3, 1, 1)

        self.label = QLabel(self.tab_exp_settings)
        self.label.setObjectName(u"label")
        sizePolicy11 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy11)

        self.gridLayout_7.addWidget(self.label, 0, 2, 1, 1)

        self.checkBox_3 = QCheckBox(self.tab_exp_settings)
        self.checkBox_3.setObjectName(u"checkBox_3")
        sizePolicy11.setHeightForWidth(self.checkBox_3.sizePolicy().hasHeightForWidth())
        self.checkBox_3.setSizePolicy(sizePolicy11)
        self.checkBox_3.setLayoutDirection(Qt.RightToLeft)
        self.checkBox_3.setAutoExclusive(False)

        self.gridLayout_7.addWidget(self.checkBox_3, 0, 1, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_7, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_exp_settings, "")

        self.gridLayout_3.addWidget(self.tabWidget, 2, 2, 3, 1)

        self.label_18 = QLabel(self.groupBox_main)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_3.addWidget(self.label_18, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_main, 0, 0, 1, 2)

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
        self.menuAnalysis = QMenu(self.menubar)
        self.menuAnalysis.setObjectName(u"menuAnalysis")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())
        self.menubar.addAction(self.menuAnalysis.menuAction())
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
        self.menuSettings.addAction(self.actionSetup)
        self.menuSettings.addAction(self.actionGeneral)
        self.menuRun.addAction(self.actionSelected_Experiments)
        self.menuRun.addAction(self.actionAll_Experiments_2)
        self.menuAnalysis.addAction(self.actionView)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionExperiment.setText(QCoreApplication.translate("MainWindow", u"Experiment", None))
        self.actionStimulus_Profile.setText(QCoreApplication.translate("MainWindow", u"Stimulus Profile", None))
        self.actionExperiment_2.setText(QCoreApplication.translate("MainWindow", u"Experiment", None))
        self.actionStimulus_Profile_2.setText(QCoreApplication.translate("MainWindow", u"Stimulus Profile", None))
        self.actionSetup.setText(QCoreApplication.translate("MainWindow", u"Setup", None))
        self.actionGeneral.setText(QCoreApplication.translate("MainWindow", u"Set Working Directory", None))
        self.actionCurrent_Run_Profile.setText(QCoreApplication.translate("MainWindow", u"Current Run Profile", None))
        self.actionSelected_Experiment.setText(QCoreApplication.translate("MainWindow", u"Selected Experiment", None))
        self.actionAll_Experiments.setText(QCoreApplication.translate("MainWindow", u"All Experiments", None))
        self.actionSelected_Experiments.setText(QCoreApplication.translate("MainWindow", u"Selected Experiments", None))
        self.actionAll_Experiments_2.setText(QCoreApplication.translate("MainWindow", u"All Experiments", None))
        self.actionView.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.groupBox_main.setTitle("")
        self.groupBox_3.setTitle("")
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Stimulus Profiles", None))
        self.label_status.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.label_status_value.setText(QCoreApplication.translate("MainWindow", u"STATUSTEXT", None))
        self.btn_run.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.label_working_dir.setText(QCoreApplication.translate("MainWindow", u"C:/PATH_TO_EXP_FILES", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Current Temp in Chamber: ", None))
        self.label_temp_val.setText(QCoreApplication.translate("MainWindow", u"TEMP_VAL", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.groupBox_2.setTitle("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Experiments", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.groupBox_4.setTitle("")
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Experiements to Run", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.groupBox_5.setTitle("")
        self.line_edit_duration.setText(QCoreApplication.translate("MainWindow", u"HH:MM:SS", None))
        self.checkbox_save_video.setText(QCoreApplication.translate("MainWindow", u"Save Video", None))
        self.line_edit_video_path.setText(QCoreApplication.translate("MainWindow", u"\"Path to video\"", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Full Duration", None))
        self.checkbox_save_log.setText(QCoreApplication.translate("MainWindow", u"Save log", None))
        self.btn_set_video_path.setText(QCoreApplication.translate("MainWindow", u"Set Video Path", None))
        self.btn_set_duration.setText(QCoreApplication.translate("MainWindow", u"Set Duration", None))
        self.line_edit_log_path.setText(QCoreApplication.translate("MainWindow", u"\"Path to logs\"", None))
        self.btn_set_log_path.setText(QCoreApplication.translate("MainWindow", u"Set Logs Path", None))
        self.checkbox_view_live.setText(QCoreApplication.translate("MainWindow", u"View Live", None))
        self.checkbox_live_ir.setText(QCoreApplication.translate("MainWindow", u"Infrared", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Stimulus profile:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"PROFILE NAME", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Add Stimulus", None))
        self.btn_center_graph.setText(QCoreApplication.translate("MainWindow", u"Center Graph", None))
        self.btn_add_stim.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"LED Intensity", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.btn_inc_start.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btn_dec_start.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn_load_stim.setText(QCoreApplication.translate("MainWindow", u"Load Profile", None))
        self.btn_inc_end.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btn_dec_end.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"To", None))
        self.checkbox_end.setText(QCoreApplication.translate("MainWindow", u"End", None))
        self.btn_save_stim.setText(QCoreApplication.translate("MainWindow", u"Save Profile", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"From", None))
        self.checkbox_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_exp_profile), QCoreApplication.translate("MainWindow", u"EXP_NAME", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Crowdsize", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Drug Name", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Drugs", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Genotype", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Genetics", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Hatching Time", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Dechorionated", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_exp_settings), QCoreApplication.translate("MainWindow", u"Additional Settings", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"C:/PATH_TO_STIM_FILES", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuNew.setTitle(QCoreApplication.translate("MainWindow", u"New", None))
        self.menuOpen.setTitle(QCoreApplication.translate("MainWindow", u"Open", None))
        self.menuSave.setTitle(QCoreApplication.translate("MainWindow", u"Save", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuRun.setTitle(QCoreApplication.translate("MainWindow", u"Run", None))
        self.menuAnalysis.setTitle(QCoreApplication.translate("MainWindow", u"Analysis", None))
    # retranslateUi

