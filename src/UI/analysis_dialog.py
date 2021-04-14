# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'analysis_dialogGOzHFf.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pyqtgraph import ImageView


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1046, 665)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.list_completed_experiments = QListWidget(Dialog)
        self.list_completed_experiments.setObjectName(u"list_completed_experiments")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_completed_experiments.sizePolicy().hasHeightForWidth())
        self.list_completed_experiments.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.list_completed_experiments)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.list_selected_experiments = QListWidget(Dialog)
        self.list_selected_experiments.setObjectName(u"list_selected_experiments")
        sizePolicy.setHeightForWidth(self.list_selected_experiments.sizePolicy().hasHeightForWidth())
        self.list_selected_experiments.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.list_selected_experiments)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.combo_playback_speed = QComboBox(Dialog)
        self.combo_playback_speed.addItem("")
        self.combo_playback_speed.addItem("")
        self.combo_playback_speed.addItem("")
        self.combo_playback_speed.addItem("")
        self.combo_playback_speed.addItem("")
        self.combo_playback_speed.addItem("")
        self.combo_playback_speed.addItem("")
        self.combo_playback_speed.setObjectName(u"combo_playback_speed")
        sizePolicy1.setHeightForWidth(self.combo_playback_speed.sizePolicy().hasHeightForWidth())
        self.combo_playback_speed.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.combo_playback_speed)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.dspinbox_playback_speed = QDoubleSpinBox(Dialog)
        self.dspinbox_playback_speed.setObjectName(u"dspinbox_playback_speed")

        self.horizontalLayout_3.addWidget(self.dspinbox_playback_speed)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.spinbox_frame_skip = QSpinBox(Dialog)
        self.spinbox_frame_skip.setObjectName(u"spinbox_frame_skip")

        self.horizontalLayout_3.addWidget(self.spinbox_frame_skip)


        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_play_vid = QPushButton(Dialog)
        self.btn_play_vid.setObjectName(u"btn_play_vid")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_play_vid.sizePolicy().hasHeightForWidth())
        self.btn_play_vid.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.btn_play_vid)

        self.btn_pause_vid = QPushButton(Dialog)
        self.btn_pause_vid.setObjectName(u"btn_pause_vid")
        sizePolicy2.setHeightForWidth(self.btn_pause_vid.sizePolicy().hasHeightForWidth())
        self.btn_pause_vid.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.btn_pause_vid)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 1, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_vid_time = QLabel(Dialog)
        self.label_vid_time.setObjectName(u"label_vid_time")

        self.horizontalLayout_4.addWidget(self.label_vid_time)

        self.horizontalSlider = QSlider(Dialog)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.horizontalSlider)

        self.btn_dec_frame_skip = QPushButton(Dialog)
        self.btn_dec_frame_skip.setObjectName(u"btn_dec_frame_skip")

        self.horizontalLayout_4.addWidget(self.btn_dec_frame_skip)

        self.btn_inc_frame_skip = QPushButton(Dialog)
        self.btn_inc_frame_skip.setObjectName(u"btn_inc_frame_skip")

        self.horizontalLayout_4.addWidget(self.btn_inc_frame_skip)

        self.btn_save_frame = QPushButton(Dialog)
        self.btn_save_frame.setObjectName(u"btn_save_frame")
        sizePolicy2.setHeightForWidth(self.btn_save_frame.sizePolicy().hasHeightForWidth())
        self.btn_save_frame.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.btn_save_frame)


        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 1, 1, 1)

        self.imgview_video = ImageView(Dialog)
        self.imgview_video.setObjectName(u"imgview_video")

        self.gridLayout.addWidget(self.imgview_video, 1, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 8, 1, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        self.combo_playback_speed.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Completed Experiments", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Selected Experiment Information", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"ShowVideo", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Refresh", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Playback Speed", None))
        self.combo_playback_speed.setItemText(0, QCoreApplication.translate("Dialog", u"0.10x", None))
        self.combo_playback_speed.setItemText(1, QCoreApplication.translate("Dialog", u"0.25x", None))
        self.combo_playback_speed.setItemText(2, QCoreApplication.translate("Dialog", u"0.5x", None))
        self.combo_playback_speed.setItemText(3, QCoreApplication.translate("Dialog", u"1x", None))
        self.combo_playback_speed.setItemText(4, QCoreApplication.translate("Dialog", u"1.5x", None))
        self.combo_playback_speed.setItemText(5, QCoreApplication.translate("Dialog", u"2x", None))
        self.combo_playback_speed.setItemText(6, QCoreApplication.translate("Dialog", u"5x", None))

        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Frames to Skip", None))
        self.btn_play_vid.setText(QCoreApplication.translate("Dialog", u"Play", None))
        self.btn_pause_vid.setText(QCoreApplication.translate("Dialog", u"Pause", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Video", None))
        self.label_vid_time.setText(QCoreApplication.translate("Dialog", u"00:00:00", None))
        self.btn_dec_frame_skip.setText(QCoreApplication.translate("Dialog", u"<", None))
        self.btn_inc_frame_skip.setText(QCoreApplication.translate("Dialog", u">", None))
        self.btn_save_frame.setText(QCoreApplication.translate("Dialog", u"Save Frame", None))
    # retranslateUi

