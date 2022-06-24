'''
PICKLEBALL TOURNAMENT CALCULATOR
A tool for generating round robin pickleball tournaments.
'''

import os
import sys
import math
import readline
import csv
import curses
from curses import wrapper
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, \
    TableStyle, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter, inch, landscape
from reportlab.lib import colors
import strings

# Skip title screen if modify tournament settings selected from menu
skip_title = 0


def main(scr):

    global skip_title

    # Embed program within padded window
    win = curses.newwin(100, 200, 1, 2)

    # Title screen
    if skip_title == 0:
        title(scr, win)

    # Get tournament options: format, number players/teams
    format = get_format(win)
    number = get_number(win, format)

    # Repeat menu until quit
    while True:

        # Get menu selection: print, save, send, modify, help, quit
        menu = get_menu(win, format, number)

        # Print tournament schedule to screen
        if menu == 1:
            screen_width = get_width(win, 'print')
            screen_print(scr, win, format, number, screen_width)

        # Save tournament schedule to file
        if menu == 2:
            file_width = get_width(win, 'save')
            file_path = get_path(win, format, number, file_width)
            file_generate(win, format, number, file_width, file_path)

        # Modify tournament settings
        if menu == 3:
            os.system('clear')
            wrapper(main)

        # Help menu
        if menu == 4:
            win.clear()
            help(scr, win)

        # Quit
        if menu == 5:
            win.clear()
            sys.exit()


def title(scr, win):
    ''' Display title screen. '''

    global skip_title

    # Print title screen
    strings.title(win)

    # Prompt to continue or access help
    key = ''
    while key != 104 and key != 10:
        key = win.getch()
    if key == 104:
        help(scr, win)
        wrapper(main)
    if key == 10:
        skip_title = 1
        wrapper(main)


def get_format(win):
    ''' Get tournament format: fixed-partner, rotating partner. '''

    # Print question
    strings.format_question(win)

    # Get format
    format = 0
    while format != 49 and format != 50:
        format = win.getch()
    format = 1 if format == 49 else 2

    # Print format
    if 1 <= format <= 2:
        if format == 1:
            strings.format_fixed(win)
        if format == 2:
            strings.format_rotating(win)

        # Print confirmation
        strings.confirm(win)

        # Confirm format
        confirm = 0
        while confirm != 110 and confirm != 121:
            confirm = win.getch()
        confirm = 0 if confirm == 110 else 1

        # If confirmed return format, otherwise ask again
        if confirm == 0:
            return get_format(win)
        if confirm == 1:
            return format


def get_number(win, format):
    ''' Get number of players/teams. '''

    # Print question
    win.clear()
    if format == 1:
        strings.number_question_fixed(win)
    if format == 2:
        strings.number_question_rotating(win)

    # Get number
    curses.curs_set(1)
    curses.echo()
    number = win.getstr(2, 2, 15)
    curses.noecho()
    curses.curs_set(0)
    win.refresh()

    # Check number validity
    try:
        number = int(number)

        # Print number if valid
        if (format == 1 and number >= 3 and number <= 26) or \
           (format == 2 and number >= 4 and number <= 26):
            if format == 1 and number >= 3 and number <= 26:
                strings.number_fixed(win, number)
            if format == 2 and number >= 4 and number <= 26:
                strings.number_rotating(win, number)

            # Print confirmation
            strings.confirm(win)

            # Confirm number
            cfm = confirm(win)

            # If confirmed return number, otherwise ask again
            if cfm == 0:
                return get_number(win, format)
            if cfm == 1:
                return number

        # If input out of range then raise error
        if format == 1 and (number < 3 or number > 26):
            raise ValueError
        if format == 2 and (number < 4 or number > 26):
            raise ValueError

    # If error print error message and ask again
    except ValueError:
        if format == 1:
            strings.number_error_fixed(win)
        if format == 2:
            strings.number_error_rotating(win)
        return get_number(win, format)


def get_menu(win, format, number):
    ''' Get menu selection: print, save, restart, help, quit. '''

    # Print question
    strings.menu(win, format, number)

    # Get selection
    menu = 0
    while menu not in [49, 50, 51, 52, 53]:
        menu = win.getch()
    if menu == 49:
        menu = 1
    elif menu == 50:
        menu = 2
    elif menu == 51:
        menu = 3
    elif menu == 52:
        menu = 4
    else:
        menu = 5

    # Return selection
    return menu


def get_width(win, action):
    ''' Get table width: narrow, wide, or both. '''

    # Print question
    strings.width(win, action)

    # Get width
    width = 0
    while width not in [49, 50, 51]:
        width = win.getch()
    if width == 49:
        width = 1
    elif width == 50:
        width = 2
    else:
        width = 3

    # Return width
    return width


