# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'analysis_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.0.1
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
        Dialog.resize(961, 665)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_video_view = QLabel(Dialog)
        self.label_video_view.setObjectName(u"label_video_view")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_video_view.sizePolicy().hasHeightForWidth())
        self.label_video_view.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_video_view, 1, 1, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_play_vid = QPushButton(Dialog)
        self.btn_play_vid.setObjectName(u"btn_play_vid")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_play_vid.sizePolicy().hasHeightForWidth())
        self.btn_play_vid.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.btn_play_vid)

        self.btn_pause_vid = QPushButton(Dialog)
        self.btn_pause_vid.setObjectName(u"btn_pause_vid")
        sizePolicy1.setHeightForWidth(self.btn_pause_vid.sizePolicy().hasHeightForWidth())
        self.btn_pause_vid.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.btn_pause_vid)

        self.btn_stop_vid = QPushButton(Dialog)
        self.btn_stop_vid.setObjectName(u"btn_stop_vid")

        self.horizontalLayout_2.addWidget(self.btn_stop_vid)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 1, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_set_video_folder = QPushButton(Dialog)
        self.btn_set_video_folder.setObjectName(u"btn_set_video_folder")

        self.horizontalLayout.addWidget(self.btn_set_video_folder)

        self.btn_refresh_video_list = QPushButton(Dialog)
        self.btn_refresh_video_list.setObjectName(u"btn_refresh_video_list")

        self.horizontalLayout.addWidget(self.btn_refresh_video_list)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.list_recordings = QListWidget(Dialog)
        self.list_recordings.setObjectName(u"list_recordings")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.list_recordings.sizePolicy().hasHeightForWidth())
        self.list_recordings.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.list_recordings)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)

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
        sizePolicy3.setHeightForWidth(self.combo_playback_speed.sizePolicy().hasHeightForWidth())
        self.combo_playback_speed.setSizePolicy(sizePolicy3)

        self.horizontalLayout_3.addWidget(self.combo_playback_speed)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.combo_frame_skip = QComboBox(Dialog)
        self.combo_frame_skip.addItem("")
        self.combo_frame_skip.addItem("")
        self.combo_frame_skip.addItem("")
        self.combo_frame_skip.addItem("")
        self.combo_frame_skip.addItem("")
        self.combo_frame_skip.setObjectName(u"combo_frame_skip")

        self.horizontalLayout_3.addWidget(self.combo_frame_skip)

        self.btn_frame_skip_back = QPushButton(Dialog)
        self.btn_frame_skip_back.setObjectName(u"btn_frame_skip_back")

        self.horizontalLayout_3.addWidget(self.btn_frame_skip_back)

        self.btn_frame_skip_fwd = QPushButton(Dialog)
        self.btn_frame_skip_fwd.setObjectName(u"btn_frame_skip_fwd")

        self.horizontalLayout_3.addWidget(self.btn_frame_skip_fwd)


        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 1, 1, 1)

        self.label_video_fps = QLabel(Dialog)
        self.label_video_fps.setObjectName(u"label_video_fps")

        self.gridLayout.addWidget(self.label_video_fps, 3, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_vid_time = QLabel(Dialog)
        self.label_vid_time.setObjectName(u"label_vid_time")

        self.horizontalLayout_4.addWidget(self.label_vid_time)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.label_vid_total_time = QLabel(Dialog)
        self.label_vid_total_time.setObjectName(u"label_vid_total_time")

        self.horizontalLayout_4.addWidget(self.label_vid_total_time)

        self.hslider_video_playback = QSlider(Dialog)
        self.hslider_video_playback.setObjectName(u"hslider_video_playback")
        self.hslider_video_playback.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.hslider_video_playback)

        self.btn_save_frame = QPushButton(Dialog)
        self.btn_save_frame.setObjectName(u"btn_save_frame")
        sizePolicy1.setHeightForWidth(self.btn_save_frame.sizePolicy().hasHeightForWidth())
        self.btn_save_frame.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.btn_save_frame)


        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 8, 1, 1, 1)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 8, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        self.combo_playback_speed.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_video_view.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"Recordings", None))
        self.label_8.setText("")
        self.btn_play_vid.setText(QCoreApplication.translate("Dialog", u"Play", None))
        self.btn_pause_vid.setText(QCoreApplication.translate("Dialog", u"Pause", None))
        self.btn_stop_vid.setText(QCoreApplication.translate("Dialog", u"Stop", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Video", None))
        self.btn_set_video_folder.setText(QCoreApplication.translate("Dialog", u"Set Video Folder", None))
        self.btn_refresh_video_list.setText(QCoreApplication.translate("Dialog", u"Refresh", None))
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
        self.combo_frame_skip.setItemText(0, QCoreApplication.translate("Dialog", u"1", None))
        self.combo_frame_skip.setItemText(1, QCoreApplication.translate("Dialog", u"5", None))
        self.combo_frame_skip.setItemText(2, QCoreApplication.translate("Dialog", u"10", None))
        self.combo_frame_skip.setItemText(3, QCoreApplication.translate("Dialog", u"30", None))
        self.combo_frame_skip.setItemText(4, QCoreApplication.translate("Dialog", u"60", None))

        self.btn_frame_skip_back.setText(QCoreApplication.translate("Dialog", u"<", None))
        self.btn_frame_skip_fwd.setText(QCoreApplication.translate("Dialog", u">", None))
        self.label_video_fps.setText(QCoreApplication.translate("Dialog", u"Selected Video FPS:", None))
        self.label_vid_time.setText(QCoreApplication.translate("Dialog", u"00:00:00", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"/", None))
        self.label_vid_total_time.setText(QCoreApplication.translate("Dialog", u"00:00:00", None))
        self.btn_save_frame.setText(QCoreApplication.translate("Dialog", u"Save Frame", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Run Analysis", None))
    # retranslateUi

