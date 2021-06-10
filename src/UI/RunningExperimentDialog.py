from UI.running_experiment_dialog import Ui_Dialog
from PySide6.QtWidgets import QDialog, QDialogButtonBox
from PySide6.QtCore import Signal, QTimer


class RunningExperimentDialog(QDialog, Ui_Dialog):
    """
    User interface component to give users feedback on experiment progression.

    Attributes
    ----------
    signal_user_aborted_experiment: Signal
        Qt signal object, emitted when a user willingly aborts an experiment
    """

    signal_user_aborted_experiment = Signal(bytes)

    def __init__(self):
        """
        Instantiate all values needed for calulating and tracking progress, but keep window hidden.
        """
        super().__init__()
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
        """
        Event fired when closing the window
        :param event: QCloseEvent
        :return: None
        """
        self.reset()

    def update_progress(self):
        """
        Updates progress bar and timer according to time progression in running experiment
        :return: None
        """
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
        """
        Sets progres bar to full and time duration to max
        :return: None
        """
        self.label_feedback_header.setText("Done!")
        self.label_experiment_run_info.setText("This window can be closed safely")
        self.experiment_progress_bar.setValue(100)
        self.set_run_time(int(self.progress_inc * 100))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)

    def update_close_countdown(self):
        """
        Event fired whenever QTimer emits timing signal, updates the progress bar and time label
        :return:
        """
        if self.countdown > 1:
            self.countdown = self.countdown - 1
            self.label_experiment_run_info.setText("This window will close in " + str(self.countdown) + " second" + ("s" if self.countdown != 1 else ""))
        else:
            self.timer.stop()
            self.close()

    def set_progress_increment(self, experiment_duration):
        """
        Compute increments to be used with progress bar
        :param experiment_duration: int number of seconds the experiment lasts
        :return: None
        """
        self.progress_inc = experiment_duration/100

    def reset(self):
        """
        Stop timer and set all values to the same as in constructor
        :return:
        """
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
        """
        Update the label showing the total run time of the experiment
        :param time:
        :return:
        """
        h = time // 60 // 60 % 60
        m = time // 60 % 60
        s = time % 60

        h_str = str(h) if h >= 10 else "0" + str(h)
        m_str = str(m) if m >= 10 else "0" + str(m)
        s_str = str(s) if s >= 10 else "0" + str(s)
        self.label_experiment_run_time.setText(h_str + ":" + m_str + ":" + s_str)