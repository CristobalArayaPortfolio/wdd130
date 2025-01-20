import datetime
import math

def calculate_tire_volume(width, aspect_ratio, diameter):
    """Calculates the approximate volume of air inside a tire.

    Args:
      width: The width of the tire in millimeters.
      aspect_ratio: The aspect ratio of the tire.
      diameter: The diameter of the wheel in inches.

    Returns:
      The volume of air inside the tire in liters.
    """
    height = (aspect_ratio / 100) * width
    volume = (math.pi * (width ** 2) * height + 2540 * diameter) / 10000000000
    return volume

def append_to_file(filename, data):
    """Appends data to a text file.

    Args:
      filename: The name of the text file to append to.
      data: The data to append to the file.
    """
    with open(filename, "a") as file:
        file.write(data + "\n")

def main():
    # Get the current date.
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")

    # Read tire dimensions from the user
    width = float(input("Enter the width of the tire in millimeters (e.g., 205): "))
    aspect_ratio = float(input("Enter the aspect ratio of the tire (e.g., 60): "))
    diameter = float(input("Enter the diameter of the wheel in inches (e.g., 15): "))

    # Calculate the tire volume
    volume = calculate_tire_volume(width, aspect_ratio, diameter)

    # Output the result
    print(f"The volume of space inside the tire is approximately {volume:.6f} liters.")

    # Append data to the volumes.txt file
    data = f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}"
    append_to_file("volumes.txt", data)

if __name__ == "__main__":
    main()