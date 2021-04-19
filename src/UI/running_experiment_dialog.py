# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'running_experiment_dialog.ui'
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
        Dialog.resize(346, 240)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_feedback_header = QLabel(Dialog)
        self.label_feedback_header.setObjectName(u"label_feedback_header")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_feedback_header.sizePolicy().hasHeightForWidth())
        self.label_feedback_header.setSizePolicy(sizePolicy)
        self.label_feedback_header.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_feedback_header)

        self.label_experiment_run_info = QLabel(Dialog)
        self.label_experiment_run_info.setObjectName(u"label_experiment_run_info")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_experiment_run_info.sizePolicy().hasHeightForWidth())
        self.label_experiment_run_info.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.label_experiment_run_info)

        self.label_experiment_run_time = QLabel(Dialog)
        self.label_experiment_run_time.setObjectName(u"label_experiment_run_time")
        sizePolicy1.setHeightForWidth(self.label_experiment_run_time.sizePolicy().hasHeightForWidth())
        self.label_experiment_run_time.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.label_experiment_run_time)

        self.experiment_progress_bar = QProgressBar(Dialog)
        self.experiment_progress_bar.setObjectName(u"experiment_progress_bar")
        self.experiment_progress_bar.setLayoutDirection(Qt.LeftToRight)
        self.experiment_progress_bar.setValue(0)
        self.experiment_progress_bar.setTextVisible(True)

        self.verticalLayout_2.addWidget(self.experiment_progress_bar)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_feedback_header.setText(QCoreApplication.translate("Dialog", u"Experiment is in progress", None))
        self.label_experiment_run_info.setText(QCoreApplication.translate("Dialog", u"Press 'Cancel' to stop and go back", None))
        self.label_experiment_run_time.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
    # retranslateUi

