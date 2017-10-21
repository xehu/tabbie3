'''
File: tabbie3.py

Names: Michael Cooper and Emily Hu
--------------------------------
Description: Upon being run, this script prompts the user to enter in the name of a PDF file which will be read.

The PDF file for reading is a tab card - a list of debaters and their respective performances
in each round of debate at a given tournament.

Upon reading the PDF file, it then displays a full speaker and team tab of debaters and teams,
ranked in order of their performance, in the same way in which they would be ranked in a 
national-standard debate tournament.

For more information on speaker tabs, team tabs, and tab cards, please see the README.txt 
file.
'''

from debater_class import Debater
from debater_class import Team
import PyPDF2
#import random
import re
import pprint

def read_from_pdf(pdf_file_name):
	'''
	Citation: credit to Al Sweigart for his PDF text extraction tutorial located at 
	https://automatetheboringstuff.com/chapter13/. We made significant use of the contents
	located here in the completion of this assignment.

	This function takes in the name of a PDF file, and the page the contents of which we would
	like to read, and returns a string containing the contents of that page from the PDF file.
	'''

	file_obj = open(pdf_file_name, 'rb')
	reader = PyPDF2.PdfFileReader(file_obj)
	returnstr = ""
#	for page in range(reader.numPages()):
	page_obj = reader.getPage(0)
	returnstr += page_obj.extractText()
	return returnstr

def separate_tabs(inp_str):
	'''
	Takes in the input string (the entire pdf read into a single string) and divides into multiple tab
	cards (one for each pair of debaters)
	'''
	return inp_str.split("Team:")

def separate_cards(tab_list):
	'''
	Takes in a list of strings (which are tab cards that need to be split) and returns 
	a list of lists---divides the cards by each element (e.g. the name of the debaters, 
	their scores, etc.)
	'''
	
	return_list = []

	for card in tab_list:
		return_list.append(card.split("     "))

	return return_list

def remove_lines(tab_card):
	'''
	Takes in a singular tab card (a list of strings), and removes all strings which are
	equivalent to the empty string. This is used for cleaning purposes to tidy up the
	strings which have initially been read in from the PDF.
	'''
	for item in tab_card:
		if item == "":
			tab_card.remove(item)

	return tab_card

