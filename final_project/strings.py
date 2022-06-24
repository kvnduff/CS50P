'''
Print strings for tournament.py
'''

import os
import curses
import textwrap


# Embed program within padded window
scr = curses.initscr()
win = curses.newwin(100, 200, 1, 2)


def title(win):
    ''' Print title screen. '''

    YELLOW, RED, BLUE, GREEN = init_colors()
    win.clear()
    curses.curs_set(0)
    win.addstr(0, 0, 'WELCOME TO THE')
    win.addstr(1, 0, 'PICKLEBALL TOURNAMENT CALCULATOR')
    win.addstr(2, 0, '********************************', RED)
    win.addstr(0, 52, '***o', YELLOW)
    win.addstr(1, 50, '********', YELLOW)
    win.addstr(2, 49, '**o**o****', YELLOW)
    win.addstr(3, 49, '*******o**', YELLOW)
    win.addstr(4, 50, '*o**o***', YELLOW)
    win.addstr(5, 52, '****', YELLOW)
    win.addstr(13, 1, '////////////////////////||')
    win.addstr(14, 0, '||///////////////////////||')
    win.addstr(15, 1, '\\///////////////////////||')
    win.addstr(7, 42, '/#######################\\', BLUE)
    win.addstr(8, 36, '/#################################\\', BLUE)
    win.addstr(9, 34, '/#####################################\\', BLUE)
    win.addstr(10, 32, '/########################################\\', BLUE)
    win.addstr(11, 30, '/###########################################', BLUE)
    win.addstr(12, 28, '/#############################################', BLUE)
    win.addstr(13, 27, '###############################################', BLUE)
    win.addstr(14, 27, '###############################################', BLUE)
    win.addstr(15, 27, '###############################################', BLUE)
    win.addstr(16, 28, '\\#############################################', BLUE)
    win.addstr(17, 30, '\\###########################################', BLUE)
    win.addstr(18, 32, '\\########################################/', BLUE)
    win.addstr(19, 34, '\\#####################################/', BLUE)
    win.addstr(20, 36, '\\#################################/', BLUE)
    win.addstr(21, 42, '\\#######################/', BLUE)
    text = textwrap.fill('''The pickleball tournament calculator is a tool '''
                         '''that generates schedules for different types of '''
                         '''pickleball tournaments. To receive your own '''
                         '''custom, pickleball tournament schedule you'll '''
                         '''first need to answer a few questions.''',
                         width=80)
    win.addstr(23, 0, text)
    win.addstr(27, 0, 'Type "Enter" to continue or "h" for help.')
    win.addstr(27, 6, 'Enter', GREEN)
    win.addstr(27, 29, 'h', GREEN)
    win.refresh()


def format_question(win):
    ''' Print tournament format question. '''

    YELLOW, RED, BLUE, GREEN = init_colors()
    win.clear()
    win.addstr(0, 0, '''What is the format of the tournament you are '''
               '''organizing?''')
    win.addstr(1, 2, 'Type "1" for a fixed-partner round robin tournament.')
    win.addstr(1, 8, '1', GREEN)
    win.addstr(2, 2, 'Type "2" for a rotating-partner round robin tournament.')
    win.addstr(2, 8, '2', GREEN)
    win.refresh()


def format_fixed(win):
    ''' Print tournament fixed format. '''

    YELLOW, RED, BLUE, GREEN = init_colors()
    win.addstr(4, 2, 'You chose a fixed-partner round robin tournament.')
    win.refresh()


def format_rotating(win):
    ''' Print tournament rotating format. '''

    YELLOW, RED, BLUE, GREEN = init_colors()
    win.addstr(4, 2, 'You chose a rotating-partner round robin tournament.')
    win.refresh()


def number_question_fixed(win):
    ''' Print tournament number question for fixed format. '''

    YELLOW, RED, BLUE, GREEN = init_colors()
    curses.curs_set(1)
    win.addstr(0, 0, 'How many teams will be participating?')
    win.addstr(1, 2, 'Type a number between "3" and "26" and press "Enter".')
    win.addstr(1, 25, '3', GREEN)
    win.addstr(1, 33, '26', GREEN)
    win.addstr(1, 48, 'Enter', GREEN)
    win.addstr(2, 2, '')
    win.refresh()


