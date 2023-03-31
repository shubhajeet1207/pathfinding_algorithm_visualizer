import sys
import pygame

sys.path.append(".")

from design_set.global_variables import *
from grid.grids import make_grid, draw, get_clicked_pos

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pathfinding Algorithm Visualizer")
pygame.init()


def main(win, width):
    grid = make_grid(ROWS, width)
    all_fonts = pygame.font.get_fonts()

    start = None
    end = None
    ALG_ID = 0
    start_time = 0
    elapsed_time = 0
    number_of_visited_nodes = 0

    run = True
    while run:

        draw(win, grid, ROWS, width, ALG_ID, elapsed_time)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if button_astar.check() == True and ALG_ID != 0:
                button_astar.background_color = LIGHT_BUTTON
            else:
                button_astar.background_color = DARK_BUTTON

            if button_bfs.check() == True and ALG_ID != 1:
                button_bfs.background_color = LIGHT_BUTTON
            else:
                button_bfs.background_color = DARK_BUTTON

            if button_dfs.check() == True and ALG_ID != 2:
                button_dfs.background_color = LIGHT_BUTTON
            else:
                button_dfs.background_color = DARK_BUTTON

            if button_dijkstra.check() == True and ALG_ID != 3:
                button_dijkstra.background_color = LIGHT_BUTTON
            else:
                button_dijkstra.background_color = DARK_BUTTON

            if button_reset.check():
                button_reset.background_color = LIGHT_BUTTON
            else:
                button_reset.background_color = DARK_BUTTON

            if pygame.mouse.get_pressed()[0]:  # LEFT SCREEN
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                if row < ROWS and col < ROWS:
                    spot = grid[row][col]
                    if not start and spot != end:
                        start = spot
                        start.isStart = 1
                        start.make_start()

                    elif not end and spot != start:
                        end = spot
                        end.isEnd = 1
                        end.make_end()

                    elif spot != end and spot != start:
                        spot.make_barrier()
                elif button_reset.check():
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)
                    start_time = 0
                    elapsed_time = 0
                    number_of_visited_nodes = 0

                if button_start.check() == True and start and end:

                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)

                    temp_start = start
                    temp_end = end
                    start_time = 0
                    elapsed_time = 0
                    temp_start.make_start()
                    temp_end.make_end()

                if button_astar.check():
                    button_astar.background_color = LIGHT_BLUE
                    ALG_ID = 0
                else:
                    button_astar.background_color = DARK_BUTTON

                if button_bfs.check():
                    button_bfs.background_color = LIGHT_BLUE
                    ALG_ID = 1
                else:
                    button_bfs.background_color = DARK_BUTTON

                if button_dfs.check():
                    button_dfs.background_color = LIGHT_BLUE
                    ALG_ID = 2
                else:
                    button_dfs.background_color = DARK_BUTTON

                if button_dijkstra.check():
                    button_dijkstra.background_color = LIGHT_BLUE
                    ALG_ID = 3
                else:
                    button_dijkstra.background_color = DARK_BUTTON

            elif pygame.mouse.get_pressed()[2]:  # RIGHT SCREEN
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                if row < ROWS and col < ROWS:
                    spot = grid[row][col]
                    spot.reset()
                    if spot == start:
                        spot.isStart = -1
                        start = None
                    elif spot == end:
                        spot.isEnd = -1
                        end = None

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()


main(WIN, WIDTH)
