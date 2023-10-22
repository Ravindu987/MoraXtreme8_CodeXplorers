no_of_images = int(input())
from PIL import Image, ImageDraw
import numpy as np
import math

def draw(image, m, c):
    # Assuming you have your image data in a 2D list
    image_data = np.zeros((50, 50))

    # convert 0 to 255
    for i in range(len(image_data)):
        for j in range(len(image_data[i])):
            if image_data[i][j] == 0:
                image_data[i][j] = 255

    # Convert the image data to a PIL Image object
    image = Image.fromarray(np.uint8(image_data))

    # Create an ImageDraw object
    draw = ImageDraw.Draw(image)

    # Assuming you have the slope (m) and y-intercept (c) of the line

    # Calculate the start and end coordinates of the line
    start_coord = (0, 50 - c)
    end_coord = (50, 50 - (m*50 + c))

    # Draw the line on the image
    draw.line([start_coord, end_coord], fill=128)

    # Display the image
    image.show()

def get_lines(image, tolerance=0.25):
    height, width = 50, 50
    lines = []

    # Get edge pixels
    edge_pixels = [(x, y) for x in range(width) for y in [0, height - 1]] + [
        (x, y) for x in [0, width - 1] for y in range(height)
    ]

    for i in range(len(edge_pixels)):
        for j in range(i + 1, len(edge_pixels)):
            x1, y1 = edge_pixels[i]
            x2, y2 = edge_pixels[j]
            # Calculate the length of the line segment
            length = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            if x2 != x1 and length >= 25:  # Only consider lines with length >= 25
                m = (y2 - y1) / (x2 - x1)
                c = y1 - m * x1
                # Check if line is close to existing lines and not too close to the edges
                if not any(
                    abs(m - m_) < tolerance and abs(c - c_) < tolerance
                    for m_, c_ in lines
                ):
                    # Divide the image into two regions using the line
                    region1 = [(x,y) for x in range(width) for y in range(height) if y > m*x + c]
                    region2 = [(x,y) for x in range(width) for y in range(height) if y <= m*x + c]
                    # If the area of the smallest region is less than 8 percent of the larger region, exclude the line
                    if min(len(region1), len(region2)) / max(len(region1), len(region2)) >= 0.2:
                        lines.append((m, c))
    
    # save to a text file as a single line array to copy as a variable
    # change number of decimal places of m and c to 5
    # Convert each line to a string with 4 decimal places
    print(lines)
    lines_str = [(f"{m:.3f}", f"{c:.3f}") for m, c in lines]

    # Convert the list of strings to a single string
    lines_str = str(lines_str)

    # Remove quotes to make it valid Python syntax for float values
    lines_str = lines_str.replace("'", "")

    with open("lines.txt", "w") as f:
        f.write(lines_str)
        


    return lines

def get_regions(image, lines):
    percentage_differences = []
    height, width = 50, 50
    for m, c in lines:
        section1 = []
        section2 = []
        for x in range(width):
            for y in range(height):
                # Check which section the pixel belongs to
                if height - y > m * x + c:  # Reverse the y-coordinate here
                    section1.append(image[y][x])
                else:
                    section2.append(image[y][x])

        # Calculate the percentage of black pixels in each section
        black_percentage_section1 = (
            section1.count(1) / len(section1) * 100 if len(section1) != 0 else 0
        )
        black_percentage_section2 = (
            section2.count(1) / len(section2) * 100 if len(section2) != 0 else 0
        )

        # Calculate the difference in percentage of black pixels
        percentage_difference = abs(
            black_percentage_section1 - black_percentage_section2
        )
        percentage_differences.append(percentage_difference)

    # print max difference
    max_difference = max(percentage_differences)
    # print m,c of line with max difference
    max_difference_index = percentage_differences.index(max_difference)
    m, c = lines[max_difference_index]
    draw(image, m,c)
    print(max_difference)
    return m, c, max_difference



# np array of images
images = []
lines = get_lines([[0]*50 for _ in range(50)])
for image in range(no_of_images):
    image_array = []
    empty_line = input()

    for row in range(50):
        # seperate each row into a list of characters and convert to np array
        row = input()
        row = list(row)
        row = [int(x) for x in row]
        image_array.append(row)

    m, c, max_difference = get_regions(image_array, lines)
    if max_difference < 25:
        print("x")
    else:
        print(m, c)