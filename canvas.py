# Made by Wessel Eikelboom (S2565196) for the Python assignment in the PiE course.
# Mechanical Engineering, Faculty of Engineering Technology, University of Twente
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas # based on https://www.pythonguis.com/tutorials/plotting-matplotlib/

from config import TABLE_WIDTH, TABLE_HEIGHT, ELEMENT_SIZE, SPACING, MARGIN, category_colors

# This class is responsible for drawing the table of elements
# It first creates a canvas using matplotlib
# Element boxes are drawn on this canvas using matplotlib
# The element boxes are plotted in the correct locations based on the element data
# Element symbol and atomic number are displayed in the element boxes and the element boxes are made clickable

class PeriodicTableCanvas(FigureCanvas): # inherit from FigureCanvas
    # The constructor of the class is called when an instance of the class is created
    # It takes the element data as input
    # It has no parent
    def __init__(self, data, parent=None):
        self.parent_instance = parent
        fig, ax = plt.subplots()  # Creates a new Matplotlib figure and axis for plotting
        super().__init__(fig)  # Initialize the superclass of PeriodicTableCanvas (FigureCanvas)
        self.setParent(parent)
        self.data = data
        self.ax = ax
        self.ax.set_xlim(0, TABLE_WIDTH)  # Impose axis limits based on config variables
        self.ax.set_ylim(TABLE_HEIGHT, 0)
        self.ax.set_aspect('equal')  # Set aspect of the axis
        self.ax.axis('off')  # Turn off visability of the axis
        self.draw_elements()  # Draw elements function is called to draw the element boxes
        self.mpl_connect('pick_event', self.on_pick)  # Connect the pick event to the on pick function

    def draw_elements(self):  # Draw the element boxes
        # Function is used to draw the element boxes on the created canvas.
        # It has no input but does use the csv file to extract element aspects used in drawing

        for atomic_number, element in self.data.items():
            # iterate through the dictionary using key 'atomic_number' and value 'element'
            x, y = self.calculate_position(element)
            # coordinates of element boxes are determined by calling calculate_position function

            sub_category = element.get('Type')  # sub category is determined based on 'Type'
            background_color = category_colors.get(sub_category, 'white')  # Background color is assigned based on category, default : white if no match

            rect = Rectangle((x, y), ELEMENT_SIZE, ELEMENT_SIZE, fc=background_color, ec='black', lw=1)
            # element box rectangle is created
            self.ax.add_patch(rect)
            atomic_number_text = element['AtomicNumber']  # text labels for atomic number and symbol are created
            symbol_text = element['Symbol']

            atomic_number_font_size = 8  # Set font size for the atomic number
            symbol_font_size = 14  # Set font size for the element symbol

            self.ax.text(x + ELEMENT_SIZE / 2, y + ELEMENT_SIZE * 0.25, atomic_number_text,
                         # Positioning of text in element cell
                         ha='center', va='center', fontsize=atomic_number_font_size,
                         color='black')  # alignment, font and color
            self.ax.text(x + ELEMENT_SIZE / 2, y + ELEMENT_SIZE * 0.65, symbol_text,
                         # Positioning of text in element cell
                         ha='center', va='center', fontsize=symbol_font_size, color='black',
                         weight='bold')  # alignment, font and color

            rect.set_picker(True)  # Enable picking for the rectangle

        self.draw()  # update canvas to draw elements

    def on_pick(self, event):
        # This function handles the event when an element box is clicked.
        artist = event.artist
        element_index = self.ax.patches.index(artist) # identify clicked element
        element_data = list(self.data.values())[element_index] # assign element's data
        self.parent_instance.open_element_info(element_data) # call open_element_info function to open information window


    def calculate_position(self, element):
        # This function calculates the location of the element boxes based on the group and period from the data file
        # For Lathanides and Actinides the atomic number and a standard defined row are used
        atomic_number = int(element['AtomicNumber'])
        if 57 <= atomic_number <= 71:  # Lathanides
            group = atomic_number - 57 + 4  # x position is determined through atomic number as opposed to group from csv
            period = 8  # y position is set for the Lathanide group to be underneath the rest of the table
            spacing_y = SPACING * 1.25  # some extra spacing is applied 0.125 instead of 0.1 to distinguish these two rows from the rest of the table
        elif 89 <= atomic_number <= 103:  # Actinides
            group = atomic_number - 89 + 4
            period = 9
            spacing_y = SPACING * 1.25
        else:  # rest of the elements
            group = int(element['Group'])  # x position determined through group from csv
            period = int(element['Period'])  # y position determined through period from csv
            spacing_y = SPACING  # for the rest of the table y spacing is set as standard
        x = group * (ELEMENT_SIZE + SPACING) + MARGIN  # account for element box size, spacing and margin
        y = period * (ELEMENT_SIZE + spacing_y) + MARGIN
        return x, y
