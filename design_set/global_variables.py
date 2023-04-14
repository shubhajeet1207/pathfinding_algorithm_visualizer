from design_set.button_design import Button

RED = (170, 119, 255)
GREEN = (0, 255, 0)
BLUE = (54, 47, 217)
YELLOW = (254, 255, 134)
WHITE = (236, 249, 255)
BLACK = (27, 36, 48)
ORANGE = (252, 41, 71)
PURPLE = (227, 132, 255)
LIGHT_BLUE = (255, 202, 200)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)
LIGHT_BUTTON = (176, 218, 255)
DARK_BUTTON = (65, 53, 67)


astar_string = ["A* Pathfinding Algorithm", "Weighted: Yes", "Guarantees shortest path: Yes", "Worst time "
                                                                                              "complexity: O("
                                                                                              "b^d)",
                "Worst space complexity: O(b^d)"]
bfs_string = ["Breadth First Search", "Weighted: No", "Guarantees shortest path: Yes", "Worst time complexity: "
                                                                                       "O(b^d)", "Worst space "
                                                                                                 "complexity: O("
                                                                                                 "b^d)"]
dfs_string = ["Depth First Search", "Weighted: No", "Guarantees shortest path: No", "Time complexity: O(b^d)",
              "Spacial complexity: O(b*d)"]

dijkstra_string = ["Dijkstra Pathfinding Algorithm", "Weighted: Yes", "Guarantees shortest path: Yes",
                   "Time complexity: O(E*logV)", "Spacial complexity: O(E*logV)"]

bidirectional_string = ["Bidirectional BFS", "Weighted -> Yes", "Guarantees shortest path -> No", "Time complexity -> "
                                                                                                  "O(b^(d/2))",
                        "Spacial complexity -> O(b^(d/2))"]

best_first_search_string = ["Best First Search", "Weighted -> No", "Guarantees shortest path -> No", "Time complexity "
                                                                                                     "-> O(b^d)",
                            "Spacial complexity -> Polynomial"]

time_string = [""]

WIDTH = 1200
HEIGHT = 750
ROWS = 50
GAP = 15

button_start = Button(825, 400, 150, 50, WHITE, DARK_BUTTON, "START")
button_reset = Button(975, 400, 150, 50, WHITE, DARK_BUTTON, "RESET GRID")
button_astar = Button(825, 550, 150, 50, WHITE, GREY, "A*")
button_bfs = Button(975, 550, 150, 50, WHITE, GREY, "BFS")
button_dijkstra = Button(975, 600, 150, 50, WHITE, GREY, "DIJKSTRA")
button_dfs = Button(825, 650, 150, 50, WHITE, GREY, "DFS")
button_bidirectional = Button(825, 600, 150, 50, WHITE, GREY, "BIDIRECTIONAL")
button_best_first_search = Button(975, 650, 150, 50, WHITE, GREY, "BEST FIRST SEARCH")
legend_start = Button(775, 275, 15, 15, GREEN, GREEN, " ")
legend_end = Button(900, 275, 15, 15, GREEN, GREEN, " ")
legend_obstacle = Button(1025, 275, 15, 15, BLACK, BLACK, " ")
