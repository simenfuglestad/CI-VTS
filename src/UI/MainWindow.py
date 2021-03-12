from PySide6.QtCore import *
from PySide6.QtWidgets import *
from UI.ui import Ui_MainWindow
from UI.AnalysisDialog import AnalysisDialog
from UI.SettingsDialog import SettingsDialog


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, settings_dialog, analysis_dialog, size, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        QObject.connect(self.actionSetup, SIGNAL("triggered()"), settings_dialog.show)

        QObject.connect(self.actionView, SIGNAL("triggered()"), analysis_dialog.show)

        #use this when available!
        # self.btn_run.clicked.connect(self.test)

        self.resize(size.width(), size.height())

    def test(self):
        print("ifhsg")