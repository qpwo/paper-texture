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
        self.setAttribute(Qt.WA_X11NetWmWindowTypeDesktop, True)  # Added for X11

        # Combine multiple window flags to ensure staying on top
        flags = (
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool |  # Makes the window a tool window
            Qt.X11BypassWindowManagerHint  # Bypasses window manager
        )
        self.setWindowFlags(flags)

        self.show()

        # Raise window to top after showing
        self.raise_()
        self.activateWindow()

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

    def showEvent(self, event):
        # Ensure window stays on top when shown
        self.raise_()
        self.activateWindow()
        super().showEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PaperWindow("black-paper.png")
    sys.exit(app.exec_())
