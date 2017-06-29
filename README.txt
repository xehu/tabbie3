File: README
Authors: Emily Hu (xehu), Michael Cooper (coopermj)

Contents:
1. Program Functionality
2. Files
3. Technical Requirements
4. Algorithm/Code Design
5. Installation/Execution Instructions
6. Known Bugs
7. Contact Information
8. Credit/Acknowledgements

Appendix: Background

——————————————————————————————————————————————————————————————————

1. PROGRAM FUNCTIONALITY

This program reads a PDF of debate “tab cards” (scores for individual debaters and teams) and outputs a readable table that ranks the debaters and teams against each other.(For more information on tab cards, see the “Background” section in the appendix.)

Upon running the program, the user is prompted to display a speaker tab, team tab, both, or to quit the program. The user can continue to generate tables until they quit.

2. FILES

The program requires two files: debater_class.py and tabbie3.py.

3. TECHNICAL REQUIREMENTS

The program runs Python 3.4. The following imported modules are required for the program: (1) PyPDF2;(2) re; (3) pprint. 

PyPDF2 is required to read in the PDF and parse it for text; re (often pre-installed with Python 3.4) is used to evaluate regular expressions; and pprint is used to Pretty Print the results into a readable table.

4. ALGORITHM/CODE DESIGN

We are trying to generalize and view trends (i.e. view the performance of debaters relative to each other) from data provided on an individual basis (i.e. the round-by-round results of an individual debater).

So, on a broad level, our strategy was to populate instances of a Debater class and a Team class, and then use sorting algorithms to sort and print the classes in order.

The steps were as follows:
	(1) Parse the entire tab document in as a single string.
	(2) Split the single string into each individual tab card, which contains information for a single team (pair of debaters).
	(3) Split a tab card into its constituent parts—detailing the scores debaters received for particular rounds, win loss documentation, and so forth.
	(4) Read the information for the tab file into instances of the Debater and Team classes. (We create one instance of a Team class and two instances of the Debater class per tab card.)
	(5) Sort the list of Debaters and Teams.
	(6) Print the result.

Also included are some auxiliary functions, which work to clean up the information read in. For example, the initial string read in contains a large number of tabs, spaces, and new lines, all of which must be removed before proceeding with populating the Debater classes.

5. INSTALLATION/EXECUTION INSTRUCTIONS 

Download both files (detailed in part 2), and include the appropriate modules (listed above, or in requirements.txt). To run in the iPython interactive interpreter, navigate to the project directory, then type %run tabbie3.py to run the program.

If using a different Python interpreter, follow similar instructions - navigate to the project directory, then run the file tabbie3.py.

When prompted, enter a valid string for the pdf to parse. Then follow the instructions in the text-based interface.

6. KNOWN BUGS

One notable caveat about this program is that it is highly dependent on the tab cards being in a precise format, since the program populates the Debate and Team classes by accessing specific indices of the lists read in. Even slight shifts in formatting—such as extra white space or an extra line—can completely throw off the indexing, which brings the program to its knees.

Thus, the sample pdf that we’ve included with this program (tab_card_sample.pdf) has been formatted so as to match the formatting required of this program. Unfortunately, therefore, this version of the program cannot be used to parse in actual tournament PDFs, since the formatting of tournament-generated PDFs does not match the formatting required for this program.

7. CONTACT INFORMATION

Contact Emily and Michael, project developers, at xehu@stanford.edu and coopermj@stanford.edu.

8. CREDITS/ACKNOWLEDGEMENTS

Credit to Al Sweigart for his PDF text extraction tutorial (used in the tabbie3.py file). Also due credit to David Slater for being a debate+CS role model, to Sam Redmond for an excellent introduction to Python with his CS41 course, and to the rest of the TA’s for the endless help and wonderful patience.

APPENDIX: BACKGROUND

In American Parliamentary Debate, performance is judged in three ways: (1) through being ranked by a judge using speaker scores (which usually range from 24-27, in quarter-point increments); (2) through being ranked from 1-4 against the others in their room (there are two speakers per team, two teams, and so four speakers per room). And (3) through evaluating a team’s win/loss ratio over the course of the tournament. Results at the end of a tournament are disseminated through a PDF document.

The current document is formatted as a series of “tab cards”, which contain the individual records and data for each team. However, tab cards provide no holistic information about the tournament overall—scores are the most meaningful when they compare a debater’s performance to that of others competing at the tournament. Thus, tab cards fail to give debaters information about where they generally stand and how they can improve relative to other debaters.

The final tournament document contains one such table for every team at the tournament. It lists off information ranging from the side of the motion on which the team spoke, whether they won or lost, whom they faced, by whom they were judged, their speaker scores, and their ranks. The ordering of the tables has no correlation to how well the speaker has performed at the tournament; rather, they are listed in alphabetical order.

Such a table may appear as follows:

Team: AU Dream Team (AU)Round     G/O        W/L      Opponent        Judge        Speaker A         Speaker B          Total1          G          W       Opponent A      Judge A      (25.75, 3.0)      (25.25, 4.0)	    (51.0, 7.0)2          O          L       Opponent B      Judge B      (26.5, 1.0)       (26.25, 2.0)      (103.75, 10.0)3          G          W       Opponent C      Judge C      (26.0, 2.0)       (25.75, 3.0)      (155.5, 15.0)4          O          L       Opponent D      Judge D      (26.25, 3.0)      (25.75, 4.0)      (207.5, 22.0)5          G          W       Opponent E      Judge E      (26.25, 1.0)      (25.75, 3.0)      (259.5, 26.0)Tournament Totals:                                         (130.75, 10.00)   (128.75, 16.00)   (259.50, 26.00)

Our program thus parses such “tab card” files to solve the current readability problem.
