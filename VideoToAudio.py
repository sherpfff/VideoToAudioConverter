import os
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QFileDialog, QTextEdit

class VideoToAudioConverter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Video to Audio Converter')
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        self.text_edit = QTextEdit()
        layout.addWidget(self.text_edit)

        self.select_button = QPushButton('Select Folder')
        self.select_button.clicked.connect(self.select_folder)
        layout.addWidget(self.select_button)

        self.convert_button = QPushButton('Convert Videos to Audio')
        self.convert_button.clicked.connect(self.convert_videos_to_audio)
        layout.addWidget(self.convert_button)

        self.central_widget.setLayout(layout)

        self.folder_path = ""

    def select_folder(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly
        folder = QFileDialog.getExistingDirectory(self, "Select Folder", options=options)
        if folder:
            self.folder_path = folder
            self.text_edit.append(f'Selected folder: {self.folder_path}')

    def convert_videos_to_audio(self):
        if not self.folder_path:
            self.text_edit.append('Please select a folder first.')
            return

        for filename in os.listdir(self.folder_path):
            if filename.endswith(".mp4"):
                mp4_file = os.path.join(self.folder_path, filename)
                mp3_file = os.path.join(self.folder_path, os.path.splitext(filename)[0] + ".mp3")

                # Используем FFmpeg для конвертации
                subprocess.run(["C:\\ffmpeg\\ffmpeg.exe", "-i", mp4_file, mp3_file])

                self.text_edit.append(f'Converted: {filename}')

        self.text_edit.append("Conversion completed.")

def run_app():
    app = QApplication([])
    window = VideoToAudioConverter()
    window.show()
    app.exec_()

if __name__ == '__main__':
    run_app()
