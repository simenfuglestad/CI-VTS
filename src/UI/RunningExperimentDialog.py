from UI.running_experiment_dialog import Ui_Dialog
from PySide6.QtWidgets import QDialog, QDialogButtonBox
from PySide6.QtCore import Signal, QTimer


class RunningExperimentDialog(QDialog, Ui_Dialog):
    signal_user_aborted_experiment = Signal(bytes)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.progress_inc = -1
        self.counter = 0
        self.time_counter = 0
        self.time_run = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_close_countdown)
        self.timer.setInterval(1000)
        self.countdown = 10

    def closeEvent(self, event):
        self.reset()

    def update_progress(self):
        self.counter = self.counter + 1
        self.time_counter = self.time_counter + 1

        if self.counter / 100 >= self.progress_inc != -1:
            self.experiment_progress_bar.setValue(self.experiment_progress_bar.value() + 1)
            self.counter = 0

        if self.time_counter % 100 == 0:
            self.time_run = self.time_run + 1
            self.set_run_time(self.time_run)

        if self.experiment_progress_bar.value() == 100:
            self.label_feedback_header.setText("Done!")

    def set_progress_completed(self):
        self.label_feedback_header.setText("Done!")
        # self.label_experiment_run_info.setText("This window will close in " + str(self.countdown) + " seconds")
        self.label_experiment_run_info.setText("This window can be closed safely")
        self.experiment_progress_bar.setValue(100)
        self.set_run_time(int(self.progress_inc * 100))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        # self.timer.start()

    def update_close_countdown(self):
        if self.countdown > 1:
            self.countdown = self.countdown - 1
            self.label_experiment_run_info.setText("This window will close in " + str(self.countdown) + " second" + ("s" if self.countdown != 1 else ""))
        else:
            self.timer.stop()
            self.close()

    def set_progress_increment(self, experiment_duration):
        self.progress_inc = experiment_duration/100

    def reset(self):
        self.timer.stop()
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel)
        self.experiment_progress_bar.setValue(0)
        self.set_run_time(0)
        self.progress_inc = -1
        self.label_feedback_header.setText("Experiment is in progress")
        self.label_experiment_run_info.setText("Press 'Cancel' to abort and go back")
        self.time_counter = 0
        self.time_run = 0
        self.countdown = 10

    def set_run_time(self, time):
        h = time // 60 // 60 % 60
        m = time // 60 % 60
        s = time % 60

        h_str = str(h) if h >= 10 else "0" + str(h)
        m_str = str(m) if m >= 10 else "0" + str(m)
        s_str = str(s) if s >= 10 else "0" + str(s)
        self.label_experiment_run_time.setText(h_str + ":" + m_str + ":" + s_str)