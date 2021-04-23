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
    def __init__(self, video_path, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.video_path = video_path
        # print(self.label_video_view.width())
        # self.video_handler = VideoHandler(video_path, self.label_video_view.width(), self.label_video_view.height())

        self.video_handler = VideoHandler(video_path, 800, 600)
        # self.video_handler.start()

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
        self.video_handler.set_analyze(analyze)

    def keypress_play_pause(self):
        if self.video_handler.isRunning():
            self.video_handler.pause_video()
        else:
            self.video_handler.play_video()

    def set_fps_label(self, fps_val):
        self.label_video_fps.setText("Selected Video FPS: " + str(fps_val))

    def update_slider_position(self, pos):
        self.hslider_video_playback.setValue(pos["slider_val"])

    def update_video_view(self, pix_map):
        self.label_video_view.setPixmap(pix_map)

    def show_video(self, video_item):
        self.video_handler.set_video(video_item.text())
        self.video_handler.stop_video()
        self.hslider_video_playback.setMaximum(self.video_handler.nr_of_frames)
        self.hslider_video_playback.setValue(0)

    def play_clicked(self):
        self.video_handler.play_video()

    def pause_clicked(self):
        self.video_handler.pause_video()

    def stop_clicked(self):
        self.video_handler.stop_video()
        self.hslider_video_playback.setValue(0)

    def skip_fwd_clicked(self):
        self.video_handler.skip_frame_forward(clicked=True, frames_to_skip=int(self.combo_frame_skip.currentText()))

    def skip_back_clicked(self):
        self.video_handler.skip_frame_backwards(clicked=True, frames_to_skip=int(self.combo_frame_skip.currentText()))

    def selected_playback_speed(self, speed):
        multiplier = float(speed[0:-1])
        self.video_handler.set_playback_speed(multiplier)

    def save_frame_clicked(self):
        if self.video_handler.video_playing is False:
            image = self.video_handler.get_current_frame()
            if image is not None:
                filename = QFileDialog.getSaveFileName(dir=self.video_path, caption="Save Frame", filter=".png")
                if filename != ('', ''):
                    cv2.imwrite(filename[0] + filename[1], image)

    def set_video_folder_clicked(self):
        self.video_handler.pause_video()
        path = QFileDialog.getExistingDirectory(dir=self.video_path, caption="Set Path to Analyze Videos")
        if path != '':
            self.video_path = path
        self.populate_video_list()

    def refresh_clicked(self):
        self.populate_video_list()

    def playback_slider_pressed(self):
        self.video_handler.pause_video()
        # time.sleep(0.1)

    def playback_slider_released(self):
        self.video_handler.set_current_playback_location(self.hslider_video_playback.value())

    def playback_slider_moved(self, index):
        self.video_handler.current_video.set(cv2.CAP_PROP_POS_FRAMES, index)
        if index >= self.prev_playback_slider_index:
            self.video_handler.skip_frame_forward(slider=True)
            self.format_label_current_run_time({"label_val" : int(index/self.video_handler.fps)})
        else:
            self.video_handler.skip_frame_backwards(slider=True)
            self.format_label_current_run_time({"label_val": int(index / self.video_handler.fps)})

        self.prev_playback_slider_index = index

    def showEvent(self, event):
        self.populate_video_list()

    def closeEvent(self, event):
        self.video_handler.is_alive = False
        # if self.current_video is not None:
        #     self.current_video.release()
        #     self.label_video_view.clear()

    def shutdown_video_handler(self):
        self.video_handler.is_alive = False

    def populate_video_list(self):
        self.list_recordings.clear()
        for v in os.listdir(self.video_path):
            if v[-4:len(v)] == ".avi":
                self.list_recordings.addItem(v)

    def format_label_current_run_time(self, run_time):
        # print(run_time)
        run_time = int(run_time["label_val"])
        h = run_time // 60 // 60 % 60
        m = run_time // 60 % 60
        s = run_time % 60

        h_str = str(h) if h >= 10 else "0" + str(h)
        m_str = str(m) if m >= 10 else "0" + str(m)
        s_str = str(s) if s >= 10 else "0" + str(s)

        self.label_vid_time.setText(h_str + ":" + m_str + ":" + s_str)

    def format_label_total_run_time(self, run_time):
        h = run_time // 60 // 60 % 60
        m = run_time // 60 % 60
        s = run_time % 60

        h_str = str(h) if h >= 10 else "0" + str(h)
        m_str = str(m) if m >= 10 else "0" + str(m)
        s_str = str(s) if s >= 10 else "0" + str(s)

        self.label_vid_total_time.setText(h_str + ":" + m_str + ":" + s_str)

    # def resizeEvent(self, event):
    #     if self.current_frame is not None:
    #         self.set_frame_video_view(self.current_frame)