# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#   Author(s): Rykir Evans, 
#   Title:     Button_Starter
#   Repo:      Selene-in-SUITS
#   Date:      1-26-2025 (Initial Creation)
#
#   Description:
#        This program was made to introduce elements of the PyQt5 library
#        for the NASA SUITS project UI development team. It showcases a
#        simple window in which each team member will code and design their
#        own button to display their name once clicked.
# 
#   Usage:
#        Other than simplistic button pressing to produce an output, this
#        program is meant to provide foundations to expand our UI further
#
#   Files:
#        button_starter.py
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter, QColor, QPen

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Buttons')
        self.setGeometry(100, 100, 1920, 1080)  # Set the window size and position

    # Grid painting
    def paintEvent(self, event):
        # Create a QPainter object to paint on the widget
        painter = QPainter(self)
        
        # Set the pen color to black
        pen = QPen(QColor(0, 0, 0))
        pen.setWidth(3)
        painter.setPen(pen)
        
        # Get the width and height of the window to determine the grid size
        width = self.width()
        height = self.height()

        # Set grid dimensions
        rows = 4
        cols = 2

        # Draw horizontal lines
        for row in range(rows + 1):
            # Calculate the y-coordinate for each horizontal line
            y = row * height // rows
            painter.drawLine(0, y, width, y)  # Draw from left to right

        # Draw vertical lines
        for col in range(cols + 1):
            # Calculate the x-coordinate for each vertical line
            x = col * width // cols
            painter.drawLine(x, 0, x, height)  # Draw from top to bottom

        painter.end()  # End the painting

def main():
    # This is to draw the grid
    app = QApplication(sys.argv)
    window = Window()

    # Global variables for location settings
    global width 
    width = window.width()
    global height
    height = window.height()



    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # _____ _____  ___  ___  ___   ______ _   _ _____ _____ _____ _   _  _____     _____ _____     _   _  ___________ _____ #
    #|_   _|  ___|/ _ \ |  \/  |   | ___ \ | | |_   _|_   _|  _  | \ | |/  ___|   |  __ \  _  |   | | | ||  ___| ___ \  ___|#
    #  | | | |__ / /_\ \| .  . |   | |_/ / | | | | |   | | | | | |  \| |\ `--.    | |  \/ | | |   | |_| || |__ | |_/ / |__  #
    #  | | |  __||  _  || |\/| |   | ___ \ | | | | |   | | | | | | . ` | `--. \   | | __| | | |   |  _  ||  __||    /|  __| #
    #  | | | |___| | | || |  | |   | |_/ / |_| | | |   | | \ \_/ / |\  |/\__/ /   | |_\ \ \_/ /   | | | || |___| |\ \| |___ #
    #  \_/ \____/\_| |_/\_|  |_/   \____/ \___/  \_/   \_/  \___/\_| \_/\____/     \____/\___/    \_| |_/\____/\_| \_\____/ #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #                                                                                                                      
                                                                                                                                                                                                                                       

    # # # # # # # # # # # #
    # Rykir's Button      #
    # # # # # # # # # # # #

    rykir_button = QPushButton("Display Name", window)
    rykir_button.resize(width // 3, height // 12)
    rykir_button.move(width // 12, height // 32)

    # Rest of the functionality is intended to be implemented soon


    # # # # # # # # # # # #
    # 
    # # # # # # # # # # # #






    window.show()
    sys.exit(app.exec_())

# # # # # # # # # # # #
# End of Program      #
# # # # # # # # # # # #

if __name__ == '__main__':
    main()
