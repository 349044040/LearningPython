import curses
def window(stdscr):
  sh,sw = stdscr.getmaxyx()
  msg = "curses hellotype esc to exit" 
  stdscr.addstr(sh // 2, sw //2 - len(msg) // 2, msg)

  stdscr.getch()
  stdscr.addstr(sh-1, 0, str(ord('a')))
  stdscr.addstr(sh-5, 0, chr(120))

  while True:
    userkey = stdscr.getch()
    stdscr.addstr(userkey)
    stdscr.addstr(str(ord(userkey)))
    if userkey ==27:
      break

curses.wrapper(window)