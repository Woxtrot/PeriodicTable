# Made by Wessel Eikelboom (S2565196) for the Python assignment in the PiE course.
# Mechanical Engineering, Faculty of Engineering Technology, University of Twente

# This file contains some configuration constants

# Constants for positioning and sizing
TABLE_WIDTH = 18 * (4 / 3)
TABLE_HEIGHT = 9 * (4 / 3)
ELEMENT_SIZE = 1.05
MARGIN = 0.1
SPACING = 0.1
WINDOW_WIDTH = TABLE_WIDTH * ELEMENT_SIZE * 60
WINDOW_HEIGHT = TABLE_HEIGHT * ELEMENT_SIZE * 60

# Defining csv file path
csv_file_path = 'FIXED_periodic_table_of_elements.csv'

# Dictionary with colors to distinguish element categories
category_colors = {
    'Nonmetal': '#9fc97d',
    'Alkali Metal': '#d01f2f',
    'Alkaline Earth Metal': '#f8a81d',
    'Transition Metal': '#99bfe6',
    'Halogen': '#26823d',
    'Noble Gas': '#fcb4cc',
    'Transactinide': '#116f9e',
    'Lanthanide': '#1798d9',
    'Actinide': '#50efb9',
    'Metalloid': '#ffce07',
    'Metal': '#bf96e2'
}
