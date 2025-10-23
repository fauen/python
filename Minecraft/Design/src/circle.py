from PIL import Image, ImageDraw

def draw_pixelated_circle(radius, output_file="pixelated_circle.png"):
    # Create a blank image with a white background
    size = (radius * 2 + 10, radius * 2 + 10)  # Add padding
    image = Image.new("RGB", size, "white")
    draw = ImageDraw.Draw(image)

    # Draw a circle with a thick border to make it pixelated
    draw.ellipse(
        [(5, 5), (size[0] - 5, size[1] - 5)],
        outline="black",
        width=2  # Adjust for more/less pixelation
    )

    # Save the image
    image.save(output_file)
    print(f"Pixelated circle saved as {output_file}")

# Example usage
draw_pixelated_circle(radius=50)

