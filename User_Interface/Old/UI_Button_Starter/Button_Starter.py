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
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter, QColor, QPen, QFont

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Buttons')
        self.setGeometry(100, 100, 1920, 1080)  # Set the window size and position

        self.button_font = QFont("Times New Roman")
        self.button_font.setPointSize(20)

        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # _____ _____  ___  ___  ___   ______ _   _ _____ _____ _____ _   _  _____     _____ _____     _   _  ___________ _____ #
        #|_   _|  ___|/ _ \ |  \/  |   | ___ \ | | |_   _|_   _|  _  | \ | |/  ___|   |  __ \  _  |   | | | ||  ___| ___ \  ___|#
        #  | | | |__ / /_\ \| .  . |   | |_/ / | | | | |   | | | | | |  \| |\ `--.    | |  \/ | | |   | |_| || |__ | |_/ / |__  #
        #  | | |  __||  _  || |\/| |   | ___ \ | | | | |   | | | | | | . ` | `--. \   | | __| | | |   |  _  ||  __||    /|  __| #
        #  | | | |___| | | || |  | |   | |_/ / |_| | | |   | | \ \_/ / |\  |/\__/ /   | |_\ \ \_/ /   | | | || |___| |\ \| |___ #
        #  \_/ \____/\_| |_/\_|  |_/   \____/ \___/  \_/   \_/  \___/\_| \_/\____/     \____/\___/    \_| |_/\____/\_| \_\____/ #
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #                                                                                                                      
        # 
        # Only the initial declaration of your button will go here
        # Make sure to update the other class methods to properly handle interacting with your button
        #     

        # # # # # # # # # # # #
        # Rykir's Button      #
        # # # # # # # # # # # #

        # Declaration of button and initial attributes
        self.rykir_button = QPushButton("Display Name", self)
        self.rykir_button.setFont(self.button_font)

        # Movement of button to top left cell
        self.rykir_button.resize(self.width() // 3, self.height() // 12)
        self.rykir_button.move(self.width() // 12, self.height() // 32)

        # User defined attributes
        self.rykir_button.nameTag = "Rykir"
        self.rykir_button.activated = False # Necessary to be clicked

        # Signal connection
        self.rykir_button.clicked.connect(self.on_click)

        ## End Rykir's Button ##


        # # # # # # # # # # # #
        # 's Button      #
        # # # # # # # # # # # #


    def on_click(self):

        # Gathering data from button that was clicked
        button = self.sender()
        name = button.nameTag
        position = button.pos()

        # Display label for specific button
        if(not button.activated):
            # Create font
            labelFont = QFont()
            labelFont.setPointSize(30)

            # Initial label creation and relative location
            self.label = QLabel(self)
            self.label.setGeometry(0, 0, button.width(), button.height())
            self.label.setAlignment(Qt.AlignCenter)
            self.label.setFont(labelFont)
            self.label.move(position.x(), position.y() + 100)

            # Showing the label
            self.label.setText(f"This is {name}'s button!")
            self.label.show()
            button.activated = True

        else:
            # Hide
            self.label.hide()
            self.label.destroy()
            button.activated = False



    def resizeEvent(self, event):

        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # For neatness, everyone should add resize handling to their button and text
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # Currently, I'm not sure how to attach the text to the button so that it's resized correctly with the button
        # I've been experimenting with layout managers, but they seem clunky and difficult to manage, but I just need
        # to learn more
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

        # Rykir's Button resize handling
        self.rykir_button.resize(self.width() // 3, self.height() // 12)
        self.rykir_button.move(self.width() // 12, self.height() // 32)



        

        
        super().resizeEvent(event)

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
    window = Window() # Create window object
    window.show() # Show the window
    sys.exit(app.exec_()) # This executes the event loop

if __name__ == '__main__':
    main()