def create_speakers(tab_card):
	'''
	Takes in a tab card - a list of strings - and returns a tuple containing two Debater
	objects and one Team object. The tab card represents performance of a team of debaters,
	and so this function returns the two individuals on the team as Debaters, and the Team
	object representing the team as a whole.

	This function makes use of predefined indices of strings within the tab card to data representing 
	the performance of debaters and the team in various rounds, and then reads that 
	information into Debater and Team objects.
	'''

	tab_card = remove_lines(tab_card)

	# List of useful data, and the indices at which it is found within each tab card
	DEBATER_TEAM_NAME = 0

	ROUND1_SR_1 = 12
	ROUND2_SR_1 = 19
	ROUND3_SR_1 = 26
	ROUND4_SR_1 = 33
	ROUND5_SR_1 = 40
	TOTAL_SR_1 = 42

	ROUND1_SR_2 = 13
	ROUND2_SR_2 = 20
	ROUND3_SR_2 = 27
	ROUND4_SR_2 = 34
	ROUND5_SR_2 = 40
	TOTAL_SR_2 = 43

	ROUND1_WL = 9
	ROUND2_WL = 16
	ROUND3_WL = 23
	ROUND4_WL = 30
	ROUND5_WL = 37


	DEBATER_1 = 5
	DEBATER_2 = 6

	TOTAL_SR = 44

	wins_losses = clean_wl(tab_card[ROUND1_WL]) + clean_wl(tab_card[ROUND2_WL]) + clean_wl(tab_card[ROUND3_WL]) + clean_wl(tab_card[ROUND4_WL]) + clean_wl(tab_card[ROUND5_WL])

	# Gather information (speaker scores, ranks, aggregate speaker scores, aggregate ranks) about one member of the team
	debater_a_speaks = [get_speaks(tab_card[ROUND1_SR_1]), get_speaks(tab_card[ROUND2_SR_1]), get_speaks(tab_card[ROUND3_SR_1]), get_speaks(tab_card[ROUND4_SR_1]), get_speaks(tab_card[ROUND5_SR_1])]
	debater_a_ranks = [get_ranks(tab_card[ROUND1_SR_1]), get_ranks(tab_card[ROUND2_SR_1]), get_ranks(tab_card[ROUND3_SR_1]), get_ranks(tab_card[ROUND4_SR_1]), get_ranks(tab_card[ROUND5_SR_2])]
	debater_a_total_speaks = get_speaks(tab_card[TOTAL_SR_1])
	debater_a_total_ranks = get_ranks(tab_card[TOTAL_SR_1])
	# Create a Debater object based upon that data
	debater_a = Debater(clean_names(tab_card[DEBATER_1]), clean_names(tab_card[DEBATER_TEAM_NAME]), debater_a_total_speaks, debater_a_total_ranks, debater_a_speaks, debater_a_ranks, wins_losses) #NEED TO ADD WINS ACK ACK ACK ACK

	# Gather information (speaker scores, ranks, aggregate speaker scores, aggregate ranks) about the second member of the team
	debater_b_speaks = [get_speaks(tab_card[ROUND1_SR_2]), get_speaks(tab_card[ROUND2_SR_2]), get_speaks(tab_card[ROUND3_SR_2]), get_speaks(tab_card[ROUND4_SR_2]), get_speaks(tab_card[ROUND5_SR_2])]
	debater_b_ranks = [get_ranks(tab_card[	ROUND1_SR_2]), get_ranks(tab_card[ROUND2_SR_2]), get_ranks(tab_card[ROUND3_SR_2]), get_ranks(tab_card[ROUND4_SR_2]), get_ranks(tab_card[ROUND5_SR_2])]
	debater_b_total_speaks = get_speaks(tab_card[TOTAL_SR_2])
	debater_b_total_ranks = get_ranks(tab_card[TOTAL_SR_2])
	# Create a Debater object based upon that data
	debater_b = Debater(clean_names(tab_card[DEBATER_2]), clean_names(tab_card[DEBATER_TEAM_NAME]), debater_b_total_speaks, debater_b_total_ranks, debater_b_speaks, debater_b_ranks, wins_losses)

	# Gather information about the debate team
	debate_team_opponents = [clean_string(tab_card[10]), clean_string(tab_card[17]), clean_string(tab_card[24]), clean_string(tab_card[31]), clean_string(tab_card[38])]

	team_total_speaks = get_speaks(clean_string(tab_card[TOTAL_SR]))
	team_total_ranks = get_ranks(clean_string(tab_card[TOTAL_SR]))

	# Create a Team object based upon the gathered data
	debate_team = Team(clean_names(tab_card[0]), debater_a, debater_b, get_num_wins(wins_losses), wins_losses, debate_team_opponents, team_total_speaks, team_total_ranks)

	return (debater_a, debater_b, debate_team)

def get_speaks(speaks_ranks_string):
	'''
	This takes in a string representing the debater's speaker scores and rank in the round of the form
	(speaker_score, rank), and returns their speaker score.
	'''
	st = divide_sr(clean_string(speaks_ranks_string))
	return float(clean_string(st[0]))

def get_ranks(speaks_ranks_string):
	'''
	This takes in a string representing the debater's speaker scores and rank in the round of the form
	(speaker_score, rank), and returns their rank.
	'''
	st = divide_sr(clean_string(speaks_ranks_string))
	return float(clean_string(st[1]))

def sort_debaters(debater_objects):
	'''
	This function takes in a list of debater objects, and sorts them first by their total speaker score,
	and then, in the event of a tie, by their total ranks.
	'''
	debater_objects = sorted(debater_objects, key = lambda debater:(-debater.total_speaks, debater.total_ranks))
	return debater_objects

def sort_teams(team_objects):
	'''
	This function takes in a list of debate team objects, and sorts them first by the number of rounds
	which the team won, then by the total speaker score obtained by members of the team.
	'''
	team_objects = sorted(team_objects, key = lambda team:(-team.wins, team.total_speaks)) #HAD TO TAKE OUT RANDOM.RANDOM(); ADD BACK WHEN TIME ALLOWS
	return team_objects

