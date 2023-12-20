
import cv2
import numpy as np
import winsound
import time
import math

# Initialize the simulation window
window_width = 800
window_height = 600
simulation_window = np.zeros((window_height, window_width, 3), dtype=np.uint8)

# Initialize car and parking spot positions
car_x = 100
car_y = 300
parking_spot_x = 600
parking_spot_y = 300

# Set car movement speed
car_speed = 5

# Set the range for beep sound (in pixels)
beep_range = 50

# Load car engine sound
def play_car_engine_sound():
    winsound.Beep(1000, 500)  # Adjust frequency and duration as needed

# Calculate the distance between two points (car and parking spot)
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Main simulation loop
while True:
    # Clear the simulation window
    simulation_window.fill(0)

    # Draw the parking spot
    cv2.rectangle(simulation_window, (parking_spot_x - 20, parking_spot_y - 50),
                  (parking_spot_x + 20, parking_spot_y + 50), (0, 255, 0), -1)

    # Draw the car
    cv2.rectangle(simulation_window, (car_x - 20, car_y - 30), (car_x + 20, car_y + 30), (0, 0, 255), -1)

    # Display the simulation window
    cv2.imshow('Car Parking Simulator', simulation_window)

    # Calculate the distance between the car and the parking spot
    distance = calculate_distance(car_x, car_y, parking_spot_x, parking_spot_y)

    # Check if the car is within the specified range for beep sound
    if distance <= beep_range:
        play_car_engine_sound()
        time.sleep(0.5)  # Adjust the sleep duration for the beep interval

    # Check for keyboard input to move the car
    key = cv2.waitKey(1)
    if key == ord('a'):
        car_x -= car_speed
    elif key == ord('d'):
        car_x += car_speed
    elif key == ord('w'):
        car_y -= car_speed
    elif key == ord('s'):
        car_y += car_speed

    # If 'q' is pressed, exit the simulation
    if key == ord('q'):
        break

# Release the simulation window
cv2.destroyAllWindows()