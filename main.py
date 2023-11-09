# Made by Wessel Eikelboom (S2565196) for the Python assignment in the PiE course.
# Mechanical Engineering, Faculty of Engineering Technology, University of Twente
import sys
from PyQt5.QtWidgets import QApplication

from window import PeriodicTable

if __name__ == '__main__':  # Check whether the script is the main program
    app = QApplication([])  # Create an instance of QApplication and store as 'app'

    table_app = PeriodicTable()  # Create an instance of PeriodicTable and store as table_app
    table_app.show()  # Display the main window of application

    sys.exit(app.exec_())  # Start application event loop
    # Application will keep running until closed by user
