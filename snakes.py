import random
import curses
import time

name = str(input("Enter Player's Name: "))
s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

snk_x = sw/4
snk_y = sh/2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

food = [sh/2, sw/2]
w.addch(int(food[0]), int(food[1]), curses.ACS_PI)
w.addstr(0, 50, "saurabh's python chase", curses.A_STANDOUT)
w.addstr(0, 0, "Player : " + str(name), curses.A_BLINK)

key = curses.KEY_RIGHT
x = 10

while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    if snake[0][0] in [0, sh] or snake[0][1]  in [0, sw] or snake[0] in snake[1:]:
        curses.newpad(20,50).refresh(50, 50, 10, 10, 20, 75)
        #w.addstr(50, 50, "You Lose!", curses.A_STANDOUT)        
        print("Total Score: " + str(x))
        curses.napms(2000)
        curses.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
        x = x + 10
    else:
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]), ' ')        

    w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)
    w.addstr(0, 100, "Score: " + str(x), curses.COLOR_BLUE)