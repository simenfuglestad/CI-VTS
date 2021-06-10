import sys
from PySide6.QtWidgets import *
from UI.MainWindow import MainWindow
from serial_interface.serial_interface import *
from arduino.arduino import Arduino
from UI.AnalysisDialog import AnalysisDialog
from UI.SettingsDialog import SettingsDialog
from UI.RunningExperimentDialog import RunningExperimentDialog
from camera.camera import *


class Main(QApplication):
    """
    Entry point of application, instantiates major application-wide instances and properties.
    ...
    Attributes:
    ----------
    video_path : str
        path to recorded videos on the system, relative by default
    stimulus_path : str
       path to stimulus profiles on the system, relative by default
    logs_path : str
        path to recorded videos on the system, relative by default
        NOTE: currently not in use
    """
    video_path = "experiment/videos/"
    stimulus_path = "stimulus/stimulus_profiles/"
    logs_path = "experiment/logs/"
    experiment_profiles_path = "experiment/experiment_profiles/"

    def __init__(self):
        """
        Initialize and set up the main application by instantiating all major components and passing them where needed.

        """
        super().__init__()
        # init serial_interface interface
        self.serial_interface = SerialInterface()

        # Init Camera
        self.camera = Camera(video_path=self.video_path)
        self.camera.start()

        # init UI
        self.settings_dialog = SettingsDialog(
            serial_interface=self.serial_interface,
            camera=self.camera)

        self.analysis_dialog = AnalysisDialog(video_path=self.video_path)

        self.running_experiment_dialog = RunningExperimentDialog()

        self.main_window = MainWindow(
            settings_dialog=self.settings_dialog,
            analysis_dialog=self.analysis_dialog,
            running_experiment_dialog=self.running_experiment_dialog,
            serial_interface=self.serial_interface,
            video_path=self.video_path,
            logs_path=self.logs_path,
            experiments_path=self.experiment_profiles_path,
            stimulus_path=self.stimulus_path,
            camera=self.camera,
            size=self.primaryScreen().size())

        self.main_window.setWindowTitle("CI-VTS")
        self.main_window.show()


if __name__ == '__main__':
    app = Main()
    sys.exit(app.exec_())
