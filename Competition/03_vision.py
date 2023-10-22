no_of_images = int(input())


def get_lines(image, tolerance=1):
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
            if x2 != x1:
                m = (y2 - y1) / (x2 - x1)
                c = y1 - m * x1
                # Check if line is close to existing lines
                if not any(
                    abs(m - m_) < tolerance and abs(c - c_) < tolerance
                    for m_, c_ in lines
                ):
                    lines.append((m, c))

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
                if y > m * x + c:
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

        # print(f"Line: y = {m}x + {c}")
        # print(f"Black percentage in section 1: {black_percentage_section1}%")
        # print(f"Black percentage in section 2: {black_percentage_section2}%")
    # print max difference
    max_difference = max(percentage_differences)
    # print(f"Max difference: {max_difference}")
    # print m,c of line with max difference
    max_difference_index = percentage_differences.index(max_difference)
    m, c = lines[max_difference_index]
    # print(f"Line: y = {m}x + {c}")
    return m, c


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
    # print(image_array)

    # # convert 1 to 255
    # image_array[image_array == 1] = 255

    # # PIL image
    # image = Image.fromarray(image_array)
    # image.show()
    # print(f"Total unique lines: {len(lines)}")
    m, c = get_regions(image_array, lines)
    print(m, c)
