# Made by Wessel Eikelboom (S2565196) for the Python assignment in the PiE course.
# Mechanical Engineering, Faculty of Engineering Technology, University of Twente

# Load periodic table data from CSV into a dictionary
from config import csv_file_path


def load_data():
    data = {}  # Create an empty dictionary
    with open(csv_file_path) as f:  # Open the csv file based on the path defined in the config file
        lines = f.read().splitlines()  # Read the file and split it into lines
        header = lines[0].split(',')  # Extract the header line and split different columns based on ',' separation
        for line in lines[1:]:  # Iterate through the rest of the lines
            elements = line.split(',')  # Again make columns based on ',' separation
            element_data = {header[i]: elements[i] for i in range(len(header))}  # Create dictionary element entry
            data[element_data['AtomicNumber']] = element_data  # Use atomic number as the key
    return data  # Return dictionary now containing the element information
