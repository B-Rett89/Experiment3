import sys
from PyQt5 import QtWidgets, QtCore

class VideoGeneratorGUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Video Generator")
        self.init_ui()

    def init_ui(self):
        layout = QtWidgets.QVBoxLayout()

        # Input type selection
        self.input_type = QtWidgets.QComboBox()
        self.input_type.addItems(["Text", "Image", "Video"])
        layout.addWidget(QtWidgets.QLabel("Input Type:"))
        layout.addWidget(self.input_type)

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

        # Generate button
        self.generate_btn = QtWidgets.QPushButton("Generate Video")
        self.generate_btn.clicked.connect(self.generate_video)
        layout.addWidget(self.generate_btn)

        self.setLayout(layout)

    def generate_video(self):
        input_type = self.input_type.currentText()
        length = self.length_spin.value()
        quality = self.quality_combo.currentText()
        prompt = self.prompt.toPlainText().strip()

        if not prompt:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Please enter a prompt.")
            return

        # Placeholder for actual AI generation logic
        QtWidgets.QMessageBox.information(
            self,
            "Generation Started",
            f"Generating a {length}-second {quality} quality video from {input_type.lower()} input...",
        )
        # Here you would call your AI backend


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = VideoGeneratorGUI()
    gui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