def number_question_rotating(win):
    ''' Print tournament number question for rotating format. '''

    YELLOW, RED, BLUE, GREEN = init_colors()
    curses.curs_set(1)
    win.addstr(0, 0, 'How many players will be participating?')
    win.addstr(1, 2, 'Type a number between "4" and "26" and press "Enter".')
    win.addstr(1, 25, '4', GREEN)
    win.addstr(1, 33, '26', GREEN)
    win.addstr(1, 48, 'Enter', GREEN)
    win.addstr(2, 2, '')
    win.refresh()


def number_fixed(win, number):
    ''' Print tournament number for fixed format. '''

    YELLOW, RED, BLUE, GREEN = init_colors()
    win.addstr(4, 2, f'You chose {number} teams.')


def number_rotating(win, number):
    ''' Print tournament number for rotating format. '''

    YELLOW, RED, BLUE, GREEN = init_colors()
    win.addstr(4, 2, f'You chose {number} players.')


def number_error_fixed(win):
    ''' Print tournament number error for fixed format. '''

    YELLOW, RED, BLUE, GREEN = init_colors()
    win.addstr(4, 2, '''ERROR: Invalid input, number of teams must be '''
               '''between 3 and 26.''')
    win.addstr(5, 2, 'Type "Enter" to try again.')
    win.addstr(5, 8, 'Enter', GREEN)
    win.addstr(4, 2, 'ERROR', RED)
    win.refresh()
    input()


def number_error_rotating(win):
    ''' Print tournament number error for rotating format. '''

    YELLOW, RED, BLUE, GREEN = init_colors()
    win.addstr(4, 2, '''ERROR: Invalid input, number of players must be '''
               '''between 4 and 26.''')
    win.addstr(5, 2, 'Type "Enter" to try again.')
    win.addstr(5, 8, 'Enter', GREEN)
    win.addstr(4, 2, 'ERROR', RED)
    win.refresh()
    input()


def menu(win, format, number):
    ''' Print menu options. '''

    YELLOW, RED, BLUE, GREEN = init_colors()
    win.clear()
    format_str = 'fixed' if format == 1 else 'rotating'
    number_str = 'team' if format == 1 else 'player'
    win.addstr(0, 0, f'''You have selected a {number} {number_str} '''
               f'''{format_str}-partner round robin tournament.''')
    win.addstr(1, 2, '''Type "1" to print your tournament schedule to the '''
               '''screen.''')
    win.addstr(1, 8, '1', GREEN)
    win.addstr(2, 2, 'Type "2" to save your tournament schedule to a file.')
    win.addstr(2, 8, '2', GREEN)
    win.addstr(3, 2, 'Type "3" to modify your tournament settings.')
    win.addstr(3, 8, '3', GREEN)
    win.addstr(4, 2, 'Type "4" for help.')
    win.addstr(4, 8, '4', GREEN)
    win.addstr(5, 2, 'Type "5" to quit.')
    win.addstr(5, 8, '5', GREEN)
    win.refresh()


def width(win, action):
    ''' Print table width options. '''

    YELLOW, RED, BLUE, GREEN = init_colors()
    win.clear()
    win.addstr(0, 0, f'''Which tournament schedule format would you like to '''
               f'''{action}?''')
    win.addstr(1, 2, f'Type "1" to {action} in narrow format.')
    win.addstr(1, 8, '1', GREEN)
    win.addstr(2, 2, f'Type "2" to {action} in wide format.')
    win.addstr(2, 8, '2', GREEN)
    win.addstr(3, 2, f'Type "3" to {action} in both narrow and wide formats.')
    win.addstr(3, 8, '3', GREEN)
    win.refresh()


