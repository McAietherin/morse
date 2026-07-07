import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QLabel, QCheckBox, QRadioButton, QButtonGroup, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import pygame
import time


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(600, 200, 700, 800)
        self.setWindowTitle("Text to Morse code")
        self.setWindowIcon(QIcon("logs.jpg"))
        self.alab = QLabel(self)
        self.inp = QLineEdit(self)
        self.conv = QPushButton("Convert", self)
        self.lisn = QPushButton("Listen", self)
        self.outp = QLabel(self)
        self.initUI()

    def initUI(self):

        self.d = ""

        self.alab.setGeometry(50, 70, 700, 45)
        self.alab.setStyleSheet("font-size: 25px;")
        self.alab.setText("Enter text to be translated:")

        self.inp.setGeometry(50, 150, 600, 90)
        self.inp.setStyleSheet("""QLineEdit { 
                                    font-size: 30px;
                                    padding-left: 25px;
                                    font-family: Arial
                                }""")
        self.inp.setPlaceholderText("Plain text goes here")

        self.conv.setGeometry(50, 275, 600, 45)
        self.conv.setStyleSheet("""QPushButton{
                                    font-size: 20px;
                                    background-color: #0000ff;
                                    color: #ffffff;
                                }
                                QPushButton:hover{
                                    background-color: #0000bb;
                                }
                                """)
        self.conv.clicked.connect(self.clickevent)

        self.outp.setGeometry(50, 330, 600, 135)
        self.outp.setStyleSheet("font-size: 28px;")
        self.outp.setText("")
        self.outp.setWordWrap(True)

        self.lisn.setGeometry(50, 520, 0, 0)
        self.lisn.setStyleSheet("""QPushButton{
                                    font-size: 20px;
                                    background-color: #ffaa00;
                                    color: #ffffff;
                                }
                                QPushButton:hover{
                                    background-color: #bb6600;
                                }
                                """)
        self.lisn.clicked.connect(self.lisev)

        self.setStyleSheet("QRadioButton{font-size: 20px;}")

    def clickevent(self):
        self.d = ""
        lib = "abcdefghijklmnopqrstuvwxyz0123456789 "
        conv = ["._", "_...", "_._.", "_..", ".", "_.__", "__.", "....", "..", ".___", "_._", "._..", "__",
                "_.", "___", ".__.", "__._", "._.", "...", "_", ".._", "..._", ".__", "_.._", "_.__", "__..", "_____", ".____", "..___", "...__", "...._", ".....", "_....", "__...", "___..", "____.", "/"]
        test = self.inp.text().lower()
        for let in test:
            self.d += conv[lib.index(let)]+" "

        self.outp.setText(self.d)

        self.lisn.setGeometry(50, 520, 600, 45)

    def lisev(self):
        pygame.mixer.init()
        for char in self.d:
            match char:
                case " ":
                    pygame.mixer.music.stop()
                    time.sleep(0.24)
                case "/":
                    pygame.mixer.music.stop()
                    time.sleep(0.24)
                case ".":
                    pygame.mixer.music.load("dot.wav")
                    pygame.mixer.music.play()
                    time.sleep(0.24)
                    pygame.mixer.music.stop()
                    time.sleep(0.24)
                case "_":
                    pygame.mixer.music.load("dash.wav")
                    pygame.mixer.music.play()
                    time.sleep(0.72)
                    pygame.mixer.music.stop()
                    time.sleep(0.24)
                case _:
                    print("nuh uh")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
