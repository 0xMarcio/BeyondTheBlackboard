import matplotlib.pyplot as plt

def calculate_image_properties(focal_length, object_distance):
    # Same function as before
    image_distance = 1 / (1 / focal_length - 1 / object_distance)
    magnification = -image_distance / object_distance
    if image_distance > 0:
        nature_of_image = "Real and Inverted"
    else:
        nature_of_image = "Virtual and Upright"
    return image_distance, magnification, nature_of_image

def draw_lens_diagram(focal_length, object_distance):
    image_distance, magnification, _ = calculate_image_properties(focal_length, object_distance)
    object_height = 2  # Arbitrary object height

    # Image height (using magnification)
    image_height = magnification * object_height

    # Plotting
    fig, ax = plt.subplots()
    ax.axhline(0, color='black')  # Principal axis

    # Lens
    ax.plot([0, 0], [-5, 5], color='blue', linewidth=2)  # Simple representation of a lens

    # Object
    ax.plot([object_distance, object_distance], [0, object_height], color='green', label='Object')
    
    # Image
    if image_distance > 0:
        # Real image
        ax.plot([image_distance, image_distance], [0, image_height], color='red', label='Image (Real)')
    else:
        # Virtual image
        ax.plot([image_distance, image_distance], [0, -image_height], color='purple', label='Image (Virtual)')

    # Focal points
    ax.plot([-focal_length, -focal_length], [-1, 1], 'o--', color='orange', label='Focal Point')
    ax.plot([focal_length, focal_length], [-1, 1], 'o--', color='orange')

    ax.set_xlim(min(-2*focal_length, object_distance-5), max(2*focal_length, image_distance+5))
    ax.set_ylim(-5, 5)
    ax.legend()
    ax.set_title("Lens Diagram")
    ax.set_xlabel("Distance")
    ax.set_ylabel("Height")
    ax.grid(True)

    plt.show()

# Example usage
focal_length = 10  # Focal length of the lens (in cm)
object_distance = 15  # Distance of the object from the lens (in cm)

# Draw lens diagram
draw_lens_diagram(focal_length, object_distance)
