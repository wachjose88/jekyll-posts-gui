from os import listdir
from os.path import isfile

from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QListWidget


class Editor(QWidget):

    def __init__(self, parent=None, working_directory=None):
        super().__init__(parent)
        self.working_directory = working_directory
        self.vlayout = QVBoxLayout()
        self.hlayout = QHBoxLayout()
        self.posts_list = QListWidget()
        self.posts_list.itemDoubleClicked.connect(
            self.posts_list_itemDoubleClicked)
        self.build_posts_list()
        self.hlayout.addWidget(self.posts_list)
        self.vlayout.addLayout(self.hlayout)
        self.setLayout(self.vlayout)

    def build_posts_list(self):
        self.posts_list.clear()
        for post_file in listdir(self.working_directory):
            if isfile(post_file):
                self.posts_list.addItem(post_file)

    @pyqtSlot()
    def posts_list_itemDoubleClicked(self):
        pass