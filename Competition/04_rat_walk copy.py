import math

# floor has rat sensors
# floor has two walls left and right
# front is open to outer floor
# back is open to the kitchen
# floor rectangular - height H width W
# 0<=x<=W 0<=y<=H

# N number of sensors
# Can detect circular area of radius R
# if rat detected at x, y rat is hit with anesthetic needle -> rat cannot move
# Rat can enter from any point on the outer floor
# Rat needs to go to the kitchen

# Input: 
# Give number of test cases T, wigth W, height H of the room
# for each test case give number of sensors N, radius R
# for each sensor give x, y coordinates
# 1 <= T <= 20
# 1 <= N <= 1000
#  1 <= R <= 5 x 108
# 1 <= H <= 109
# 1 <= W <= 109
# 1 <= Xi <= 109
# 1 <= Yi <= 109

# Output: CAN or CANNOT

# get input line
first_line = input()
T, W, H = first_line.split()
T = int(T)
W = int(W)
H = int(H)



rectangle = [(0, 0), (W, 0), (W, H), (0, H)]



def check_path(rectangle, circles, radius):
    intersecting_circles = [[0]*N for _ in range(N)]

    for i in range(len(circles)):
        for j in range(i + 1, len(circles)):
            if (i != j):
                x1, y1 = circles[i]
                x2, y2 = circles[j]
                r_to_r = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                if (r_to_r <= 2 * radius):
                    intersecting_circles[i][j] = 1
                    intersecting_circles[j][i] = 1
    # get intersecting circle groups
    circle_groups = []

    for circle in circles:
        circle_groups.append([circle])


    visited = [0]*N

    def dfs(node, group):
        visited[node] = 1
        group.append(node)
        for i in range(N):
            if intersecting_circles[node][i] == 1 and visited[i] == 0:
                dfs(i, group)

    for i in range(N):
        if visited[i] == 0:
            group = []
            dfs(i, group)
            circle_group = [circles[i] for i in group]
            circle_groups.append(circle_group)

    hugging_groups = []
    for group in circle_groups:
        left_hug = False
        right_hug = False
        for circle in group:
            x, y = circle
            if x <= radius:
                left_hug = True
            if x >= W - radius:
                right_hug = True
        if left_hug and right_hug:
            hugging_groups.append(group)

    if len(hugging_groups) > 0:
        return True
    else:
        return False


# get sensor coordinates
for test_case in range(T):
    second_line = input()
    N, R = second_line.split()
    N = int(N)
    R = int(R)

    radius = R

    x_coords = input()
    x_coords = x_coords.split()
    x_coords = [int(x) for x in x_coords]
    y_coords = input()
    y_coords = y_coords.split()
    y_coords = [int(y) for y in y_coords]
    coordinates = list(zip(x_coords, y_coords))
    circles = [(2, 2), (4, 4), (6, 6), (8, 8)]
    circles = coordinates
    # get intersecting circles
    # for each circle check if it intersects with any other circle\
    # create N by N array

    path_blocked = check_path(rectangle, circles, radius)
    if path_blocked:
        print("CAN'T")
    else:
        print("CAN")


