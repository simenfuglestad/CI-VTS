from PySide6.QtCore import *
from PySide6.QtGui import *
import time
import cv2
import os


class VideoHandler(QThread):
    signal_read_frame = Signal(bytes)
    signal_read_first_frame = Signal(bytes)
    signal_current_play_time = Signal(bytes)
    signal_total_run_time = Signal(bytes)
    signal_set_fps_in_dialog = Signal(bytes)

    def __init__(self, video_path, frame_display_width, frame_display_height, parent=None):
        super().__init__(parent)
        self.is_alive = True

        self.current_video = None
        self.current_frame = None
        self.video_frame_data = []
        self.nr_of_frames = -1
        self.fps = -1
        self.video_path = video_path
        self.frame_display_width = frame_display_width
        self.frame_display_height = frame_display_height

        self.current_playback_location = 0
        self.playback_speed_multiplier = 1
        self.video_duration = -1
        self.frames_to_skip = 1
        self.video_playing = False
        self.video_paused = False

    def run(self):
        while self.is_alive:
            if self.video_playing and self.current_video is not None:
                try:
                    t = time.perf_counter()
                    self.skip_frame_forward()
                    self.signal_current_play_time.emit(
                        {"label_val": int(self.current_playback_location / self.fps),
                         "slider_val": self.current_playback_location})
                    time.sleep(((1/self.fps) / self.playback_speed_multiplier) - (time.perf_counter() - t))
                except Exception as e:
                    print("Error when playing video")
                    print(e)

    def set_frames_to_skip(self, i):
        self.frames_to_skip = int(self.combo_frame_skip.itemText(i))

    def set_playback_speed(self, multiplier):
        self.playback_speed_multiplier = multiplier

    def set_current_playback_location(self, val):
        self.current_playback_location = val

    def get_current_frame(self):
        return self.current_frame

    def set_video(self, video_name):
        try:
            self.current_playback_location = 0
            self.load_video(video_name)
            self.signal_set_fps_in_dialog.emit(self.fps)
            self.set_frame(self.current_frame)
            self.video_duration = int(self.nr_of_frames/self.fps)
            self.signal_total_run_time.emit(self.video_duration)
        except Exception as e:
            print("An error occurred when trying to load video '" + video_name + "' for analysis")
            print(e)

    def set_frame(self, frame):
        if self.current_video is not None and self.current_frame is not None:
            h, w, ch = frame.shape
            bytes_per_line = ch * w

            qt_image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)

            # scaled_image = qt_image.scaled(self.label_video_view.width(), self.label_video_view.height(), Qt.KeepAspectRatio)
            scaled_image = qt_image.scaled(self.frame_display_width, self.frame_display_height, Qt.KeepAspectRatio)
            pix_map = QPixmap.fromImage(scaled_image)
            self.signal_read_frame.emit(pix_map)

    def play_video(self):
        if self.current_video is not None and self.fps > 0:
            self.video_playing = True
            self.video_paused = False

    def pause_video(self):
        self.video_playing = False
        # self.video_paused = True
        print(self.current_playback_location)
        # self.current_video.set(cv2.CAP_PROP_POS_FRAMES, self.current_playback_location)

    def stop_video(self):
        self.video_playing = False
        self.video_paused = True
        self.current_playback_location = 0
        self.signal_current_play_time.emit({"label_val": 0, "slider_val" : 0})
        self.current_video.set(cv2.CAP_PROP_POS_FRAMES, 0)
        # self.hslider_video_playback.setValue(0)
        # self.format_label_run_time(0, self.label_vid_time)
        r, frame = self.current_video.read()
        if r:
            self.set_frame(frame)

    def skip_frame_forward(self, clicked=False, frames_to_skip=1):
        if self.current_playback_location < self.nr_of_frames and self.current_video is not None:
            if clicked:
                self.pause_video()
            self.current_playback_location += frames_to_skip
            if self.current_playback_location > self.nr_of_frames:
                self.current_playback_location = self.nr_of_frames

            if frames_to_skip != 1:
                self.current_video.set(cv2.CAP_PROP_POS_FRAMES, self.current_playback_location)

            r, frame = self.current_video.read()
            if r:
                self.set_frame(frame)
                self.current_frame = frame
                if clicked:
                    self.signal_current_play_time.emit(
                        {"label_val": int(self.current_playback_location / self.fps),
                         "slider_val": self.current_playback_location})
            else:
                print("skipped ahead of end")
        else:
            self.pause_video()

    def skip_frame_backwards(self, frames_to_skip=1):
        if 0 < self.current_playback_location <= self.nr_of_frames and self.current_video is not None:
            self.pause_video()
            self.current_playback_location -= frames_to_skip
            if self.current_playback_location < 0:
                self.current_playback_location = 0

            if frames_to_skip != 1:
                self.current_video.set(cv2.CAP_PROP_POS_FRAMES, self.current_playback_location)

            r, frame = self.current_video.read()
            if r:
                self.signal_current_play_time.emit(
                    {"label_val": int(self.current_playback_location / self.fps),
                     "slider_val": self.current_playback_location})

                self.set_frame(frame)
                self.current_frame = frame

    def load_video(self, video_name):
        if self.current_video is not None:
            self.current_video.release()
        path = os.path.abspath(self.video_path + video_name)
        self.current_video = cv2.VideoCapture(path)
        first_cap, first_frame = self.current_video.read()
        if first_cap:
            nr_of_frames = int(self.current_video.get(cv2.CAP_PROP_FRAME_COUNT))
            self.current_frame = first_frame
            self.nr_of_frames = nr_of_frames
            self.fps = self.current_video.get(cv2.CAP_PROP_FPS)
            self.current_playback_location = self.current_video.get(cv2.CAP_PROP_POS_FRAMES)
