from PySide2.QtWidgets import *
from UI.analysis_dialog import Ui_Dialog


class AnalysisDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


