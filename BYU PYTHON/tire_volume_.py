import math
from datetime import datetime

def calculate_tire_volume(width, aspect_ratio, diameter):
    """
    Calculate the volume of a tire using the formula:
    Volume = π * width^2 * (aspect_ratio / 100 * width + diameter) / 1000000
    This returns the volume in cubic meters.
    """
    volume = (math.pi * (width ** 2) * (width * (aspect_ratio / 100) + diameter)) / 1000000  # volume in cubic meters
    return volume

def main():
    # prompt user for tire dimensions
    width = float(input("Enter the width of the tire in mm: "))  # Tire width in millimeters
    aspect_ratio = float(input("Enter the aspect ratio of the tire (as a percentage): "))  # Aspect ratio
    diameter = float(input("Enter the diameter of the wheel in inches: "))  # Wheel diameter in inches

    # calculate the volume of the tire
    volume = calculate_tire_volume(width, aspect_ratio, diameter)

    # Get the current date
    current_date = datetime.now().date()

    # open the file in append mode
    with open("volumes.txt", "a") as file:
        # Append the data to the file
        file.write(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {round(volume, 2)}\n")

    print("Tire volume data has been appended to volumes.txt.")

if __name__ == "__main__":
    main()