from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from UI.analysis_dialog import Ui_Dialog
import os
import cv2
import numpy
import time
from experiment.VideoHandler import VideoHandler


class AnalysisDialog(QDialog, Ui_Dialog):
    """
    User interface component that allows video playback and interaction with tracking software.

    """
    def __init__(self, video_path):
        """
        Sets up a VideoHandler to deal with video playback and binds functionality to UI components

        :param video_path: system path where recorded videos are loaded from
        """

        super().__init__()
        self.setupUi(self)
        self.video_path = video_path

        # Need this first to connect playback functionality to UI components
        self.video_handler = VideoHandler(video_path, 800, 600)

        self.list_recordings.itemClicked.connect(lambda x: self.show_video(x))

        self.btn_play_vid.clicked.connect(self.play_clicked)
        self.btn_pause_vid.clicked.connect(self.pause_clicked)
        self.btn_stop_vid.clicked.connect(self.stop_clicked)
        self.combo_playback_speed.currentTextChanged.connect(lambda x: self.selected_playback_speed(x))

        self.btn_frame_skip_fwd.clicked.connect(self.skip_fwd_clicked)
        self.btn_frame_skip_back.clicked.connect(self.skip_back_clicked)

        self.video_handler.signal_read_first_frame.connect(lambda x: self.update_video_view(x))
        self.video_handler.signal_read_frame.connect(lambda x: self.update_video_view(x))

        self.video_handler.signal_total_run_time.connect(lambda x: self.format_label_total_run_time(x))
        self.video_handler.signal_current_play_time.connect(lambda x: self.format_label_current_run_time(x))
        self.video_handler.signal_current_play_time.connect(lambda x: self.update_slider_position(x))
        self.video_handler.signal_set_fps_in_dialog.connect(lambda x: self.set_fps_label(x))

        self.prev_playback_slider_index = 0
        self.hslider_video_playback.sliderMoved.connect(self.playback_slider_moved)
        self.hslider_video_playback.sliderReleased.connect(self.playback_slider_released)
        self.hslider_video_playback.sliderPressed.connect(self.playback_slider_pressed)

        self.btn_set_video_folder.clicked.connect(self.set_video_folder_clicked)
        self.btn_refresh_video_list.clicked.connect(self.populate_video_list)

        self.btn_save_frame.clicked.connect(self.save_frame_clicked)

        self.shortcut_playpause = QShortcut(QKeySequence(Qt.Key_Space), self)
        self.shortcut_playpause.activated.connect(self.keypress_play_pause)

        self.checkbox_analyze.toggled.connect(lambda x: self.analyze_checked(x))

    def analyze_checked(self, analyze):
        """
        Run when checkbox 'analyze' is toggled, sets flag indicating if analysis should be performed or not.
        :param analyze: boolean indicating toggle value, true means toggled while false means un-toggled
        :return: None
        """
        self.video_handler.set_analyze(analyze)

    def keypress_play_pause(self):
        """
        Pauses or plays video when user presses appropriate key (defined in class constructor)
        :return: None
        """
        if self.video_handler.isRunning():
            self.video_handler.pause_video()
        else:
            self.video_handler.play_video()

    def set_fps_label(self, fps_val):
        """
        Sets a label providing user feedback of the current fps
        :param fps_val: Non-negative integer indicating FPS
        :return: None
        """
        self.label_video_fps.setText("Selected Video FPS: " + str(fps_val))

    def update_slider_position(self, pos):
        """
        Update the position of the playback slider
        :param pos: Dictionary object formatted as {'label_val' : int, 'slider_val': int}
        :return: None
        """
        self.hslider_video_playback.setValue(pos["slider_val"])

    def update_video_view(self, pix_map):
        """
        Displays a pixel map of a frame in the video playback
        :param pix_map: QPixMap object containing pixel data of a frame
        :return: None
        """
        self.label_video_view.setPixmap(pix_map)

    def show_video(self, video_item):
        """
        Brings up a selected video file in the playback display and resets playback UI
        :param video_item: QListWidgetItem object with a text property that matches the name of the video
        :return: None
        """
        self.video_handler.set_video(video_item.text())
        self.video_handler.stop_video()
        self.hslider_video_playback.setMaximum(self.video_handler.nr_of_frames)
        self.hslider_video_playback.setValue(0)

    def play_clicked(self):
        """
        Play button clicked by user, start video playback
        :return: None
        """
        self.video_handler.play_video()

    def pause_clicked(self):
        """
        Pause button clicked by user, pauses video playback
        :return: None
        """
        self.video_handler.pause_video()

    def stop_clicked(self):
        """
        Stop button clicked by user, stops video playback and resets slider
        :return: None
        """
        self.video_handler.stop_video()
        self.hslider_video_playback.setValue(0)

    def skip_fwd_clicked(self):
        """
        Right arrow button clicked, skips ahead a number of frames indicated by the combobox
        :return: None
        """
        self.video_handler.skip_frame_forward(clicked=True, frames_to_skip=int(self.combo_frame_skip.currentText()))

    def skip_back_clicked(self):
        """
        Left arrow button clicked, goes back a number of frames indicated by the combobox
        :return:
        """
        self.video_handler.skip_frame_backwards(clicked=True, frames_to_skip=int(self.combo_frame_skip.currentText()))

    def selected_playback_speed(self, speed):
        """
        User selects playback speed, multiples regular playback speed by the amount selected
        :param speed: playback speed multiplier,
        :return: String that can be parsed to get multiplier value
        """
        multiplier = float(speed[0:-1])
        self.video_handler.set_playback_speed(multiplier)

    def save_frame_clicked(self):
        """
        User clicks save frame button, stores an image of the current frame on the machine
        :return: None
        """
        if self.video_handler.video_playing is False:
            image = self.video_handler.get_current_frame()
            if image is not None:
                filename = QFileDialog.getSaveFileName(dir=self.video_path, caption="Save Frame", filter=".png")
                if filename != ('', ''):
                    cv2.imwrite(filename[0] + filename[1], image)

    def set_video_folder_clicked(self):
        """
        User clicks set folder button, brings up dialog for user to select folder to load videos from
        :return: None
        """
        self.video_handler.pause_video()
        path = QFileDialog.getExistingDirectory(dir=self.video_path, caption="Set Path to Analyze Videos")
        if path != '':
            self.video_path = path
        self.populate_video_list()

    def refresh_clicked(self):
        """
        User clicked refresh button, updates the list of videos in the currently selected folder
        :return: None
        """
        self.populate_video_list()

    def playback_slider_pressed(self):
        """
        Event fired when playback slider is pressed with mouse, but not moved. Pauses playback.
        :return: None
        """
        self.video_handler.pause_video()
        # time.sleep(0.1)

    def playback_slider_released(self):
        """
        Event fired when playback slider is released with mouse. Updates playback location.
        :return: None
        """
        self.video_handler.set_current_playback_location(self.hslider_video_playback.value())

    def playback_slider_moved(self, index):
        """
        Event fired when playback slider is moved. Playback location is adjusted according to direction.
        :param index: Integer showing current position of the slider, corresponds to current frame number
        :return: None
        """
        self.video_handler.current_video.set(cv2.CAP_PROP_POS_FRAMES, index)
        if index >= self.prev_playback_slider_index:
            self.video_handler.skip_frame_forward(slider=True)
            self.format_label_current_run_time({"label_val" : int(index/self.video_handler.fps)})
        else:
            self.video_handler.skip_frame_backwards(slider=True)
            self.format_label_current_run_time({"label_val": int(index / self.video_handler.fps)})

        self.prev_playback_slider_index = index

    def showEvent(self, event):
        """
        Event fired when opening the dialog. Useful for last-minute inits.
        :param event: QShowEvent object
        :return: None
        """
        self.populate_video_list()

    def closeEvent(self, event):
        """
        Event fired when closing dialog. Useful for correct shutdown.
        :param event: QCloseEvent
        :return: None
        """
        print(event)
        self.video_handler.is_alive = False

    def shutdown_video_handler(self):
        """
        Signals that the video handler object should stop, useful for shutting down correctly.
        :return: None
        """
        self.video_handler.is_alive = False

    def populate_video_list(self):
        """
        Loads all .avi recordings from the current video path and displays in list
        :return: None
        """
        self.list_recordings.clear()
        for v in os.listdir(self.video_path):
            if v[-4:len(v)] == ".avi":
                self.list_recordings.addItem(v)

    def format_label_current_run_time(self, run_time):
        """
        Formats the current label to display correct current run time of the video playback
        :param run_time: Dictionary object formatted as {'label_val' : int, 'slider_val': int}
        :return: None
        """
        run_time = int(run_time["label_val"])
        h = run_time // 60 // 60 % 60
        m = run_time // 60 % 60
        s = run_time % 60

        h_str = str(h) if h >= 10 else "0" + str(h)
        m_str = str(m) if m >= 10 else "0" + str(m)
        s_str = str(s) if s >= 10 else "0" + str(s)

        self.label_vid_time.setText(h_str + ":" + m_str + ":" + s_str)

    def format_label_total_run_time(self, run_time):
        """
        Format the current lable to display total run time of video playback
        :param run_time: Dictionary object formatted as {'label_val' : int, 'slider_val': int}
        :return: None
        """
        h = run_time // 60 // 60 % 60
        m = run_time // 60 % 60
        s = run_time % 60

        h_str = str(h) if h >= 10 else "0" + str(h)
        m_str = str(m) if m >= 10 else "0" + str(m)
        s_str = str(s) if s >= 10 else "0" + str(s)

        self.label_vid_total_time.setText(h_str + ":" + m_str + ":" + s_str)