
import sys
import PySide6.QtCore
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QPushButton, QLabel, QPlainTextEdit
from PySide6.QtCore import QFile

print(PySide6.__version__)
print(PySide6.QtCore.__version__)

first_label = ""
second_label = ""
text_field = ""


def load_ui_components():
    return


def test_btn_click():
    print("First button got clicked!")


# def test_btn_second_click(label):
#     val = "Some val"
#     print(label)
#
#     def inner():
#         print("Second button got clicked! Setting label to " + val)
#         label(val)
#     return inner

def test_btn_second_click(val):
    print("Second button was clicked!" + val)
    first_label.setText(val)
    p = text_field.document()
    print(p.toPlainText())
    print(text_field.document())


def hello(func):
    def inner():
        print("Hello")
        func()
    return inner


@hello
def name():
    print("Alice")


def load_form():
    # let ui component load different forms and redraw window, one form per app page!
    return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui_file = QFile("test2.ui")
    loader = QUiLoader()
    window = loader.load(ui_file)
    boxes = window.findChildren(QPushButton)

    for b in boxes:
        if "First" in b.text():
            b.clicked.connect(name)
        if "Second" in b.text():
            b.clicked.connect(lambda: test_btn_second_click("vjjyjygy"))
    first_label = window.findChild(QLabel, "label")
    second_label = window.findChild(QLabel, "label_2")
    text_field = window.findChild(QPlainTextEdit)
    first_label.setText("Ya found me!")
    ui_file.close()
    window.setWindowTitle("CI-VTS")
    window.show()
    sys.exit(app.exec_())
