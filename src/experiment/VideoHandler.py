from PySide6.QtCore import *
from PySide6.QtGui import *
import time
import cv2
import os
from experiment.DataCollect import *
import json


class VideoHandler(QThread):
    """
    Handle the playback routines of videos displayed in the Analysis dialog.

    Attributes
    ----------
    signal_read_frame : Signal
        Qt signal object, emits a frame during playback
    signal_read_first_frame : Signal
        Qt signal object, emits the fist frame when a video is selected
    signal_current_play_time:
        Qt signal object, emits current playback time during playback and skipping operations
    signal_total_run_time:
        Qt signal object, emits total run time when a video is selected
    signal_set_fps_in_dialog:
        Qt signal object, emits fps to be set in dialog
    """
    signal_read_frame = Signal(bytes)
    signal_read_first_frame = Signal(bytes)
    signal_current_play_time = Signal(bytes)
    signal_total_run_time = Signal(bytes)
    signal_set_fps_in_dialog = Signal(bytes)

    def __init__(self, video_path, frame_display_width, frame_display_height):
        """
        Sets up a video handler object,
        :param video_path: Path to load video data from
        :param frame_display_width: Width of video playback frame
        :param frame_display_height: Height of video playback frame
        """
        super().__init__()
        self.is_alive = True

        self.video_name = None
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

        self.data_collect = None
        self.analyze = False
        self.analyze_json_info = "[xm, ym, w, h, id, frame]"
        self.analyze_in_progress = False
        self.frames_skip = 10

    def run(self):
        """
        Start the video playback in a new thread separate from the main application thread.
        :return: None
        """
        while self.is_alive:
            if self.video_playing and self.current_video is not None:
                try:
                    t = time.perf_counter()
                    self.skip_frame_forward()
                    self.signal_current_play_time.emit(
                        {"label_val": int(self.current_playback_location / self.fps),
                         "slider_val": self.current_playback_location})

                    # This sometimes causes bugs that halts playback if camera is not connected, consider removing.
                    time.sleep(((1/self.fps) / self.playback_speed_multiplier) - (time.perf_counter() - t))
                except Exception as e:
                    print("Error when playing video")
                    print(e)

    def set_playback_speed(self, multiplier):
        """
        Set playback muiltipler
        :param multiplier: Integer playback multiplier
        :return: None
        """
        self.playback_speed_multiplier = multiplier

    def set_current_playback_location(self, val):
        """
        Set current playback location
        :param val: Integer frame/slider position of playback to set
        :return: None
        """
        self.current_playback_location = val

    def get_current_frame(self):
        """
        Get current frame displayed to user
        :return: Integer indicating current frame
        """
        return self.current_frame

    def set_video(self, video_name):
        """
        Load a video from file and setup preparations for playback and tracking analysis
        :param video_name: String indicating name of video file to be loaded
        :return: None
        """
        try:
            self.data_collect = DataCollect(pop_num=15, skip_frames=self.frames_skip)
            self.current_playback_location = 0
            self.load_video(video_name)
            self.signal_set_fps_in_dialog.emit(self.fps)
            self.set_frame(self.current_frame)
            self.video_duration = int(self.nr_of_frames/self.fps)
            self.signal_total_run_time.emit(self.video_duration)
        except Exception as e:
            print("An error occurred when trying to load video '" + video_name + "' for analysis")
            print(e)

    def set_analyze(self, a):
        """
        Set flag indicating if tracking analysis should be perform. True indicates it should.
        :param a: bool flag
        :return: None
        """
        print(a)
        if self.data_collect is not None:
            self.analyze = a
            self.data_collect = DataCollect(pop_num=15, skip_frames=self.frames_skip)

    def write_data(self, data, file_path):
        """
        Write tracking data to file on the system.
        :param data: List of lists with tracking data, See DataCollect.py for more info
        :param file_path: str path to where file should be stored.
        :return: NOne
        """
        try:
            with open(file_path, 'a') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
                # print("wrote " + str(data) + "to file")

        except IOError as e:
            print("An error occurred when writing points data: \n" + e)

    def set_frame(self, frame):
        """
        Set the current frame of video playback
        :param frame: int current frame to set
        :return: None
        """
        if self.current_video is not None and self.current_frame is not None:
            h, w, ch = frame.shape
            bytes_per_line = ch * w

            if self.analyze:
                points, frame = self.data_collect.update(frame)
                if len(points) != 0:
                    self.write_data(points, self.video_path + self.video_name[0:-4] + "_analysis.json")
            qt_image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)

            # scaled_image = qt_image.scaled(self.label_video_view.width(), self.label_video_view.height(), Qt.KeepAspectRatio)
            scaled_image = qt_image.scaled(self.frame_display_width, self.frame_display_height, Qt.KeepAspectRatio)
            pix_map = QPixmap.fromImage(scaled_image)
            self.signal_read_frame.emit(pix_map)

    def play_video(self):
        """
        Start video playback
        :return: None
        """
        if self.current_video is not None and self.fps > 0:
            if self.analyze:
                name = self.video_path + self.video_name[0:-4] + "_analysis.json"
                if os.path.isfile(name):
                    os.remove(name)
                    self.write_data(self.analyze_json_info, name)
            self.video_playing = True
            self.video_paused = False
            if not self.isRunning():
                self.is_alive = True
                self.start()

    def pause_video(self):
        """
        Pause video playback
        :return: None
        """
        if self.isRunning():
            self.is_alive = False
            self.wait()
        self.video_playing = False

    def stop_video(self):
        """
        Stop video playback and reset playback positions and data collecting
        :return:
        """
        if self.isRunning():
            self.is_alive = False
            self.wait()
        self.analyze_in_progress = False
        self.data_collect = DataCollect(pop_num=15, skip_frames=self.frames_skip)
        self.video_playing = False
        self.video_paused = True
        self.current_playback_location = 0
        self.signal_current_play_time.emit({"label_val": 0, "slider_val": 0})
        self.current_video.set(cv2.CAP_PROP_POS_FRAMES, 0)
        r, frame = self.current_video.read()
        if r:
            self.set_frame(frame)

    def skip_frame_forward(self, slider=False, clicked=False, frames_to_skip=1):
        """
        Skip forward a number of frames in the video playback
        :param slider: flag to indicate if user drags the playback slider
        :param clicked: flag to indicate if user clicks any of the skip buttons
        :param frames_to_skip: number of frames to skip
        :return: None
        """
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
                if not slider:
                    self.signal_current_play_time.emit(
                        {"label_val": int(self.current_playback_location / self.fps),
                         "slider_val": self.current_playback_location})
            else:
                print("skipped ahead of end")
        else:
            self.pause_video()

    def skip_frame_backwards(self, slider=False, clicked=False, frames_to_skip=1):
        """
        Skip backwards a number of frames in the video playback
        :param slider: flag to indicate if user drags the playback slider
        :param clicked: flag to indicate if user clicks any of the skip buttons
        :param frames_to_skip: number of frames to skip
        :return: None
        """
        if 0 < self.current_playback_location <= self.nr_of_frames and self.current_video is not None:
            if self.video_playing or clicked:
                self.pause_video()

            self.current_playback_location -= frames_to_skip
            if self.current_playback_location < 0:
                self.current_playback_location = 0

            if frames_to_skip != 1:
                self.current_video.set(cv2.CAP_PROP_POS_FRAMES, self.current_playback_location)

            r, frame = self.current_video.read()
            if r:
                self.set_frame(frame)
                self.current_frame = frame
                if not slider:
                    self.signal_current_play_time.emit(
                        {"label_val": int(self.current_playback_location / self.fps),
                        "slider_val": self.current_playback_location})

    def load_video(self, video_name):
        """
        Load video from file and set metadata, used by set_video
        :param video_name: N
        :return:
        """
        if self.current_video is not None:
            self.current_video.release()
        path = os.path.abspath(self.video_path + video_name)
        self.video_name = video_name
        self.current_video = cv2.VideoCapture(path)
        first_cap, first_frame = self.current_video.read()
        if first_cap:
            nr_of_frames = int(self.current_video.get(cv2.CAP_PROP_FRAME_COUNT))
            self.current_frame = first_frame
            self.nr_of_frames = nr_of_frames
            self.fps = self.current_video.get(cv2.CAP_PROP_FPS)
            self.current_playback_location = self.current_video.get(cv2.CAP_PROP_POS_FRAMES)
