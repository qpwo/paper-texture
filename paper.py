"""
overlay paper texture on top of the screen
download "https://www.transparenttextures.com/patterns/black-paper.png"
python paper.py &
"""
filename = "black-paper.png"
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt

class PaperWindow(QWidget):
    def __init__(self, image_path):
        super().__init__()
        self.image_path = image_path
        self.pixmap = QPixmap(image_path)
        self.initUI()

    def initUI(self):
        # Get screen size
        screen = QApplication.primaryScreen().size()

        # Set window size to screen size
        self.setGeometry(0, 0, screen.width(), screen.height())

        # Set window attributes
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)  # Added WindowStaysOnTopHint

        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)

        # Set opacity to 20%
        painter.setOpacity(0.15)

        # Calculate how many tiles we need in each direction
        cols = self.width() // self.pixmap.width() + 1
        rows = self.height() // self.pixmap.height() + 1

        # Draw the tiles
        for row in range(rows):
            for col in range(cols):
                x = col * self.pixmap.width()
                y = row * self.pixmap.height()
                painter.drawPixmap(x, y, self.pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PaperWindow("black-paper.png")
    sys.exit(app.exec_())
