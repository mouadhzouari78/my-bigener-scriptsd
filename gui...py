import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton





class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        label = QLabel(self)
        self.setGeometry(700, 300, 1000, 1000)
        self.setWindowTitle("programm ig")
        self.setWindowIcon(QIcon("Capture d'écran 2026-09-15 161255.png"))
        label.setText("Hello World")
        label.setFont(QFont("Times", 100, QFont.Bold))
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("background-color: gray;")
        label.setGeometry(0, 0, 1000, 200)
        label1 = QLabel(self)
        pixmap = QPixmap("Capture d'écran 2026-09-15 161255.png")
        label1.setPixmap(pixmap)
        label1.setGeometry(0, 0, 200, 500)
        label1.setScaledContents(True)
        label1.setStyleSheet("background-color: red;")
        label1.setGeometry(
            (self.width() - 1000) // 2,
            (self.height() - 600) // 2,
            1000,
            600
        )
        self.button = QPushButton(self)
        self.label2 = QLabel(self)

        self.ui()
    def ui(self):
            self.button.setText("dont Click me")
            self.button.setFont(QFont("Times", 39, QFont.Bold))
            self.button.setGeometry(320, 300, 400, 200)
            self.button.clicked.connect(self.click)
            self.label2.setText("Hello World")
            self.label2.setGeometry(
                ((self.width() - self.label2.width()) // 2) - 130,
                (self.height() - self.label2.height()) - 50,
                self.label2.width() + 300,
                self.label2.height() + 50
            )
            self.label2.setFont(QFont("Times", 50, QFont.Bold))
    def click(self):
        self.label2.setText("fuh u")
        self.button.setText("Clicked")
        self.button.setDisabled(True)
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
