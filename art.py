import pygame
import math

color_selection = [(153, 0, 0), (51, 0, 0), (160, 160, 160), (255, 255, 51)]


def main(triangle, circle, rectangle, right_triangle, square, equilateral_triangle, rhombus):
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []

    while True:

        pressed = pygame.key.get_pressed()

        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():

            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_c:
                    points.clear()
                if event.key == pygame.K_t:
                    triangle = True
                    circle = False
                    rectangle = False
                    right_triangle = False
                    square = False
                    equilateral_triangle = False
                    rhombus = False
                if event.key == pygame.K_o:
                    triangle = False
                    circle = True
                    rectangle = False
                    right_triangle = False
                    square = False
                    equilateral_triangle = False
                    rhombus = False
                if event.key == pygame.K_p:
                    triangle = False
                    circle = False
                    rectangle = True
                    right_triangle = False
                    square = False
                    equilateral_triangle = False
                    rhombus = False
                if event.key == pygame.K_i:
                    triangle = False
                    circle = False
                    rectangle = False
                    right_triangle = True
                    square = False
                    equilateral_triangle = False
                    rhombus = False
                if event.key == pygame.K_o:
                    triangle = False
                    circle = False
                    rectangle = False
                    right_triangle = False
                    square = True
                    equilateral_triangle = False
                    rhombus = False
                if event.key == pygame.K_k:
                    triangle = False
                    circle = False
                    rectangle = False
                    right_triangle = False
                    square = False
                    equilateral_triangle = True
                    rhombus = False
                if event.key == pygame.K_l:
                    triangle = False
                    circle = False
                    rectangle = False
                    right_triangle = False
                    square = False
                    equilateral_triangle = False
                    rhombus = True
                # determine if a letter key was pressed
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_1:
                    mode = 'yellow'

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # left click grows radius
                    radius = min(200, radius + 1)
                elif event.button == 3:  # right click shrinks radius
                    radius = max(1, radius - 1)

            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list
                position = event.pos
                points = points + [position]
                points = points[-256:]

        screen.fill((0, 0, 0))

        # draw all points
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode, triangle, circle, rectangle,
                            right_triangle, square, equilateral_triangle, rhombus)
            i += 1

        pygame.display.flip()

        clock.tick(60)


def drawLineBetween(screen, index, start, end, width, color_mode, triangle, circle, rectangle, right_triangle,
                    square, equilateral_triangle, rhombus):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    elif color_mode == 'yellow':
        color = (c1, c2, 0)
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        if circle == True:
            pygame.draw.circle(screen, color, (x, y), width)
        elif triangle == True:
            vertices = [(x, y), (x + width, y + width), (x - width, y + width)]
            pygame.draw.polygon(screen, color, vertices)
        elif rectangle:
            rect_width = 5  # Border width
            rect_x, rect_y = x - 100, y - 75  # Calculate position based on mouse position
            rect_size = (200, 150)
            pygame.draw.rect(screen, color, pygame.Rect(rect_x, rect_y, rect_size[0], rect_size[1]))  # Fill
            pygame.draw.rect(screen, color, pygame.Rect(rect_x, rect_y, rect_size[0], rect_size[1]),
                             rect_width)  # Border

        elif right_triangle:
            vertices = [(x + 50, y + 50), (x + 50, y + 150), (x + 150, y + 150)]
            pygame.draw.polygon(screen, color, vertices)
        elif square:
            pygame.draw.rect(screen, color, (x, y, 20, 20))

        elif equilateral_triangle:
            center_x, center_y = 320, 240
            side_length = 200

            # Calculate the vertices of the equilateral triangle
            angle = math.radians(30)  # 60 degrees in radians
            x1 = x + center_x - side_length // 2
            y1 = y + center_y + int(math.sqrt(3) * side_length / 2)
            x2 = x + center_x
            y2 = y + center_y - int(math.sqrt(3) * side_length / 2)
            x3 = x + center_x + side_length // 2
            y3 = y + y1
            pygame.draw.polygon(screen, color, [(x1, y1), (x2, y2), (x3, y3)])
        elif rhombus:
            center_x, center_y = 320, 240
            side_length = 200
            vertices = [
                (x + center_x - side_length // 2, y + center_y),
                (x + center_x, y + center_y - side_length // 2),
                (x + center_x + side_length // 2, y + center_y),
                (x + center_x, y + center_y + side_length // 2)
            ]
            pygame.draw.polygon(screen, color, vertices)


main(triangle=False, circle=True, rectangle=False, right_triangle=False, square=False, equilateral_triangle=False,
     rhombus=False)
