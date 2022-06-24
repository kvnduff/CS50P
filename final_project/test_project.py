'''
Unit tests for tournament.py
The current project was developed using the curses library and most user input
was collected using getch(). As such, unit tests were conducted by executing
the functions and testing the window output using instr().
'''

import curses
from curses import wrapper
import textwrap
import pytest
import tournament
import strings


# Embed program within padded window
scr = curses.initscr()
win = curses.newwin(100, 200, 1, 2)
curses.start_color()


# Test title screen output
# strings.title(win): prints title screen
def test_title_print():
    strings.title(win)
    assert win.instr(0, 0, 15) == b'WELCOME TO THE '     # 0 line of title
    assert win.instr(14, 0, 15) == b'||/////////////'    # 14 line of title
    assert win.instr(27, 0, 15) == b'Type "Enter" to'    # 27 line of title


# Unsure how to unit test curses functions. No sufficient online documentation.
# Contacted course admins (EdX) but no reply.