# Stripper functions - the following functions which begin with the word "clean"
# are used to remove unnecessary information from strings such that the strings may
# easily be processed.

def clean_wl(st):
	'''
	This function takes in a string, and removes all characters which are not a 
	"W" or an "L".
	'''
	st = re.sub('[^WL]', "", st)
	return st

def clean_string(st):
	'''
	This function takes in a string, and removes all characters which are not
	the digits 0 through 9.
	'''
	st = re.sub('[^0123456789.,]', "", st)
	return st

def clean_names(st):
	'''
	This function takes in a string, and removes all non-alphabetical characters, 
	as well as removing the word "Round" from the string.
	'''
	st = re.sub('[^a-zA-z ()]', "", st)
	st = re.sub('Round', "", st)
	return st

#split speaks from ranks
def divide_sr(string):
	'''
	This function takes in a string, and returns a list of values which, in the input string
	had been separated by the "," character.
	'''
	result = string.split(",")
	return result #note that this will be a list--access speaks with result[0] and ranks with result[1]

#get number of wins
def get_num_wins(string):
	'''
	This function takes in a string of five characters, W's and L's. It determines the number of wins
	that a team has attained by counting the number of W's in the string, and returning that number
	of W's.
	'''
	return string.count('W')


def print_speaker_tab(sorted_speakers):
	'''
	This function takes in a list of sorted Debater objects, then prints out the list of
	debaters in sorted order, complete with their respective teams, win-loss records, and
	speaker scores from each round.
	'''
	print("\nSPEAKER TAB: \n")
	pp = pprint.PrettyPrinter();
	for index in range(len(sorted_speakers)):
		round_speaks = []
		for round_num in range(5):
			round_speaks.append(sorted_speakers[index].get_speaks(round_num))
		debater_data = (index+1, sorted_speakers[index].name, sorted_speakers[index].team, sorted_speakers[index].wins, sorted_speakers[index].total_speaks, round_speaks)
		pp.pprint(debater_data)


def print_team_tab(sorted_teams):
	'''
	This function takes in a list of sorted Team objects, then prints out the list of teams
	in sorted order, complete with the team name, the team's members, and the team's win-loss
	record.
	'''
	print("\nTEAM TAB: \n")
	pp = pprint.PrettyPrinter();
	for index in range(len(sorted_teams)):
		team_data = (index+1, sorted_teams[index].name, sorted_teams[index].debaterA.name, sorted_teams[index].debaterB.name, sorted_teams[index].win_str) 
		pp.pprint(team_data)


if __name__ == "__main__":
	'''
	This runs the program as a script!
	It takes in user input for a file, and then prompts the user to display
	a speaker tab, team tab, or both, from the data gathered from the PDF.
	'''
	usr_input_filename = input("Please enter a file name: ")

	raw_tab_doc = read_from_pdf(usr_input_filename)
	full_cards = separate_tabs(raw_tab_doc)
	card_pieces = separate_cards(full_cards)

	# Create empty lists of debaters and teams. Then read in Debater and Team objects from the 
	# PDF.
	debater_list = []
	team_list = []
	for tab_card in card_pieces:
		if len(tab_card) > 1:
			debaters_and_team = create_speakers(tab_card)
			debater_list.append(debaters_and_team[0])
			debater_list.append(debaters_and_team[1])
			team_list.append(debaters_and_team[2])

	# Sort the list of debaters and teams
	debater_list = sort_debaters(debater_list)
	team_list = sort_teams(team_list)

	while True:

	# Ask user whether they want to print the speaker tab, team tab, or both.
		user_choice = input("Would you like to print S)peaker tab, T)eam tab?, B)oth?, or Q)uit?")
		while user_choice not in "SsTtBbQq":
			user_choice = input("Would you like to print S)peaker tab, T)eam tab?, B)oth?, or Q)uit?")

		if user_choice in "Ss":
			print_speaker_tab(debater_list)
			continue
		elif user_choice in "Tt":
			print_team_tab(team_list)
			continue
		elif user_choice in "Bb":
			print_speaker_tab(debater_list)
			print_team_tab(team_list)
			continue
		elif user_choice in "Qq":
			break


