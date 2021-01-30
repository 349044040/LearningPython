import curses
def window(stdscr):
  curses.start_colors
curses.use_default_colors
for i in range(0, curses.colors):
  curses.init_pair(i+1, i, -1)
  stdscr.addstr(str(i+1), curses.color-pair(i+1))
  stdscr.getch():
curse.wrapper(window)

