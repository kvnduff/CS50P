# THE PICKLEBALL TOURNAMENT CALCULATOR

The pickleball tournament calculator is a program that generates schedules for
different types of pickleball tournaments. A video demonstration of the program 
can be found at:
  `https://www.youtube.com/watch?v=WHggJosI90s`


## Program Features

The program begins at the title screen. The title screen includes an image and 
a brief introduction. From the title screen, users can type "h" to view the 
help documentation or type "Enter" to start the program. Following is the text 
included in the help documentation.

  ROTATING-PARTNER ROUND ROBIN FORMAT

  A rotating partner round robin is a tournament format in which players 
  partner with every other player once (i.e. they "rotate" through partners) 
  and oppose every other player twice. This is a highly social format but tends 
  not to be used in high-level competition.

  It is not possible to produce "true" rotating-partner round robins for all
  number of players. Following is a breakdown of how the rotating-parter round
  robin format has been modified in order to produce schedules for 4 through 26
  players. The format depends upon the number of players remaining
  after dividing the total number of players by 4. If the number of players
  is divisible by 4 then a "true" rotating-partner is possible and no
  modifications are needed.

  * R = 1: Each round, the player not assigned to a game is given
    a bye.

  * R = 2: Each round, the two players not assigned to a doubles game play a
    one-versus-one game. Depending on the preference of the tournament
    organizers, this could constitute full court singles, skinny-singles,
    half-court dinking singles, or any other preferred one-versus-one format.
    Alternatively, these two players could be
    assigned a bye.

  * R = 3: Each round, the three players not assigned to a doubles game play a
    one-versus-two game. Depending on the preference of the tournament
    organizers, this could constitute cut-throat or any other two-versus-one
    format. Alternatively, these three players could be
    assigned a bye.

  FIXED-PARTNER ROUND ROBIN FORMAT

  A fixed-partner round robin is the classic round-robin format where players
  partner with the same player (i.e. they have "fixed" teams) throughout the
  tournament. This format ensures each team plays the same number of games and
  often a higher number of minimum games compared to other tournament
  formats (e.g. only two games in double elimination format). If the number
  of teams is odd then one team will be assigned a bye every round.

  ROUND ROBIN TOURNAMENT SCHEDULES

  The tournament schedules can be viewed in "narrow" and "wide" formats. The
  narrow format shows games sequentially in a list. This format is useful to
  see a list of all the games in the tournament. If your venue doesn't have
  the ideal number of courts available (see below) then this list can be used
  to assign games to courts and to keep track of completed games. The wide
  format schedule shows all games in a table where rows are rounds and courts
  are columns. This format also shows if a player/team has a bye.

  The following information can be used to interpret the tournament schedules:

  * GAMES: The number of games included in the schedule is explicitly
    included in the narrow format schedule under the "GAME" column. This is a
    unique listing of all the games included in the schedule. The "GAME"
    column is not included in the wide format schedule, however, the
    number of games can be calculated multiplying the number of rows and 
    columns.

  * ROUND: Several games are included within a round. All teams
    (fixed-partner) or players (rotating-partner) will play during each
    round, except for schedules with 7, 11, 15, 19 and 23 players/teams,
    where one player/team will have a bye.

  * COURTS: Ideally, the venue where the tournament is hosted will have at
    least as many courts as there are games in a round. This allows all games
    of each round to be played simultaneously. The number of games in each
    round (i.e. the ideal number of courts available) is shown by the maximum
    number in the "COURT" column in the narrow format schedule, or by the
    largest C# in the first row in the wide format schedule. If your venue
    doesn't have enough courts to accommodate the number of games within a
    round then games can be assigned as soon as courts and players/teams
    become available.

  * TEAMS: The players/teams assigned to each court are shown in the "TEAM"
    column in the narrow format schedule and under the court columns (e.g.
    "C1", "C2", "C3", etc.) in the wide format schedule. The team to the left
    of the ":" is the team that serves first.

  * BYE: For schedules that require a bye (schedules with 7, 11, 15, 19 or
    23 players/teams) the player/team with a bye is indicated in the wide 
    format schedule.

After typing "Enter" from the title screen, the program begins by asking users
the format of the tournament they are planning to organize (rotating partner or 
fixed partner) and the number of teams/players that will participate.

After the tournament format and number of players/teams is collected, users are 
then presented with the following options at the main menu:
  Type "1" to print your tournament schedule to the screen.
  Type "2" to save your tournament schedule to a file.
  Type "3" to modify your tournament settings.
  Type "4" for help.
  Type "5" to quit.

If the user chooses to print their tournament schedule to the screen or to save 
to a file, then they are asked which format they would like to print/save. The 
formats include narrow, wide (or both). The formats are described in the help 
documentation. If users choose to save to a file then they are prompted to type 
in the file path where they would like the file saved. The print to screen 
option outputs the tournament schedule to the screen. The save to file option 
saves the tournament schedule to a pdf file.

The other main menu options include modify tournament settings, help and quit. 
If users choose to modify their tournament settings then they are prompted to 
reenter the tournament format and number of players/teams. The help option 
prints the help documentation to the screen (similar to typing "h" from the 
title screen). The quit option exits the program.


## Technical Details

The program is implemented using the curses library to provide a more refined 
user experience. The curse's library includes the getch function which is 
useful for capturing user input without requiring "Enter" to be typed. So for 
example, typing "h" at the title screen will immediately present the help 
documentation without requiring the user to type "h" followed by "Enter" (which 
would be required using Python's builtin input function). The getch function is 
also useful to limit user input. For example, the main menu includes options 
"1" through "5". If users type any number between "1" and "5" then they will 
proceed to the indicated option but nothing will happen if users type any other 
character. Curses also includes other useful features that can be used to  
capture the terminal display size and to detect the cursors location.

After users input their tournament settings (e.g. format and number 
players/teams), the settings are printed to the screen and the user is prompted 
to confirm the settings inputted are correct. If users indicate the settings 
are incorrect by typing "n" then the user is prompted to renter the settings. A 
range check is included for the number of players/teams. If the number inputted 
is out of range then an error message is displayed and users are prompted to 
provide a valid number.

The print to screen main menu options prints the tournament schedule in tabular 
format to the screen. Originally, prior to implementing the program in curses, 
the tabulate library was used to output the desired table from a raw data file. 
However, as far as the developer is aware, the tabulate library can't be used 
with curses. This being the case, the screen_print function was created to 
print the schedule to the screen.

Both the help documentation and print to screen main menu option prints text to 
the screen by first detecting the terminal size. If more text is being printed 
than can be accommodated by the terminal then the user is prompted to type 
"Enter" to continue to the next screen/page. Additionally, the first row 
includes a title that indicates the current page and the total number of pages 
to be displayed.

The save to file main menu option saves the tournament schedule to a pdf file 
(one pdf file for each table format selected). The reportlab library was used 
to generate the pdf files from the raw data.


## Project files

The project includes the following files:
  * README.md: description of program features and technical details
  * help.txt: help documentation text
  * requirements.txt: required pip dependencies (reportlab)
  * strings.py: functions for printing strings to the cursses interface
  * test_project.py: unit tests
  * tournament.py: main program file
  * ./data folder: tournament schedule raw data (96 total files)
