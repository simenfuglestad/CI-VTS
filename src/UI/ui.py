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
        MainWindow.resize(1219, 759)
        self.actionExperiment_new = QAction(MainWindow)
        self.actionExperiment_new.setObjectName(u"actionExperiment_new")
        self.actionStimulus_Profile_new = QAction(MainWindow)
        self.actionStimulus_Profile_new.setObjectName(u"actionStimulus_Profile_new")
        self.actionExperiment_open = QAction(MainWindow)
        self.actionExperiment_open.setObjectName(u"actionExperiment_open")
        self.actionStimulus_Profile_open = QAction(MainWindow)
        self.actionStimulus_Profile_open.setObjectName(u"actionStimulus_Profile_open")
        self.actionSetup = QAction(MainWindow)
        self.actionSetup.setObjectName(u"actionSetup")
        self.actionGeneral = QAction(MainWindow)
        self.actionGeneral.setObjectName(u"actionGeneral")
        self.actionExperiment_save = QAction(MainWindow)
        self.actionExperiment_save.setObjectName(u"actionExperiment_save")
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
        self.actionUndo = QAction(MainWindow)
        self.actionUndo.setObjectName(u"actionUndo")
        self.actionRedo = QAction(MainWindow)
        self.actionRedo.setObjectName(u"actionRedo")
        self.actionStimulus_Profile_save = QAction(MainWindow)
        self.actionStimulus_Profile_save.setObjectName(u"actionStimulus_Profile_save")
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
        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_8.addWidget(self.label_10, 0, 0, 1, 1)

        self.list_stim_profiles = QListWidget(self.groupBox_3)
        self.list_stim_profiles.setObjectName(u"list_stim_profiles")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_stim_profiles.sizePolicy().hasHeightForWidth())
        self.list_stim_profiles.setSizePolicy(sizePolicy)

        self.gridLayout_8.addWidget(self.list_stim_profiles, 1, 0, 1, 2)


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
        self.list_exp_profiles = QListWidget(self.groupBox_2)
        self.list_exp_profiles.setObjectName(u"list_exp_profiles")
        sizePolicy.setHeightForWidth(self.list_exp_profiles.sizePolicy().hasHeightForWidth())
        self.list_exp_profiles.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.list_exp_profiles, 2, 0, 1, 2)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_2, 2, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.groupBox_main)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy2.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy2)
        self.gridLayout_9 = QGridLayout(self.groupBox_4)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout.addWidget(self.label_7)


        self.gridLayout_9.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.list_experiments_to_run = QListWidget(self.groupBox_4)
        self.list_experiments_to_run.setObjectName(u"list_experiments_to_run")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.list_experiments_to_run.sizePolicy().hasHeightForWidth())
        self.list_experiments_to_run.setSizePolicy(sizePolicy4)

        self.gridLayout_9.addWidget(self.list_experiments_to_run, 1, 0, 1, 2)

        self.pushButton_6 = QPushButton(self.groupBox_4)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_9.addWidget(self.pushButton_6, 3, 1, 1, 1)

        self.pushButton_5 = QPushButton(self.groupBox_4)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_9.addWidget(self.pushButton_5, 3, 0, 1, 1)


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
        self.label_13 = QLabel(self.groupBox_5)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_5.addWidget(self.label_13, 0, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.line_edit_duration = QLineEdit(self.groupBox_5)
        self.line_edit_duration.setObjectName(u"line_edit_duration")
        sizePolicy3.setHeightForWidth(self.line_edit_duration.sizePolicy().hasHeightForWidth())
        self.line_edit_duration.setSizePolicy(sizePolicy3)
        self.line_edit_duration.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.line_edit_duration)

        self.spin_duration_hour = QSpinBox(self.groupBox_5)
        self.spin_duration_hour.setObjectName(u"spin_duration_hour")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.spin_duration_hour.sizePolicy().hasHeightForWidth())
        self.spin_duration_hour.setSizePolicy(sizePolicy6)
        self.spin_duration_hour.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
        self.spin_duration_hour.setDisplayIntegerBase(10)

        self.horizontalLayout_4.addWidget(self.spin_duration_hour)

        self.spin_duration_min = QSpinBox(self.groupBox_5)
        self.spin_duration_min.setObjectName(u"spin_duration_min")
        sizePolicy6.setHeightForWidth(self.spin_duration_min.sizePolicy().hasHeightForWidth())
        self.spin_duration_min.setSizePolicy(sizePolicy6)
        self.spin_duration_min.setMaximum(59)

        self.horizontalLayout_4.addWidget(self.spin_duration_min)

        self.spin_duration_sec = QSpinBox(self.groupBox_5)
        self.spin_duration_sec.setObjectName(u"spin_duration_sec")
        sizePolicy6.setHeightForWidth(self.spin_duration_sec.sizePolicy().hasHeightForWidth())
        self.spin_duration_sec.setSizePolicy(sizePolicy6)
        self.spin_duration_sec.setMaximum(59)

        self.horizontalLayout_4.addWidget(self.spin_duration_sec)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)


        self.gridLayout_5.addLayout(self.horizontalLayout_4, 0, 1, 1, 1)

        self.checkbox_save_log = QCheckBox(self.groupBox_5)
        self.checkbox_save_log.setObjectName(u"checkbox_save_log")
        self.checkbox_save_log.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_5.addWidget(self.checkbox_save_log, 4, 0, 1, 1)

        self.checkbox_save_video = QCheckBox(self.groupBox_5)
        self.checkbox_save_video.setObjectName(u"checkbox_save_video")
        sizePolicy3.setHeightForWidth(self.checkbox_save_video.sizePolicy().hasHeightForWidth())
        self.checkbox_save_video.setSizePolicy(sizePolicy3)
        self.checkbox_save_video.setLayoutDirection(Qt.RightToLeft)
        self.checkbox_save_video.setChecked(True)

        self.gridLayout_5.addWidget(self.checkbox_save_video, 3, 0, 1, 1)

        self.checkbox_view_live = QCheckBox(self.groupBox_5)
        self.checkbox_view_live.setObjectName(u"checkbox_view_live")
        self.checkbox_view_live.setLayoutDirection(Qt.RightToLeft)
        self.checkbox_view_live.setCheckable(True)
        self.checkbox_view_live.setChecked(False)

        self.gridLayout_5.addWidget(self.checkbox_view_live, 5, 0, 1, 1)

        self.line_edit_video_path = QLineEdit(self.groupBox_5)
        self.line_edit_video_path.setObjectName(u"line_edit_video_path")
        self.line_edit_video_path.setReadOnly(True)

        self.gridLayout_5.addWidget(self.line_edit_video_path, 3, 1, 1, 1)

        self.btn_set_logs_path = QPushButton(self.groupBox_5)
        self.btn_set_logs_path.setObjectName(u"btn_set_logs_path")

        self.gridLayout_5.addWidget(self.btn_set_logs_path, 4, 2, 1, 1)

        self.btn_set_video_path = QPushButton(self.groupBox_5)
        self.btn_set_video_path.setObjectName(u"btn_set_video_path")

        self.gridLayout_5.addWidget(self.btn_set_video_path, 3, 2, 1, 1)

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

        self.line_edit_logs_path = QLineEdit(self.groupBox_5)
        self.line_edit_logs_path.setObjectName(u"line_edit_logs_path")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.line_edit_logs_path.sizePolicy().hasHeightForWidth())
        self.line_edit_logs_path.setSizePolicy(sizePolicy7)
        self.line_edit_logs_path.setReadOnly(True)

        self.gridLayout_5.addWidget(self.line_edit_logs_path, 4, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_17 = QLabel(self.groupBox_5)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_6.addWidget(self.label_17)

        self.label_stim_profile_name = QLabel(self.groupBox_5)
        self.label_stim_profile_name.setObjectName(u"label_stim_profile_name")
        sizePolicy5.setHeightForWidth(self.label_stim_profile_name.sizePolicy().hasHeightForWidth())
        self.label_stim_profile_name.setSizePolicy(sizePolicy5)

        self.horizontalLayout_6.addWidget(self.label_stim_profile_name)

        self.check_box_draw_mode = QCheckBox(self.groupBox_5)
        self.check_box_draw_mode.setObjectName(u"check_box_draw_mode")

        self.horizontalLayout_6.addWidget(self.check_box_draw_mode)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.stim_profile_plot = PlotWidget(self.groupBox_5)
        self.stim_profile_plot.setObjectName(u"stim_profile_plot")
        sizePolicy4.setHeightForWidth(self.stim_profile_plot.sizePolicy().hasHeightForWidth())
        self.stim_profile_plot.setSizePolicy(sizePolicy4)

        self.verticalLayout_4.addWidget(self.stim_profile_plot)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btn_add_stim = QPushButton(self.groupBox_5)
        self.btn_add_stim.setObjectName(u"btn_add_stim")
        sizePolicy7.setHeightForWidth(self.btn_add_stim.sizePolicy().hasHeightForWidth())
        self.btn_add_stim.setSizePolicy(sizePolicy7)

        self.horizontalLayout_8.addWidget(self.btn_add_stim)


        self.gridLayout_13.addLayout(self.horizontalLayout_8, 3, 0, 1, 1)

        self.checkbox_sync_led = QCheckBox(self.groupBox_5)
        self.checkbox_sync_led.setObjectName(u"checkbox_sync_led")
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.checkbox_sync_led.sizePolicy().hasHeightForWidth())
        self.checkbox_sync_led.setSizePolicy(sizePolicy8)

        self.gridLayout_13.addWidget(self.checkbox_sync_led, 1, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.spin_stim_led_end = QSpinBox(self.groupBox_5)
        self.spin_stim_led_end.setObjectName(u"spin_stim_led_end")
        sizePolicy3.setHeightForWidth(self.spin_stim_led_end.sizePolicy().hasHeightForWidth())
        self.spin_stim_led_end.setSizePolicy(sizePolicy3)
        self.spin_stim_led_end.setMaximum(100)

        self.horizontalLayout_10.addWidget(self.spin_stim_led_end)

        self.hslider_stim_led_end = QSlider(self.groupBox_5)
        self.hslider_stim_led_end.setObjectName(u"hslider_stim_led_end")
        sizePolicy7.setHeightForWidth(self.hslider_stim_led_end.sizePolicy().hasHeightForWidth())
        self.hslider_stim_led_end.setSizePolicy(sizePolicy7)
        self.hslider_stim_led_end.setMaximum(100)
        self.hslider_stim_led_end.setOrientation(Qt.Horizontal)

        self.horizontalLayout_10.addWidget(self.hslider_stim_led_end)


        self.gridLayout_13.addLayout(self.horizontalLayout_10, 2, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_13, 3, 2, 1, 1)

        self.line_2 = QFrame(self.groupBox_5)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_2, 2, 0, 1, 1)

        self.line_11 = QFrame(self.groupBox_5)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.VLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_11, 3, 1, 1, 1)

        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_16 = QLabel(self.groupBox_5)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_12.addWidget(self.label_16, 2, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.spin_stim_led_start = QSpinBox(self.groupBox_5)
        self.spin_stim_led_start.setObjectName(u"spin_stim_led_start")
        sizePolicy3.setHeightForWidth(self.spin_stim_led_start.sizePolicy().hasHeightForWidth())
        self.spin_stim_led_start.setSizePolicy(sizePolicy3)
        self.spin_stim_led_start.setMaximum(100)

        self.horizontalLayout_9.addWidget(self.spin_stim_led_start)

        self.hslider_stim_led_start = QSlider(self.groupBox_5)
        self.hslider_stim_led_start.setObjectName(u"hslider_stim_led_start")
        sizePolicy7.setHeightForWidth(self.hslider_stim_led_start.sizePolicy().hasHeightForWidth())
        self.hslider_stim_led_start.setSizePolicy(sizePolicy7)
        self.hslider_stim_led_start.setMaximum(100)
        self.hslider_stim_led_start.setOrientation(Qt.Horizontal)

        self.horizontalLayout_9.addWidget(self.hslider_stim_led_start)


        self.gridLayout_12.addLayout(self.horizontalLayout_9, 1, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(self.groupBox_5)
        self.label_5.setObjectName(u"label_5")
        sizePolicy9 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy9)

        self.horizontalLayout_7.addWidget(self.label_5)

        self.label_14 = QLabel(self.groupBox_5)
        self.label_14.setObjectName(u"label_14")
        sizePolicy10 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy10)

        self.horizontalLayout_7.addWidget(self.label_14)


        self.gridLayout_12.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_12, 3, 0, 1, 1)

        self.line = QFrame(self.groupBox_5)
        self.line.setObjectName(u"line")
        sizePolicy11 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy11)
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line, 1, 1, 1, 1)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.checkbox_end = QCheckBox(self.groupBox_5)
        self.checkbox_end.setObjectName(u"checkbox_end")
        sizePolicy7.setHeightForWidth(self.checkbox_end.sizePolicy().hasHeightForWidth())
        self.checkbox_end.setSizePolicy(sizePolicy7)
        self.checkbox_end.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_11.addWidget(self.checkbox_end, 2, 1, 1, 1)

        self.label_23 = QLabel(self.groupBox_5)
        self.label_23.setObjectName(u"label_23")
        sizePolicy7.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy7)

        self.gridLayout_11.addWidget(self.label_23, 3, 3, 1, 1)

        self.label_12 = QLabel(self.groupBox_5)
        self.label_12.setObjectName(u"label_12")
        sizePolicy7.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy7)

        self.gridLayout_11.addWidget(self.label_12, 1, 1, 1, 1)

        self.spin_end_hours = QSpinBox(self.groupBox_5)
        self.spin_end_hours.setObjectName(u"spin_end_hours")

        self.gridLayout_11.addWidget(self.spin_end_hours, 4, 1, 1, 1)

        self.spin_end_mins = QSpinBox(self.groupBox_5)
        self.spin_end_mins.setObjectName(u"spin_end_mins")

        self.gridLayout_11.addWidget(self.spin_end_mins, 4, 2, 1, 1)

        self.label_15 = QLabel(self.groupBox_5)
        self.label_15.setObjectName(u"label_15")
        sizePolicy7.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy7)

        self.gridLayout_11.addWidget(self.label_15, 3, 1, 1, 1)

        self.label_22 = QLabel(self.groupBox_5)
        self.label_22.setObjectName(u"label_22")
        sizePolicy7.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy7)

        self.gridLayout_11.addWidget(self.label_22, 3, 2, 1, 1)

        self.btn_reset_stim = QPushButton(self.groupBox_5)
        self.btn_reset_stim.setObjectName(u"btn_reset_stim")
        sizePolicy7.setHeightForWidth(self.btn_reset_stim.sizePolicy().hasHeightForWidth())
        self.btn_reset_stim.setSizePolicy(sizePolicy7)

        self.gridLayout_11.addWidget(self.btn_reset_stim, 1, 3, 1, 1)

        self.btn_clear_plot = QPushButton(self.groupBox_5)
        self.btn_clear_plot.setObjectName(u"btn_clear_plot")

        self.gridLayout_11.addWidget(self.btn_clear_plot, 0, 3, 1, 1)

        self.spin_end_secs = QSpinBox(self.groupBox_5)
        self.spin_end_secs.setObjectName(u"spin_end_secs")
        self.spin_end_secs.setMaximum(59)

        self.gridLayout_11.addWidget(self.spin_end_secs, 4, 3, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_11, 1, 2, 1, 1)

        self.line_3 = QFrame(self.groupBox_5)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_3, 2, 2, 1, 1)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_11 = QLabel(self.groupBox_5)
        self.label_11.setObjectName(u"label_11")
        sizePolicy10.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy10)

        self.gridLayout_10.addWidget(self.label_11, 3, 0, 1, 1)

        self.label_21 = QLabel(self.groupBox_5)
        self.label_21.setObjectName(u"label_21")
        sizePolicy10.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy10)
        self.label_21.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_21, 5, 0, 1, 1)

        self.checkbox_start = QCheckBox(self.groupBox_5)
        self.checkbox_start.setObjectName(u"checkbox_start")

        self.gridLayout_10.addWidget(self.checkbox_start, 4, 0, 1, 1)

        self.label_20 = QLabel(self.groupBox_5)
        self.label_20.setObjectName(u"label_20")
        sizePolicy10.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy10)
        self.label_20.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_20, 5, 2, 1, 1)

        self.spin_start_mins = QSpinBox(self.groupBox_5)
        self.spin_start_mins.setObjectName(u"spin_start_mins")
        self.spin_start_mins.setMaximum(59)

        self.gridLayout_10.addWidget(self.spin_start_mins, 6, 1, 1, 1)

        self.label_19 = QLabel(self.groupBox_5)
        self.label_19.setObjectName(u"label_19")
        sizePolicy10.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy10)
        self.label_19.setLayoutDirection(Qt.LeftToRight)
        self.label_19.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_19, 5, 1, 1, 1)

        self.spin_start_hours = QSpinBox(self.groupBox_5)
        self.spin_start_hours.setObjectName(u"spin_start_hours")

        self.gridLayout_10.addWidget(self.spin_start_hours, 6, 0, 1, 1)

        self.btn_center_graph = QPushButton(self.groupBox_5)
        self.btn_center_graph.setObjectName(u"btn_center_graph")

        self.gridLayout_10.addWidget(self.btn_center_graph, 2, 0, 1, 1)

        self.spin_start_secs = QSpinBox(self.groupBox_5)
        self.spin_start_secs.setObjectName(u"spin_start_secs")
        self.spin_start_secs.setMaximum(59)

        self.gridLayout_10.addWidget(self.spin_start_secs, 6, 2, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_10, 1, 0, 1, 1)


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

        self.spin_crowdsize = QSpinBox(self.tab_exp_settings)
        self.spin_crowdsize.setObjectName(u"spin_crowdsize")
        sizePolicy3.setHeightForWidth(self.spin_crowdsize.sizePolicy().hasHeightForWidth())
        self.spin_crowdsize.setSizePolicy(sizePolicy3)

        self.gridLayout_7.addWidget(self.spin_crowdsize, 6, 3, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_7.addItem(self.verticalSpacer_2, 3, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_7.addItem(self.verticalSpacer, 1, 2, 1, 1)

        self.label_6 = QLabel(self.tab_exp_settings)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_6, 4, 2, 1, 1)

        self.checkbox_drugs = QCheckBox(self.tab_exp_settings)
        self.checkbox_drugs.setObjectName(u"checkbox_drugs")
        self.checkbox_drugs.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_7.addWidget(self.checkbox_drugs, 4, 1, 1, 1)

        self.line_edit_drug_name = QLineEdit(self.tab_exp_settings)
        self.line_edit_drug_name.setObjectName(u"line_edit_drug_name")
        sizePolicy7.setHeightForWidth(self.line_edit_drug_name.sizePolicy().hasHeightForWidth())
        self.line_edit_drug_name.setSizePolicy(sizePolicy7)

        self.gridLayout_7.addWidget(self.line_edit_drug_name, 4, 3, 1, 1)

        self.line_edit_geno_type = QLineEdit(self.tab_exp_settings)
        self.line_edit_geno_type.setObjectName(u"line_edit_geno_type")
        sizePolicy7.setHeightForWidth(self.line_edit_geno_type.sizePolicy().hasHeightForWidth())
        self.line_edit_geno_type.setSizePolicy(sizePolicy7)

        self.gridLayout_7.addWidget(self.line_edit_geno_type, 2, 3, 1, 1)

        self.label_3 = QLabel(self.tab_exp_settings)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_3, 2, 2, 1, 1)

        self.checkbox_genetics = QCheckBox(self.tab_exp_settings)
        self.checkbox_genetics.setObjectName(u"checkbox_genetics")
        self.checkbox_genetics.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_7.addWidget(self.checkbox_genetics, 2, 1, 1, 1)

        self.combo_hatching_time = QComboBox(self.tab_exp_settings)
        self.combo_hatching_time.setObjectName(u"combo_hatching_time")
        sizePolicy12 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.combo_hatching_time.sizePolicy().hasHeightForWidth())
        self.combo_hatching_time.setSizePolicy(sizePolicy12)

        self.gridLayout_7.addWidget(self.combo_hatching_time, 0, 3, 1, 1)

        self.label = QLabel(self.tab_exp_settings)
        self.label.setObjectName(u"label")
        sizePolicy9.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy9)

        self.gridLayout_7.addWidget(self.label, 0, 2, 1, 1)

        self.checkbox_dechorionated = QCheckBox(self.tab_exp_settings)
        self.checkbox_dechorionated.setObjectName(u"checkbox_dechorionated")
        sizePolicy9.setHeightForWidth(self.checkbox_dechorionated.sizePolicy().hasHeightForWidth())
        self.checkbox_dechorionated.setSizePolicy(sizePolicy9)
        self.checkbox_dechorionated.setLayoutDirection(Qt.RightToLeft)
        self.checkbox_dechorionated.setAutoExclusive(False)

        self.gridLayout_7.addWidget(self.checkbox_dechorionated, 0, 1, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_7, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_exp_settings, "")

        self.gridLayout_3.addWidget(self.tabWidget, 2, 2, 3, 1)

        self.label_path_stim = QLabel(self.groupBox_main)
        self.label_path_stim.setObjectName(u"label_path_stim")

        self.gridLayout_3.addWidget(self.label_path_stim, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_main, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1219, 23))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
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
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuAnalysis.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.menuOpen.menuAction())
        self.menuFile.addAction(self.menuSave.menuAction())
        self.menuOpen.addSeparator()
        self.menuOpen.addSeparator()
        self.menuOpen.addAction(self.actionExperiment_open)
        self.menuOpen.addAction(self.actionStimulus_Profile_open)
        self.menuSave.addAction(self.actionExperiment_save)
        self.menuSave.addAction(self.actionStimulus_Profile_save)
        self.menuSettings.addAction(self.actionSetup)
        self.menuSettings.addAction(self.actionGeneral)
        self.menuRun.addAction(self.actionSelected_Experiments)
        self.menuRun.addAction(self.actionAll_Experiments_2)
        self.menuAnalysis.addAction(self.actionView)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionExperiment_new.setText(QCoreApplication.translate("MainWindow", u"Experiment", None))
        self.actionStimulus_Profile_new.setText(QCoreApplication.translate("MainWindow", u"Stimulus Profile", None))
        self.actionExperiment_open.setText(QCoreApplication.translate("MainWindow", u"Experiment", None))
        self.actionStimulus_Profile_open.setText(QCoreApplication.translate("MainWindow", u"Stimulus Profile", None))
        self.actionSetup.setText(QCoreApplication.translate("MainWindow", u"Setup", None))
        self.actionGeneral.setText(QCoreApplication.translate("MainWindow", u"General", None))
        self.actionExperiment_save.setText(QCoreApplication.translate("MainWindow", u"Experiment", None))
        self.actionSelected_Experiment.setText(QCoreApplication.translate("MainWindow", u"Selected Experiment", None))
        self.actionAll_Experiments.setText(QCoreApplication.translate("MainWindow", u"All Experiments", None))
        self.actionSelected_Experiments.setText(QCoreApplication.translate("MainWindow", u"Selected Experiments", None))
        self.actionAll_Experiments_2.setText(QCoreApplication.translate("MainWindow", u"All Experiments", None))
        self.actionView.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.actionUndo.setText(QCoreApplication.translate("MainWindow", u"Undo (Ctrl + z)", None))
        self.actionRedo.setText(QCoreApplication.translate("MainWindow", u"Redo (Ctrl + y)", None))
        self.actionStimulus_Profile_save.setText(QCoreApplication.translate("MainWindow", u"Stimulus Profile", None))
        self.groupBox_main.setTitle("")
        self.groupBox_3.setTitle("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Stimulus Profiles", None))
        self.label_status.setText(QCoreApplication.translate("MainWindow", u"Camera Status:", None))
        self.label_status_value.setText(QCoreApplication.translate("MainWindow", u"STATUSTEXT", None))
        self.btn_run.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.label_working_dir.setText(QCoreApplication.translate("MainWindow", u"C:/PATH_TO_EXP_FILES", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Current Temp in Chamber: ", None))
        self.label_temp_val.setText(QCoreApplication.translate("MainWindow", u"TEMP_VAL", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.groupBox_2.setTitle("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Experiments", None))
        self.groupBox_4.setTitle("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Experiements to Run", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.groupBox_5.setTitle("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Full Duration", None))
        self.line_edit_duration.setText(QCoreApplication.translate("MainWindow", u"HH:MM:SS", None))
        self.checkbox_save_log.setText(QCoreApplication.translate("MainWindow", u"Save log", None))
        self.checkbox_save_video.setText(QCoreApplication.translate("MainWindow", u"Save Video", None))
        self.checkbox_view_live.setText(QCoreApplication.translate("MainWindow", u"View Live", None))
        self.line_edit_video_path.setText(QCoreApplication.translate("MainWindow", u"\"Path to video\"", None))
        self.btn_set_logs_path.setText(QCoreApplication.translate("MainWindow", u"Set Logs Path", None))
        self.btn_set_video_path.setText(QCoreApplication.translate("MainWindow", u"Set Video Path", None))
        self.checkbox_live_ir.setText(QCoreApplication.translate("MainWindow", u"Infrared", None))
        self.line_edit_logs_path.setText(QCoreApplication.translate("MainWindow", u"\"Path to logs\"", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Stimulus profile:", None))
        self.label_stim_profile_name.setText(QCoreApplication.translate("MainWindow", u"PROFILE NAME", None))
        self.check_box_draw_mode.setText(QCoreApplication.translate("MainWindow", u"Draw Mode", None))
        self.btn_add_stim.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.checkbox_sync_led.setText(QCoreApplication.translate("MainWindow", u"Same as Start", None))
        self.label_16.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"LED Intensity", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.checkbox_end.setText(QCoreApplication.translate("MainWindow", u"End", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Seconds", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"To", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Hours", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Minutes", None))
        self.btn_reset_stim.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.btn_clear_plot.setText(QCoreApplication.translate("MainWindow", u"Clear Plot", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"From", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Hours", None))
        self.checkbox_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Seconds", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Minutes", None))
        self.btn_center_graph.setText(QCoreApplication.translate("MainWindow", u"Center Graph", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_exp_profile), QCoreApplication.translate("MainWindow", u"EXP_NAME", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Crowdsize", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Drug Name", None))
        self.checkbox_drugs.setText(QCoreApplication.translate("MainWindow", u"Drugs", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Genotype", None))
        self.checkbox_genetics.setText(QCoreApplication.translate("MainWindow", u"Genetics", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Hatching Time", None))
        self.checkbox_dechorionated.setText(QCoreApplication.translate("MainWindow", u"Dechorionated", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_exp_settings), QCoreApplication.translate("MainWindow", u"Additional Settings", None))
        self.label_path_stim.setText(QCoreApplication.translate("MainWindow", u"C:/PATH_TO_STIM_FILES", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuOpen.setTitle(QCoreApplication.translate("MainWindow", u"Open", None))
        self.menuSave.setTitle(QCoreApplication.translate("MainWindow", u"Save", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuRun.setTitle(QCoreApplication.translate("MainWindow", u"Run", None))
        self.menuAnalysis.setTitle(QCoreApplication.translate("MainWindow", u"Analysis", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
    # retranslateUi