def path_onewidth(win):
    ''' Print path to save file if one width selected. '''

    YELLOW, RED, BLUE, GREEN = init_colors()
    curses.curs_set(1)
    win.addstr(5, 2, '''Please specify the path you would like to save your '''
               '''schedule.''')


def path_twowidth(win):
    ''' Print path to save files if two widths selected. '''

    YELLOW, RED, BLUE, GREEN = init_colors()
    curses.curs_set(1)
    win.addstr(5, 2, '''Please specify the path you would like to save your '''
               '''schedules.''')


def path_error(win):
    ''' Print path to save files if two widths selected. '''

    YELLOW, RED, BLUE, GREEN = init_colors()
    ycoord, xcoord = win.getyx()
    win.addstr(ycoord + 1, xcoord + 2, 'ERROR', RED)
    win.addstr(': Invalid path, please type a path that exists. Type ')
    win.addstr('"Enter" ', GREEN)
    win.addstr('to try again.')
    win.refresh()
    input()
    ycoord, xcoord = win.getyx()
    win.addstr(ycoord, 2, '''                                         '''
               '''                                             ''')
    win.refresh()


def file_narrow(win):
    ''' Print confirmation of narrow width file generation. '''

    YELLOW, RED, BLUE, GREEN = init_colors()
    win.addstr(8, 2, '''Your tournament schedule (narrow format) has been '''
               '''saved!''')
    win.addstr(10, 2, 'Type "Enter" to continue.')
    win.addstr(10, 8, 'Enter', GREEN)
    win.refresh()
    input()


def file_wide(win):
    ''' Print confirmation of wide width file generation. '''

    YELLOW, RED, BLUE, GREEN = init_colors()
    win.addstr(8, 2, '''Your tournament schedule (wide format) has been '''
               '''saved!''')
    win.addstr(10, 2, 'Type "Enter" to continue.')
    win.addstr(10, 8, 'Enter', GREEN)
    win.refresh()
    input()


def file_both(win):
    ''' Print confirmation of both width file generation. '''

    YELLOW, RED, BLUE, GREEN = init_colors()
    win.addstr(8, 2, '''Your tournament schedule (narrow and wide formats) '''
               '''have been saved!''')
    win.addstr(10, 2, 'Type "Enter" to continue.')
    win.addstr(10, 8, 'Enter', GREEN)
    win.refresh()
    input()


def screen_narrow(win, number, table, pages, lines):
    ''' Print narrow width table to screen. '''

    YELLOW, RED, BLUE, GREEN = init_colors()
    for page in range(pages):

        # Print title
        win.clear()
        format_str = 'FIXED' if format == 1 else 'ROTATING'
        number_str = 'TEAMS' if format == 1 else 'PLAYERS'
        win.addstr(0, 0, f'''{format_str}-PARTNER ROUND ROBIN ({number} '''
                   f'''{number_str}) ({page + 1}/{pages})''')

        # Print header
        win.addstr(2, 0, '╒═════════╤═════════╤═════════╤═════════╕')
        win.addstr(3, 0, '│  GAME   │  ROUND  │  COURT  │  TEAMS  │')
        win.addstr(4, 0, '╞═════════╪═════════╪═════════╪═════════╡')

        # Print body
        body = table[1:]
        start = page * lines
        stop = ((page + 1) * lines)
        for i, row in enumerate(body[start:stop]):
            win.addstr((i * 2) + 5, 0, '│')
            for j, cell in enumerate(row):
                if len(cell) == 1:
                    win.addstr((i * 2) + 5, 1 + (j * 10), f'    {cell}    │')
                if len(cell) == 2:
                    win.addstr((i * 2) + 5, 1 + (j * 10), f'   {cell}    │')
                if len(cell) == 3:
                    win.addstr((i * 2) + 5, 1 + (j * 10), f'   {cell}   │')
                if len(cell) == 4:
                    win.addstr((i * 2) + 5, 1 + (j * 10), f'  {cell}   │')
                if len(cell) == 5:
                    win.addstr((i * 2) + 5, 1 + (j * 10), f'  {cell}  │')
                if len(cell) == 6:
                    win.addstr((i * 2) + 5, 1 + (j * 10), f' {cell}  │')
                if len(cell) == 7:
                    win.addstr((i * 2) + 5, 1 + (j * 10), f' {cell} │')
            if i == lines - 1 or body[-1] == row:
                win.addstr((i * 2) + 6, 0, '''└─────────┴─────────┴─────────'''
                           '''┴─────────┘''')
            else:
                win.addstr((i * 2) + 6, 0, '├─────────┼─────────┼─────────'''
                           '''┼─────────┤''')

        # Prompt to continue
        ycoord, _ = win.getyx()
        win.addstr((ycoord + 2), 0, 'Type "Enter" to continue')
        win.addstr((ycoord + 2), 6, 'Enter', GREEN)
        win.refresh()
        input()


