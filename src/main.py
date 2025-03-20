import sys

from PyQt6.QtWidgets import QMainWindow, QApplication

from home import Home
from editor import Editor


class JekyllPostsGUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle(self.tr('Jekyll Posts'))
        self.home = Home()
        self.editor = None
        self.setCentralWidget(self.home)
        self.working_directory = None
        self.show()

    def open_editor(self):
        self.editor = Editor(self, self.working_directory)
        self.setCentralWidget(self.editor)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    jpg = JekyllPostsGUI()
    sys.exit(app.exec())