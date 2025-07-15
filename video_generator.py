import sys
from PyQt5 import QtWidgets, QtCore
import qdarkstyle
from moviepy import TextClip, ImageClip, VideoFileClip, CompositeVideoClip

class VideoGeneratorGUI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Video Generator")
        self.init_ui()

    def init_ui(self):
        central = QtWidgets.QWidget()
        self.setCentralWidget(central)
        main_layout = QtWidgets.QHBoxLayout(central)

        controls = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(controls)

        # Input type selection
        self.input_type = QtWidgets.QComboBox()
        self.input_type.addItems(["Text", "Image", "Video"])
        layout.addWidget(QtWidgets.QLabel("Input Type:"))
        layout.addWidget(self.input_type)

        # Source file path for Image/Video input
        file_layout = QtWidgets.QHBoxLayout()
        self.file_path = QtWidgets.QLineEdit()
        self.browse_btn = QtWidgets.QPushButton("Browse")
        self.browse_btn.clicked.connect(self.browse_file)
        file_layout.addWidget(self.file_path)
        file_layout.addWidget(self.browse_btn)
        layout.addWidget(QtWidgets.QLabel("Source File:"))
        layout.addLayout(file_layout)

        # Output length
        self.length_spin = QtWidgets.QSpinBox()
        self.length_spin.setRange(1, 60)
        self.length_spin.setSuffix(" sec")
        layout.addWidget(QtWidgets.QLabel("Output Length:"))
        layout.addWidget(self.length_spin)

        # Quality selection
        self.quality_combo = QtWidgets.QComboBox()
        self.quality_combo.addItems(["Low", "Medium", "High"])
        layout.addWidget(QtWidgets.QLabel("Quality:"))
        layout.addWidget(self.quality_combo)

        # Prompt input
        self.prompt = QtWidgets.QTextEdit()
        layout.addWidget(QtWidgets.QLabel("Prompt:"))
        layout.addWidget(self.prompt)

        # Output file path
        self.output_path = QtWidgets.QLineEdit("output.mp4")
        layout.addWidget(QtWidgets.QLabel("Output File:"))
        layout.addWidget(self.output_path)

        # Generate button
        self.generate_btn = QtWidgets.QPushButton("Generate Video")
        self.generate_btn.clicked.connect(self.generate_video)
        layout.addWidget(self.generate_btn)

        main_layout.addWidget(controls)

        # Preview placeholder
        self.preview = QtWidgets.QLabel("Preview")
        self.preview.setAlignment(QtCore.Qt.AlignCenter)
        self.preview.setStyleSheet(
            "background-color: #232323; color: #aaaaaa; border: 1px solid #444;"
        )
        main_layout.addWidget(self.preview, 1)

    def browse_file(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select File")
        if path:
            self.file_path.setText(path)

    def generate_video(self):
        input_type = self.input_type.currentText()
        length = self.length_spin.value()
        quality = self.quality_combo.currentText()
        prompt = self.prompt.toPlainText().strip()
        src = self.file_path.text().strip()
        output = self.output_path.text().strip()

        if input_type in {"Image", "Video"} and not src:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Please select a source file.")
            return
        if not output:
            QtWidgets.QMessageBox.warning(self, "Output Error", "Please specify an output file name.")
            return
        if input_type == "Text" and not prompt:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Please enter a prompt.")
            return

        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        try:
            if input_type == "Text":
                clip = TextClip(prompt, fontsize=48, color="white", size=(1280, 720))
                clip = clip.set_duration(length)
            elif input_type == "Image":
                clip = ImageClip(src).set_duration(length)
                if prompt:
                    text = TextClip(prompt, fontsize=48, color="white")
                    text = text.set_position("center").set_duration(length)
                    clip = CompositeVideoClip([clip, text])
            else:
                clip = VideoFileClip(src)
                if length < clip.duration:
                    clip = clip.subclip(0, length)
                if prompt:
                    text = TextClip(prompt, fontsize=48, color="white")
                    text = text.set_position("center").set_duration(clip.duration)
                    clip = CompositeVideoClip([clip, text])

            bitrate_map = {"Low": "500k", "Medium": "1500k", "High": "3000k"}
            clip.write_videofile(output, bitrate=bitrate_map.get(quality, "1500k"), fps=24)
            QtWidgets.QMessageBox.information(self, "Done", f"Video saved to {output}")
        except Exception as exc:
            QtWidgets.QMessageBox.critical(self, "Generation Error", str(exc))
        finally:
            QtWidgets.QApplication.restoreOverrideCursor()


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    gui = VideoGeneratorGUI()
    gui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
