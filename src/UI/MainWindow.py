from PySide6.QtCore import *
from PySide6.QtWidgets import *
from UI.ui import Ui_MainWindow
from stimulus.stimulus import *
import pyqtgraph as pg

class MainWindow(QMainWindow, Ui_MainWindow, QWidget):
    def __init__(self, settings_dialog, analysis_dialog, size, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Bind menu actions
        QObject.connect(self.actionSetup, SIGNAL("triggered()"), settings_dialog.show)
        QObject.connect(self.actionView, SIGNAL("triggered()"), analysis_dialog.show)

        # Init Stimulus Profile and Data
        self.current_stimulus_profile = None
        self.show_stimulus_profile_names()
        # self.stimulus_profile_names = [self.list_stim_profiles.addItem(x) for x in get_all_stimulus_profile_names()]
        self.stimulus_plot_data = []
        self.deleted_plot_items = []

        # Bindings Stimulus List
        self.list_stim_profiles.itemDoubleClicked.connect(self.view_stimulus_profile)

        # Bindings Stimulus UI
        self.btn_clear_plot.clicked.connect(self.clear_plot)
        self.btn_center_graph.clicked.connect(self.center_stimulus_plot)
        self.btn_add_stim.clicked.connect(self.add_to_stimulus_plot)
        self.btn_reset_stim.clicked.connect(self.reset_spin_and_slider)
        # self.btn_save_stim_profile.clicked.connect(save_stimulus_profile(self.stimulus_plot_data), self)

        self.hslider_stim_led_start.valueChanged.connect(self.slide_adjust_led_start)
        self.spin_stim_led_start.valueChanged.connect(self.spin_adjust_led_start)
        self.hslider_stim_led_end.valueChanged.connect(self.slide_adjust_led_end)
        self.spin_stim_led_end.valueChanged.connect(self.spin_adjust_led_end)

        # Bindings Stimulus Plot
        self.stim_profile_plot.sceneObj.sigMouseClicked.connect(self.stimulus_plot_clicked)
        # self.stim_profile_plot.setXRange(0, 100, 0)
        # self.stim_profile_plot.setYRange(0, 100, 0)

        # Keyboard event control variables
        self.holding_ctrl = False
        self.holding_s = False

        self.resize(size.width(), size.height())

    def show_stimulus_profile_names(self):
        self.list_stim_profiles.clear()
        for n in get_all_stimulus_profile_names():
            self.list_stim_profiles.addItem(n)

        self.list_stim_profiles.sortItems()

    def reset_spin_and_slider(self):
        self.spin_start_secs.setValue(0)
        self.spin_start_mins.setValue(0)
        self.spin_start_hours.setValue(0)

        self.spin_end_secs.setValue(0)
        self.spin_end_mins.setValue(0)
        self.spin_end_hours.setValue(0)

        self.hslider_stim_led_end.setValue(0)
        self.hslider_stim_led_start.setValue(0)

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_Control:
            self.holding_ctrl = False

        if event.key() == Qt.Key_S:
            self.holding_s = False

    def plot_stimulus_data(self):
        self.stim_profile_plot.clear()
        for p in self.stimulus_plot_data:
            self.stim_profile_plot.plot(p["time"], p["value"])

    def keyPressEvent(self, event):
        if self.holding_ctrl:
            if event.key() == Qt.Key_Z and len(self.stimulus_plot_data) > 0:
                deleted = self.stimulus_plot_data.pop()
                self.deleted_plot_items.append(deleted)
                self.plot_stimulus_data()

            elif event.key() == Qt.Key_S and len(self.stimulus_plot_data) > 0 and not self.holding_s:
                save_stimulus_profile(self.stimulus_plot_data)
                self.show_stimulus_profile_names()
                self.holding_s = True

            elif event.key() == Qt.Key_Y and len(self.deleted_plot_items) > 0:
                undeleted = self.deleted_plot_items.pop()
                self.stimulus_plot_data.append(undeleted)
                self.plot_stimulus_data()

        elif event.key() == Qt.Key_Delete and self.list_stim_profiles.count() > 0:
            delete_stimulus_profile(self.list_stim_profiles.currentItem().text())
            self.list_stim_profiles.takeItem(self.list_stim_profiles.currentRow())

        if event.key() == Qt.Key_Control:
            self.holding_ctrl = True

    def slide_adjust_led_end(self):
        slide_val = self.hslider_stim_led_end.value()
        self.spin_stim_led_end.setValue(slide_val)

        if self.checkbox_sync_led.isChecked():
            self.spin_stim_led_start.setValue(slide_val)
            self.hslider_stim_led_start.setValue(slide_val)

    def slide_adjust_led_start(self):
        slide_val = self.hslider_stim_led_start.value()
        if self.checkbox_start.isChecked():
            self.spin_stim_led_start.setValue(0)
            self.hslider_stim_led_start.setValue(0)
        elif self.checkbox_sync_led.isChecked():
            self.spin_stim_led_end.setValue(slide_val)
            self.hslider_stim_led_start.setValue(slide_val)
        else:
            self.spin_stim_led_start.setValue(slide_val)

    def spin_adjust_led_start(self):
        spin_val_start = self.spin_stim_led_start.value()
        self.hslider_stim_led_start.setValue(spin_val_start)
        if self.checkbox_sync_led.isChecked():
            spin_val_end = self.spin_stim_led_end.value()
            self.hslider_stim_led_end.setValue(spin_val_end)

    def spin_adjust_led_end(self):
        spin_val = self.spin_stim_led_end.value()
        self.hslider_stim_led_end.setValue(spin_val)
        if self.checkbox_sync_led.isChecked():
            self.spin_stim_led_start.setValue(spin_val)
            self.hslider_stim_led_start.setValue(spin_val)

    def get_stimulus_start(self):
        hours = self.spin_start_hours.value()
        mins = self.spin_start_mins.value()
        secs = self.spin_start_secs.value()

        return hours * 60 * 60 + mins * 60 + secs

    def get_stimulus_end(self):
        hours = self.spin_end_hours.value()
        mins = self.spin_end_mins.value()
        secs = self.spin_end_secs.value()

        return hours * 60 * 60 + mins * 60 + secs

    def add_to_stimulus_plot(self):
        start = self.get_stimulus_start()
        end = self.get_stimulus_end()
        led_val_start = self.spin_stim_led_start.value()
        led_val_end = self.spin_stim_led_end.value()

        if self.validate_plot(start, end, led_val_start, led_val_end):
            data = {"time": [start, end], "value": [led_val_start, led_val_end]}
            self.stimulus_plot_data.append(data)
            self.stim_profile_plot.plot(data["time"], data["value"])

    def validate_plot(self, start, end, led_start, led_end):
        if led_start <= 0 and led_end <= 0 or end < start:
            return False

        interval = [start, end]

        if interval in self.stimulus_plot_data:
            return False

        for d in self.stimulus_plot_data:
            t = d["time"]
            if t[0] <= start < t[1] or t[0] <= end <= t[1]:
                return False

        return True

    def clear_plot(self):
        self.stim_profile_plot.clear()
        self.deleted_plot_items = self.deleted_plot_items + self.stimulus_plot_data
        self.stimulus_plot_data = []

    def stimulus_plot_clicked(self, mouse_click_event):
        print(mouse_click_event.pos().x())
        print(mouse_click_event.pos().y())

    def center_stimulus_plot(self):
        self.stim_profile_plot.enableAutoRange(enable=True)

    def view_stimulus_profile(self):
        selected = self.list_stim_profiles.selectedItems()[0].text()
        profile = load_stimulus_profile(selected)
        if profile is not None:
            self.label_stim_profile_name.setText(selected)
            self.stim_profile_plot.clear()
            self.current_stimulus_profile = profile
            data = profile["data"]
            for d in data:
                self.stim_profile_plot.plot(d["time"], d["value"])

            self.stimulus_plot_data = profile["data"]
            self.deleted_plot_items = []

    def add_profile_to_experiment(self):
        selected = self.list_stim_profiles.selectedItems()
        for s in selected:

            print(s.text())
        print(selected)