def screen_wide(win, format, number, table, pages, lines):
    ''' Print wide width table to screen. '''

    YELLOW, RED, BLUE, GREEN = init_colors()
    for page in range(pages):

        # Print title
        win.clear()
        format_str = 'FIXED' if format == 1 else 'ROTATING'
        number_str = 'TEAMS' if format == 1 else 'PLAYERS'
        win.addstr(0, 0, f'''{format_str}-PARTNER ROUND ROBIN ({number} '''
                   f'''{number_str}) ({page + 1}/{pages})''')

        # Print header
        header = table[0]
        for i in range(3):
            for cell in enumerate(header):

                # First row
                if i == 0:
                    win.addstr(2, 0, '╒═════════╤')
                    for _ in range(len(header) - 2):
                        if format == 1:
                            win.addstr('══════╤')
                        else:
                            win.addstr('═════════╤')
                    if format == 1:
                        win.addstr('══════╕')
                    else:
                        win.addstr('═════════╕')

                # Second row
                if i == 1:
                    win.addstr(3, 0, '│  ROUND  │')
                    for k in range(len(header) - 1):
                        if k < len(header) - 2:
                            if format == 1:
                                if k < 9:
                                    win.addstr(f'  C{k + 1}  │')
                                else:
                                    win.addstr(f' C{k + 1}  │')
                            if format == 2:
                                if k < 9:
                                    win.addstr(f'   C{k + 1}    │')
                                else:
                                    win.addstr(f'   C{k + 1}   │')
                        if k == len(header) - 2:    # len-2=3, 3
                            if format == 1:
                                if number % 2 == 0:
                                    if k < 9:
                                        win.addstr(f'  C{k + 1}  │')
                                    else:
                                        win.addstr(f' C{k + 1}  │')
                                else:
                                    win.addstr(' BYE  │')
                            if format == 2:
                                if number % 4 != 1:
                                    if k < 9:
                                        win.addstr(f'   C{k + 1}    │')
                                    else:
                                        win.addstr(f'   C{k + 1}   │')
                                else:
                                    win.addstr('   BYE   │')

                # Third row
                if i == 2:
                    win.addstr(4, 0, '╞═════════╪')
                    for _ in range(len(header) - 2):
                        if format == 1:
                            win.addstr('══════╪')
                        else:
                            win.addstr('═════════╪')
                    if format == 1:
                        win.addstr('══════╡')
                    else:
                        win.addstr('═════════╡')

        # Print body
        body = table[1:]
        start = page * lines
        stop = ((page + 1) * lines)
        for i, row in enumerate(body[start:stop]):
            for j, cell in enumerate(row):

                # Within row
                if j == 0:
                    if len(cell) == 1:
                        win.addstr((i * 2) + 5, 0, f'│    {cell}    │')
                    if len(cell) == 2:
                        win.addstr((i * 2) + 5, 0, f'│   {cell}    │')
                if j > 0 and format == 1:
                    if len(cell) == 1:
                        win.addstr((i * 2) + 5, 4 + (j * 7), f'  {cell}   │')
                    if len(cell) == 3:
                        win.addstr((i * 2) + 5, 4 + (j * 7), f' {cell}  │')
                if j > 0 and format == 2:
                    if len(cell) == 1:
                        win.addstr((i * 2) + 5, 1 + (j * 10), f'''    {cell}'''
                                   ''''│''')
                    if len(cell) == 3:
                        win.addstr((i * 2) + 5, 1 + (j * 10), f'   {cell}   │')
                    if len(cell) == 5:
                        win.addstr((i * 2) + 5, 1 + (j * 10), f'  {cell}  │')
                    if len(cell) == 7:
                        win.addstr((i * 2) + 5, 1 + (j * 10), f' {cell} │')

                # Below row border for last row
                if i == lines - 1 or body[-1] == row:
                    if j == 0:
                        win.addstr((i * 2) + 6, 0, '└─────────┴')
                    if j > 0 and format == 1:
                        if j != (len(body[0]) - 1):
                            win.addstr((i * 2) + 6, 4 + (j * 7), '──────┴')
                        if j == (len(body[0]) - 1):
                            win.addstr((i * 2) + 6, 4 + (j * 7), '──────┘')
                    if j > 0 and format == 2:
                        if j != (len(body[0]) - 1):
                            win.addstr((i * 2) + 6, 1 + (j * 10), '─────────┴')
                        if j == (len(body[0]) - 1):
                            win.addstr((i * 2) + 6, 1 + (j * 10), '─────────┘')

                # Below row border except for last row
                else:
                    if j == 0:
                        win.addstr((i * 2) + 6, 0, '├─────────┼')
                    if j > 0 and format == 1:
                        if j != (len(body[0]) - 1):
                            win.addstr((i * 2) + 6, 4 + (j * 7), '──────┼')
                        if j == (len(body[0]) - 1):
                            win.addstr((i * 2) + 6, 4 + (j * 7), '──────┤')
                    if j > 0 and format == 2:
                        if j != (len(body[0]) - 1):
                            win.addstr((i * 2) + 6, 1 + (j * 10), '─────────┼')
                        if j == (len(body[0]) - 1):
                            win.addstr((i * 2) + 6, 1 + (j * 10), '─────────┤')

        # Prompt to continue
        ycoord, _ = win.getyx()
        win.addstr((ycoord + 2), 0, 'Type "Enter" to continue')
        win.addstr((ycoord + 2), 6, 'Enter', GREEN)
        win.refresh()
        input()


