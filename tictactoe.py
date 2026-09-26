import sys
from pathlib import Path
from PyQt5.QtGui import QIcon, QFont, QPixmap , QTransform
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 1. Automatically get the current user's home directory (e.g., C:\Users\poazw)
        HOME_DIR = Path.home()

        # 2. Point to the folder on the Desktop (change "assets" to match your exact folder name)
        ASSETS_DIR = HOME_DIR / "Desktop" / "ASSETS" / "images.png"
        ASSETS_DIRR = HOME_DIR / "Desktop" / "ASSETS" / "Capture d'écran 2026-09-18 143224.png"
        self.label = QLabel(self)
        pixmap = QPixmap(str(ASSETS_DIR))
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)
        self.label1 = QLabel(self)
        self.pixmap1 = QPixmap(str(ASSETS_DIRR))
        self.label1.setPixmap(self.pixmap1)
        self.label1.setScaledContents(True)
        self.setupUi()
        self.setWindowTitle("Tic Tac Toe")
        self.setWindowIcon(QIcon(str(ASSETS_DIR)))
        self.turn = "x"
        self.label2 = QLabel(self)
        self.button9 = QPushButton(self)
        self.button9.setText("  play again?")
        self.button9.setFont(QFont("Times", 25, QFont.Bold))
        self.button9.hide()
    def setupUi(self):
        self.setGeometry(700, 300, 1000, 600)
        self.label.setGeometry(
            (self.width() - 1000) // 2,
            (self.height() - 600) // 2,
            1000,
            600)
        #up
        self.button = QPushButton(self)
        self.button.setGeometry(0 , 0 , 310, 190)
        self.button.clicked.connect(self.clicked)
        self.button1 = QPushButton(self)
        self.button1.setGeometry(330 , 0 , 335, 190)
        self.button1.clicked.connect(self.clicked)
        self.button2 = QPushButton(self)
        self.button2.setGeometry(680 , 0 , 340, 190)
        self.button2.clicked.connect(self.clicked)
        #mid
        self.button3 = QPushButton(self)
        self.button3.setGeometry(0 ,200 , 310, 190)
        self.button3.clicked.connect(self.clicked)
        self.button4 = QPushButton(self)
        self.button4.setGeometry(330 ,200 , 335, 190)
        self.button4.clicked.connect(self.clicked)
        self.button5 = QPushButton(self)
        self.button5.setGeometry(680 ,200 , 340, 190)
        self.button5.clicked.connect(self.clicked)
        #down
        self.button6 = QPushButton(self)
        self.button6.setGeometry(0 ,405 , 310, 195)
        self.button6.clicked.connect(self.clicked)
        self.button7 = QPushButton(self)
        self.button7.setGeometry(330 ,405 , 335, 195)
        self.button7.clicked.connect(self.clicked)
        self.button8 = QPushButton(self)
        self.button8.setGeometry(680 ,405 , 340, 195)
        self.button8.clicked.connect(self.clicked)
    def clicked(self):
        if self.turn == "x":
            self.sender().setText("X")
            self.sender().setFont(QFont("Times", 75, QFont.Bold))
            self.turn = "o"
        elif self.turn == "o":
            self.sender().setText("O")
            self.sender().setFont(QFont("Times", 75, QFont.Bold))
            self.turn = "x"
        if self.button.text() != "" and self.button1.text() != "" and self.button2.text() != "" and self.button3.text() != "" and self.button4.text() != "" and self.button5.text() != "" and self.button6.text() != "" and self.button7.text() != "" and self.button8.text() != "":
            self.button9.setGeometry(370, 300, 250, 100)
            self.button9.show()
            self.button9.raise_()
            self.button9.clicked.connect(self.reset)
        if self.button.text() == self.button1.text() and self.button2.text() == self.button1.text() and self.button.text() != "":
            self.label1.show()
            self.label1.setGeometry(0, 80, 1000, 30)
            self.label1.raise_()
            #copy from here
            self.button.setDisabled(True)
            for i in range(1,9):
                getattr(self, f"button{i}").setDisabled(True)

            self.label2.setGeometry((self.width() // 2)-400, (self.height() // 2)-350, 1000, 500)
            self.label2.raise_()
            self.label2.setFont(QFont("Times", 50, QFont.Bold))
            self.label2.setStyleSheet("color : red;")
            self.label2.setText(f"the player using {"o" if self.turn == "x" else "x"} won")
            self.label2.show()
            self.button9.setGeometry(370, 300, 250, 100)
            self.button9.show()
            self.button9.raise_()
            self.button9.clicked.connect(self.reset)
        if self.button.text() == self.button3.text() and self.button3.text() == self.button6.text() and self.button6.text() != "":
            self.label1.show()
            transform = QTransform()
            transform.rotate(90)

            rotated = self.pixmap1.transformed(transform)
            self.label1.setPixmap(rotated)
            self.label1.setGeometry(140, 0, 25, 675)
            self.label1.raise_()
            self.button.setDisabled(True)
            for i in range(1, 9):
                getattr(self, f"button{i}").setDisabled(True)

            self.label2.setGeometry((self.width() // 2) - 400, (self.height() // 2) - 350, 1000, 500)
            self.label2.raise_()
            self.label2.setFont(QFont("Times", 50, QFont.Bold))
            self.label2.setStyleSheet("color : red;")
            self.label2.setText(f"the player using {"o" if self.turn == "x" else "x"} won")
            self.label2.show()
            self.button9.setGeometry(370, 300, 250, 100)
            self.button9.show()
            self.button9.raise_()
            self.button9.clicked.connect(self.reset)

        if self.button.text() == self.button4.text() and self.button4.text() == self.button8.text() and self.button8.text() != "":
            self.label1.show()
            transform = QTransform()
            transform.rotate(60)

            rotated = self.pixmap1.transformed(transform)
            self.label1.setPixmap(rotated)
            self.label1.setGeometry(0, 0, 1100, 675)
            self.label1.raise_()
            self.button.setDisabled(True)
            for i in range(1, 9):
                getattr(self, f"button{i}").setDisabled(True)

            self.label2.setGeometry((self.width() // 2) - 400, (self.height() // 2) - 350, 1000, 500)
            self.label2.raise_()
            self.label2.setFont(QFont("Times", 50, QFont.Bold))
            self.label2.setStyleSheet("color : red;")
            self.label2.setText(f"the player using {"o" if self.turn == "x" else "x"} won")
            self.label2.show()
            self.button9.setGeometry(370, 300, 250, 100)
            self.button9.show()
            self.button9.raise_()
            self.button9.clicked.connect(self.reset)
            for i in range(1, 9):
                getattr(self, f"button{i}").setDisabled(True)
        if self.button3.text() == self.button4.text() and self.button4.text() == self.button5.text() and self.button5.text() != "":
            self.label1.show()
            self.label1.setGeometry(0, 275, 1000, 30)
            self.label1.raise_()
            self.button.setDisabled(True)
            for i in range(1, 9):
                getattr(self, f"button{i}").setDisabled(True)

            self.label2.setGeometry((self.width() // 2) - 400, (self.height() // 2) - 350, 1000, 500)
            self.label2.raise_()
            self.label2.setFont(QFont("Times", 50, QFont.Bold))
            self.label2.setStyleSheet("color : red;")
            self.label2.setText(f"the player using {"o" if self.turn == "x" else "x"} won")
            self.label2.show()
            self.button9.setGeometry(370, 300, 250, 100)
            self.button9.show()
            self.button9.raise_()
            self.button9.clicked.connect(self.reset)
        if self.button6.text() == self.button7.text() and self.button7.text() == self.button8.text() and self.button8.text() != "":
            self.label1.show()
            self.label1.setGeometry(0, 490, 1000, 25)
            self.label1.raise_()
            self.button.setDisabled(True)
            for i in range(1, 9):
                getattr(self, f"button{i}").setDisabled(True)

            self.label2.setGeometry((self.width() // 2) - 400, (self.height() // 2) - 350, 1000, 500)
            self.label2.raise_()
            self.label2.setFont(QFont("Times", 50, QFont.Bold))
            self.label2.setStyleSheet("color : red;")
            self.label2.setText(f"the player using {"o" if self.turn == "x" else "x"} won")
            self.label2.show()
            self.button9.setGeometry(370, 300, 250, 100)
            self.button9.show()
            self.button9.raise_()
            self.button9.clicked.connect(self.reset)
        if self.button2.text() == self.button4.text() and self.button4.text() == self.button6.text() and self.button6.text() != "":
            self.label1.show()
            transform = QTransform()
            transform.rotate(-60)

            rotated = self.pixmap1.transformed(transform)
            self.label1.setPixmap(rotated)
            self.label1.setGeometry(-75, 0, 1100, 675)
            self.label1.raise_()
            self.button.setDisabled(True)
            for i in range(1, 9):
                getattr(self, f"button{i}").setDisabled(True)

            self.label2.setGeometry((self.width() // 2) - 400, (self.height() // 2) - 350, 1000, 500)
            self.label2.raise_()
            self.label2.setFont(QFont("Times", 50, QFont.Bold))
            self.label2.setStyleSheet("color : red;")
            self.label2.setText(f"the player using {"o" if self.turn == "x" else "x"} won")
            self.label2.show()
            self.button9.setGeometry(370, 300, 250, 100)
            self.button9.show()
            self.button9.raise_()
            self.button9.clicked.connect(self.reset)
        if self.button1.text() == self.button4.text() and self.button4.text() == self.button7.text() and self.button7.text() != "":
            self.label1.show()
            transform = QTransform()
            transform.rotate(90)

            rotated = self.pixmap1.transformed(transform)
            self.label1.setPixmap(rotated)
            self.label1.setGeometry(485, 0, 25, 675)
            self.label1.raise_()
            self.button.setDisabled(True)
            self.button.setDisabled(True)
            for i in range(1, 9):
                getattr(self, f"button{i}").setDisabled(True)

            self.label2.setGeometry((self.width() // 2) - 400, (self.height() // 2) - 350, 1000, 500)
            self.label2.raise_()
            self.label2.setFont(QFont("Times", 50, QFont.Bold))
            self.label2.setStyleSheet("color : red;")
            self.label2.setText(f"the player using {"o" if self.turn == "x" else "x"} won")
            self.label2.show()
            self.button9.setGeometry(370, 300, 250, 100)
            self.button9.show()
            self.button9.raise_()
            self.button9.clicked.connect(self.reset)
        if self.button2.text() == self.button5.text() and self.button5.text() == self.button8.text() and self.button8.text() != "":
            self.label1.show()
            transform = QTransform()
            transform.rotate(90)

            rotated = self.pixmap1.transformed(transform)
            self.label1.setPixmap(rotated)
            self.label1.setGeometry(840, 0, 25, 675)
            self.label1.raise_()
            self.button.setDisabled(True)
            self.button.setDisabled(True)
            for i in range(1, 9):
                getattr(self, f"button{i}").setDisabled(True)

            self.label2.setGeometry((self.width() // 2) - 400, (self.height() // 2) - 350, 1000, 500)
            self.label2.raise_()
            self.label2.setFont(QFont("Times", 50, QFont.Bold))
            self.label2.setStyleSheet("color : red;")
            self.label2.setText(f"the player using {"o" if self.turn == "x" else "x"} won")
            self.label2.show()
            self.button9.setGeometry(370, 300, 250, 100)
            self.button9.show()
            self.button9.raise_()
            self.button9.clicked.connect(self.reset)
    def reset(self):
        buttons = [
            self.button, self.button1, self.button2,
            self.button3, self.button4, self.button5,
            self.button6, self.button7, self.button8
        ]

        for button in buttons:
            button.setText("")
            button.setEnabled(True)

        self.turn = "x"
        self.label1.hide()
        self.label2.hide()
        self.button9.hide()
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()