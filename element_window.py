# Made by Wessel Eikelboom (S2565196) for the Python assignment in the PiE course.
# Mechanical Engineering, Faculty of Engineering Technology, University of Twente
import re
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QGridLayout, QDialog

# This class creates the element information window after an element box has been clicked.

class ElementInfoWindow(QDialog): # inherit from QDialog
    # The constructor initializes the element window
    def __init__(self, element_data):
        super().__init__() # Initialize the superclass of ElementInfoWindow (QDialog)
        self.setWindowTitle(element_data['Symbol']) # Title of the window is set to the clicked element symbol
        layout = QVBoxLayout() # a vertical layout is created to display the window contents

        # A title of the element name is created
        # It is assigned a font size, center alignment and added as a widget to the window
        title_label = QLabel(element_data['Element']) # a title of the element name is created
        title_font = title_label.font()
        title_font.setPointSize(18)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        info_grid = QGridLayout() # a grid layout is created for the element information
                                  # This enables the key and value to be displayed next to each other

        # Iterate through the element data and create labels for each key-value pair
        for row, (key, value) in enumerate(element_data.items()):
            if value:  # Exclude nan/empty values
                key = ' '.join(re.findall(r'[A-Z][a-z]*', key))
                if "Numberof" in key:
                    key = key.replace("Numberof", "Number of")

                key_label = QLabel(key) # Makes a label for the key
                value_label = QLabel(str(value)) # Makes a label for the value, converts it to a string

                key_label.setStyleSheet("font-weight: bold;") # Key is made bold
                value_label.setStyleSheet("color: #116f9e;")  # Value is given a color
                # Key and value are put next to each other for every row
                info_grid.addWidget(key_label, row, 0)
                info_grid.addWidget(value_label, row, 1)

        layout.addLayout(info_grid) # the grid layout is added into the main vertical layout
        self.setLayout(layout) # vertical layout is set as the main layout for the window
