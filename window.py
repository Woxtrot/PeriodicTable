# Made by Wessel Eikelboom (S2565196) for the Python assignment in the PiE course.
# Mechanical Engineering, Faculty of Engineering Technology, University of Twente

from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QDesktopWidget

from config import WINDOW_WIDTH, WINDOW_HEIGHT
from data_loader import load_data
from canvas import PeriodicTableCanvas
from element_window import ElementInfoWindow


# The purpose of this class is to create the main window in which the matplotlib canvas is embedded

class PeriodicTable(QMainWindow):  # inherit from QMainWindow
    # The constructor initializes the main window
    def __init__(self):
        super().__init__()  # Initialize the superclass of Periodictable (QMainWindow)

        # Set window title and dimensions
        self.setWindowTitle('Periodic Table')
        self.setGeometry(0, 0, int(WINDOW_WIDTH), int(WINDOW_HEIGHT))
        self.setMinimumSize(900, 450)  # Set minimum width and height to ensure readability when the user scales the window
        # Create a central widget for the content of the window
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a canvas for drawing the periodic table
        data = load_data()  # Load data from csv file via load_data() function
        self.canvas = PeriodicTableCanvas(data, self)  # Pass loaded data and current instance to PeriodicTableCanvas to create canvas
        layout = QVBoxLayout()  # Manage widget layout
        layout.addWidget(self.canvas)  # Add canvas to layout
        central_widget.setLayout(layout)  # Assign layout to central widget

        # Create an instance to display element information
        self.element_info_window = None

        self.center_on_screen()
    # This function center the main window on the screen irrespective of screen resolution, its input is the current instance.
    def center_on_screen(self): # Based on: https://pythonprogramminglanguage.com/pyqt5-center-window/
        # Get the main window's geometry
        window = self.frameGeometry()
        # Get the screen resolution and center the window on the screen
        centerPoint = QDesktopWidget().availableGeometry().center()
        window.moveCenter(centerPoint)
        self.move(window.topLeft())

    # This function is responsbile of creating an instance for the ElementInfoWindow class, which in turn opens the element information window
    # its input is the current instance and element data
    def open_element_info(self, element_data):
        # It creates an instance of the ElementInfoWindow class to which it passes the element data
        # In this class the element information window is created
        self.element_info_window = ElementInfoWindow(element_data)
        self.element_info_window.show() # Newly created element information window is displayed to the user
        # Centering is not required as a Qdialog window centers on the parent window, which is in this case already centered