def help(height, pages):
    ''' Print help. '''

    YELLOW, RED, BLUE, GREEN = init_colors()
    for j in range(pages):
        win.addstr(0, 0, f'''PICKLEBALL TOURNAMENT CALCULATOR HELP '''
                   f'''({j + 1}/{pages})''')
        with open(os.path.join('./help.txt'), 'r') as f:
            for i, row in enumerate(f):
                if i >= (height * j) and i < (height * (j + 1)):
                    try:
                        win.addstr(i + 2 - (height*j), 0, row)
                        win.refresh()
                    except curses.error:
                        pass
            ycoord, _ = win.getyx()

            # Prompt to continue
            win.addstr(ycoord + 1, 0, 'Type "Enter" to continue')
            win.addstr(ycoord + 1, 6, 'Enter', GREEN)
            win.refresh()
            input()
            win.clear()


def confirm(win):
    ''' Print confirmation. '''

    YELLOW, RED, BLUE, GREEN = init_colors()
    win.addstr(5, 2, 'Type "y" to confirm or type "n" to change.')
    win.addstr(5, 8, 'y', GREEN)
    win.addstr(5, 31, 'n', GREEN)
    win.refresh()


def init_colors():
    ''' Initialize colors. '''

    # Use colors if terminal has colors
    if curses.has_colors():
        curses.use_default_colors()

        # Initialize colors
        curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
        YELLOW = curses.color_pair(1)
        RED = curses.color_pair(2)
        BLUE = curses.color_pair(3)
        GREEN = curses.color_pair(4)
        return YELLOW, RED, BLUE, GREEN
