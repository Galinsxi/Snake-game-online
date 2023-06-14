import curses
import random
from add_score import add_score

def play_snake_game(stdscr,username):
    # Clear the screen
    stdscr.clear()

    # Setup
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    # Initial snake position and direction
    snake_x = curses.COLS // 2
    snake_y = curses.LINES // 2
    snake = [
        [snake_y, snake_x],
        [snake_y, snake_x - 1],
        [snake_y, snake_x - 2]
    ]
    direction = curses.KEY_RIGHT

    # Initial score
    score = 0

    # Generate initial food
    food = [random.randint(1, curses.LINES - 2), random.randint(1, curses.COLS - 2)]
    stdscr.addch(food[0], food[1], curses.ACS_PI) # add food to screen

    # Game loop
    while True:
        # Get user input
        key = stdscr.getch()

        # Change direction based on user input
        if (
            (key == curses.KEY_UP and direction != curses.KEY_DOWN) or
            (key == curses.KEY_DOWN and direction != curses.KEY_UP) or
            (key == curses.KEY_LEFT and direction != curses.KEY_RIGHT) or
            (key == curses.KEY_RIGHT and direction != curses.KEY_LEFT)
        ):
            direction = key

        # Calculate new head position
        head = snake[0]
        if direction == curses.KEY_UP:
            new_head = [head[0] - 1, head[1]]
        elif direction == curses.KEY_DOWN:
            new_head = [head[0] + 1, head[1]]
        elif direction == curses.KEY_LEFT:
            new_head = [head[0], head[1] - 1]
        elif direction == curses.KEY_RIGHT:
            new_head = [head[0], head[1] + 1]

        # Insert new head into snake
        snake.insert(0, new_head)

        # Check if snake eats the food
        if snake[0] == food:
            # Generate new food
            food = None
            while food is None:
                nf = [
                    random.randint(1, curses.LINES - 2),
                    random.randint(1, curses.COLS - 2)
                ]
                food = nf if nf not in snake else None
            stdscr.addch(food[0], food[1], curses.ACS_PI)
            score += 100
        else:
            # Remove tail segment
            stdscr.addch(snake[-1][0], snake[-1][1], ' ')
            snake.pop()

        # Check if snake hits the wall or itself
        if (
            snake[0][0] in [0, curses.LINES - 1] or
            snake[0][1] in [0, curses.COLS - 1] or
            snake[0] in snake[1:]
        ):
            break

        # Draw snake
        stdscr.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)

        # Refresh the screen
        stdscr.refresh()

    # Game over message
    stdscr.clear()
    stdscr.addstr(curses.LINES // 2, (curses.COLS - 11) // 2, "Game Over, "+username+"!")
    stdscr.addstr(curses.LINES // 2 + 1, (curses.COLS - len("Score: ")) // 2, "Score: {}".format(score))
    add_score(username, score) 
    stdscr.refresh()

    # Ask to play again
    stdscr.addstr(curses.LINES - 1, 0, "Play again? (y/n)")
    stdscr.refresh()
    while True:
        key = stdscr.getch()
        if key == ord('y'):
            play_snake_game(stdscr,username)
        elif key == ord('n'):
            break

def snake(username):
    # Run the game
    curses.wrapper(play_snake_game,username)
