# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'analysis_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1046, 665)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.list_completed_experiments = QtWidgets.QListWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_completed_experiments.sizePolicy().hasHeightForWidth())
        self.list_completed_experiments.setSizePolicy(sizePolicy)
        self.list_completed_experiments.setObjectName("list_completed_experiments")
        self.verticalLayout.addWidget(self.list_completed_experiments)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.list_selected_experiments = QtWidgets.QListWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_selected_experiments.sizePolicy().hasHeightForWidth())
        self.list_selected_experiments.setSizePolicy(sizePolicy)
        self.list_selected_experiments.setObjectName("list_selected_experiments")
        self.verticalLayout.addWidget(self.list_selected_experiments)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.combo_playback_speed = QtWidgets.QComboBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_playback_speed.sizePolicy().hasHeightForWidth())
        self.combo_playback_speed.setSizePolicy(sizePolicy)
        self.combo_playback_speed.setObjectName("combo_playback_speed")
        self.combo_playback_speed.addItem("")
        self.combo_playback_speed.addItem("")
        self.combo_playback_speed.addItem("")
        self.combo_playback_speed.addItem("")
        self.combo_playback_speed.addItem("")
        self.combo_playback_speed.addItem("")
        self.combo_playback_speed.addItem("")
        self.horizontalLayout_3.addWidget(self.combo_playback_speed)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.dspinbox_playback_speed = QtWidgets.QDoubleSpinBox(Dialog)
        self.dspinbox_playback_speed.setObjectName("dspinbox_playback_speed")
        self.horizontalLayout_3.addWidget(self.dspinbox_playback_speed)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.spinbox_frame_skip = QtWidgets.QSpinBox(Dialog)
        self.spinbox_frame_skip.setObjectName("spinbox_frame_skip")
        self.horizontalLayout_3.addWidget(self.spinbox_frame_skip)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_play_vid = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_play_vid.sizePolicy().hasHeightForWidth())
        self.btn_play_vid.setSizePolicy(sizePolicy)
        self.btn_play_vid.setObjectName("btn_play_vid")
        self.horizontalLayout_2.addWidget(self.btn_play_vid)
        self.btn_pause_vid = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_pause_vid.sizePolicy().hasHeightForWidth())
        self.btn_pause_vid.setSizePolicy(sizePolicy)
        self.btn_pause_vid.setObjectName("btn_pause_vid")
        self.horizontalLayout_2.addWidget(self.btn_pause_vid)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_vid_time = QtWidgets.QLabel(Dialog)
        self.label_vid_time.setObjectName("label_vid_time")
        self.horizontalLayout_4.addWidget(self.label_vid_time)
        self.horizontalSlider = QtWidgets.QSlider(Dialog)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_4.addWidget(self.horizontalSlider)
        self.btn_dec_frame_skip = QtWidgets.QPushButton(Dialog)
        self.btn_dec_frame_skip.setObjectName("btn_dec_frame_skip")
        self.horizontalLayout_4.addWidget(self.btn_dec_frame_skip)
        self.btn_inc_frame_skip = QtWidgets.QPushButton(Dialog)
        self.btn_inc_frame_skip.setObjectName("btn_inc_frame_skip")
        self.horizontalLayout_4.addWidget(self.btn_inc_frame_skip)
        self.btn_save_frame = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_save_frame.sizePolicy().hasHeightForWidth())
        self.btn_save_frame.setSizePolicy(sizePolicy)
        self.btn_save_frame.setObjectName("btn_save_frame")
        self.horizontalLayout_4.addWidget(self.btn_save_frame)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 1, 1, 1)
        self.imgview_video = ImageView(Dialog)
        self.imgview_video.setObjectName("imgview_video")
        self.gridLayout.addWidget(self.imgview_video, 1, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 8, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.combo_playback_speed.setCurrentIndex(3)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Completed Experiments"))
        self.label_3.setText(_translate("Dialog", "Selected Experiment Information"))
        self.pushButton.setText(_translate("Dialog", "ShowVideo"))
        self.pushButton_2.setText(_translate("Dialog", "Refresh"))
        self.label_4.setText(_translate("Dialog", "Playback Speed"))
        self.combo_playback_speed.setItemText(0, _translate("Dialog", "0.10x"))
        self.combo_playback_speed.setItemText(1, _translate("Dialog", "0.25x"))
        self.combo_playback_speed.setItemText(2, _translate("Dialog", "0.5x"))
        self.combo_playback_speed.setItemText(3, _translate("Dialog", "1x"))
        self.combo_playback_speed.setItemText(4, _translate("Dialog", "1.5x"))
        self.combo_playback_speed.setItemText(5, _translate("Dialog", "2x"))
        self.combo_playback_speed.setItemText(6, _translate("Dialog", "5x"))
        self.label_7.setText(_translate("Dialog", "Frames to Skip"))
        self.btn_play_vid.setText(_translate("Dialog", "Play"))
        self.btn_pause_vid.setText(_translate("Dialog", "Pause"))
        self.label_2.setText(_translate("Dialog", "Video"))
        self.label_vid_time.setText(_translate("Dialog", "00:00:00"))
        self.btn_dec_frame_skip.setText(_translate("Dialog", "<"))
        self.btn_inc_frame_skip.setText(_translate("Dialog", ">"))
        self.btn_save_frame.setText(_translate("Dialog", "Save Frame"))
from pyqtgraph import ImageView


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