def screen_print(scr, win, format, number, width):
    ''' Print tournament schedule(s) to screen. '''

    # Specify file(s) to open
    file_narrow = ''
    file_wide = ''
    if width == 1:
        file_narrow = os.path.join(f'./data/{format}_{number}_n.csv')
    if width == 2:
        file_wide = os.path.join(f'./data/{format}_{number}_w.csv')
    if width == 3:
        file_narrow = os.path.join(f'./data/{format}_{number}_n.csv')
        file_wide = os.path.join(f'./data/{format}_{number}_w.csv')

    # Get terminal height
    ymax, _ = scr.getmaxyx()
    height_window = int(ymax)

    # Window print height (after title, header, prompt excluded)
    height_print = height_window - 8

    # Narrow
    if file_narrow != '':

        # Load file
        with open(file_narrow, 'r') as f:
            table = []
            reader = csv.reader(f)
            for row in reader:
                table.append(row)

        # Screen setup
        pages, lines = screen_setup(win, table, height_print)

        # Print table
        strings.screen_narrow(win, number, table, pages, lines)

    # Wide
    if file_wide != '':

        # Load file
        with open(file_wide, 'r') as f:
            table = []
            reader = csv.reader(f)
            for row in reader:
                table.append(row)

        # Screen setup
        pages, lines = screen_setup(win, table, height_print)

        # Print table
        strings.screen_wide(win, format, number, table, pages, lines)


def get_path(win, format, number, width):
    ''' Get path to save file, only existing paths accepted. '''

    # Print question
    if width == 1 or width == 2:
        strings.path_onewidth(win)
    if width == 3:
        strings.path_twowidth(win)

    # Get path
    curses.echo()
    ycoord, xcoord = win.getyx()
    win.addstr(ycoord + 1, 2, '''                                        '''
               '''                                      ''')
    ycoord, xcoord = win.getyx()
    file_path = win.getstr(ycoord, 2, 70)
    file_path = str(file_path)
    file_path = file_path[2:-1]
    file_path = file_path.rstrip()
    if len(file_path) > 0:
        if file_path[-1] != os.path.join('/'):
            file_path = os.path.join(f'{file_path}/')
    curses.noecho()
    curses.curs_set(0)
    win.refresh()

    # If path doesn't exist then print error message and ask again
    path_exist = str(os.path.exists(file_path))
    if path_exist == 'False':
        strings.path_error(win)
        return get_path(win, format, number, width)
    if path_exist == 'True':
        return file_path


def file_generate(win, format, number, width, path):
    ''' Generate table pdf file(s). '''

    # Assign list of width(s) to generate
    gen = []
    if width == 1 or width == 3:
        gen.append('narrow')
    if width == 2 or width == 3:
        gen.append('wide')

    # Iterate through widths
    for i, _ in enumerate(gen):

        # Assign input/output file names for width
        input_name = ''
        output_name = ''
        format_str = 'fixed' if format == 1 else 'rotating'
        if gen[i] == 'narrow':
            input_name = os.path.join(f'./data/{format}_{number}_n.csv')
            output_name = os.path.join(f'''{path}pbtc_{format_str}_{number}'''
                                       '''_narrow.pdf''')
        if gen[i] == 'wide':
            input_name = os.path.join(f'./data/{format}_{number}_w.csv')
            output_name = os.path.join(f'''{path}pbtc_{format_str}_{number}'''
                                       '''_wide.pdf''')

        # Assign title
        title = f'{format_str}-PARTNER ROUND ROBIN ({number} PERSON)'.upper()

        # Instantiate document template
        doc = SimpleDocTemplate(output_name,
                                rightMargin=0.5*inch, leftMargin=0.5*inch,
                                topMargin=0.5*inch, bottomMargin=0.5*inch)
        doc.pagesize = letter if gen[i] == 'narrow' else landscape(letter)

        # Initialize element list
        elements = []

        # Append title and spacer objects to elements
        styles = getSampleStyleSheet()
        elements.append(Paragraph(title, styles['Title']))
        elements.append(Spacer(1, 0.25*inch))

        # Read input file and append contents to data
        data = []
        with open(input_name, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                data.append(row)

        # Determine table height and width from data
        table_height = len(data)
        table_width = len(data[0])

        # Instantiate table object
        if format == 1 and gen[i] == 'wide':
            table = Table(data, table_width*[0.6*inch],
                          table_height*[0.3*inch], repeatRows=1)
        else:
            table = Table(data, table_width*[1*inch], table_height*[0.3*inch],
                          repeatRows=1)

        # Customize table style
        table.setStyle(TableStyle(
                        [('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
                         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                         ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                         ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                         ('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))

        # Append table to elements
        elements.append(table)

        # Build document
        doc.build(elements)

    # Print confirmation
    path = path[0:-1]
    if width == 1 and path != os.path.join('./'):
        strings.file_narrow(win)
    if width == 2 and path != os.path.join('./'):
        strings.file_wide(win)
    if width == 3 and path != os.path.join('./'):
        strings.file_both(win)


def help(scr, win):
    ''' Information about tournament and schedule formats. '''

    # Get terminal height
    ymax, _ = scr.getmaxyx()
    height = int(ymax) - 5

    # Open help file
    win.clear()
    with open(os.path.join('./help.txt'), 'r') as f:

        # Calculate lines/pages required for help
        lines = sum(1 for line in f)
        pages = math.ceil(float(lines / height))

    # Print help
    strings.help(height, pages)


def screen_setup(win, table, height_print):
    ''' Determine parameters required for printing table to screen. '''

    # Table height (not including header row)
    height_table = (len(table) - 1) * 2

    # Pages required
    pages = math.ceil(float(height_table / height_print))

    # Table lines per page (cells (1) and bottom border (1))
    lines = math.floor(float(height_print / 2))

    # Return pages, lines
    return pages, lines


def confirm(win):
    ''' Confirm input. '''
    confirm = 0
    while confirm != 110 and confirm != 121:
        confirm = win.getch()
    confirm = 0 if confirm == 110 else 1
    return confirm


if __name__ == '__main__':
    wrapper(main)
