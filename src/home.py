from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QVBoxLayout


class Home(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.vlayout = QVBoxLayout()
        self.header = QLabel(self.tr('Select the directory containing the posts.'))
        self.vlayout.addWidget(self.header)
        self.main = QGridLayout()
        self.lbl_directory = QLabel(self.tr('Directory:'))
        self.main.addWidget(self.lbl_directory, 0, 0)
        self.txt_directory = QLineEdit()
        self.main.addWidget(self.txt_directory, 0, 1)
        self.btn_directory = QPushButton(self.tr('Browse'))
        self.btn_directory.clicked.connect(self.btn_directory_clicked)
        self.main.addWidget(self.btn_directory, 0, 2)
        self.btn_open = QPushButton(self.tr('Open'))
        self.btn_open.clicked.connect(self.btn_open_clicked)
        self.main.addWidget(self.btn_open, 1, 0, 3, 0)
        self.vlayout.addLayout(self.main)
        self.vlayout.addStretch()
        self.setLayout(self.vlayout)

    @pyqtSlot()
    def btn_directory_clicked(self):
        path = QFileDialog.getExistingDirectory(self, self.tr('Directory:'))
        self.txt_directory.setText(path)

    @pyqtSlot()
    def btn_open_clicked(self):
        self.parent().working_directory = self.txt_directory.text()
        self.parent().open_editor()
