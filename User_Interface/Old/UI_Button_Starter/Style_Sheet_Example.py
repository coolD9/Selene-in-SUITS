import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the window
        self.setWindowTitle("Styled GUI Example")
        self.setGeometry(100, 100, 800, 600)

        # Create a layout for the window
        layout = QVBoxLayout()

        # Create some buttons
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")

        # Add buttons to the layout
        layout.addWidget(button1)
        layout.addWidget(button2)

        # Set layout to the window
        self.setLayout(layout)

        # Define the stylesheet to apply
        self.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                font-size: 16px;
                border-radius: 8px;
                padding: 10px;
                margin: 5px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QLabel {
                font-size: 18px;
                color: #333;
            }
        """)

        # Optionally, set a custom font for the window
        font = QFont("Arial", 14)
        self.setFont(font)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
