'''
File: debater_class.py

Names: Michael Cooper and Emily Hu
SUIDs: coopermj, xehu

--------------------------------
This file implements the Debater and Team classes, to be used
in the main function tabbie3.py.
'''

class Debater:
	'''
	Debater class - this class represents a debater's performance over the course of
	a debate tournament. It stores the following information about the debater:

	- Name
	- Name of their Team
	- Aggregate Speaker Scores (sum of their speaker scores from each of their rounds)
	- Aggregate Ranks (sum of their ranks from each of their rounds)
	- Speaker Scores (a list containing the debater's speaker score earned at each round of the
	  tournament)
	- Ranks (a list containing the debater's ranks earned in each round of the tournament)
	- Wins (a string containing an ordered series of W's and L's, representing rounds won and lost,
	  respectively).
	'''
	
	def __init__(self, name, team, total_speaks, total_ranks, speaks = [], ranks = [], wins = ""):
		'''
		Constructor.
		'''
		self.name = name
		self.team = team
		self.speaks = speaks #List to be filled up with their speaks, one per round.
		self.ranks = ranks
		self.total_speaks = total_speaks
		self.total_ranks = total_ranks
		self.wins = wins


	def get_name(self):
		'''
		Returns the name of the debater.
		'''
		return self.name

	def get_team(self):
		'''
		Returns the school of the debater.
		'''
		return self.team

	def get_speaks(self, round):
		'''
		Returns a debater's speaker scores for a given round. Note that round is an int,
		and that speaker scores are doubles (so this function returns a double).
		'''
		return self.speaks[round]

	def get_ranks(self, round):
		'''
		Returns a debater's ranks for a given round. Note that ranks are stored as ints
		so this function returns an int.
		'''
		return self.ranks[round]

	def get_total_speaks(self):
		'''
		Returns the total speaker score obtained by the debater
		over the course of the tournament.
		'''
		return self.total_speaks

	def get_total_ranks(self):
		'''
		Returns the total ranks earned by the debater over the course
		of the tournament.
		'''
		return self.total_ranks

	def get_wins(self):
		'''
		Returns the number of times that the debater has won a round over the
		course of the tournament
		'''
		return self.wins
        
	def __str__(self):
		'''
		When the debater is printed, the debater's name is printed.
		'''
		return str(self.name)


class Team:
	'''
	Team class - this class represents a debate team's performance over the course of
	a debate tournament. It stores the following information about the team:

	- Team name
	- Names of Debaters on the Team
	- Number of Rounds the Team won over the course of the tournament.
	- Wins (a string containing an ordered series of W's and L's, representing rounds won and lost,
	  respectively).
	- List of opponents the Team faced over the course of the tournament.
	- Aggregate Speaker Scores (sum of their speaker scores from both partners from each of their rounds)
	- Aggregate Ranks (sum of their ranks from both partners from each of their rounds)
	'''
	def __init__(self, name, debaterA, debaterB, wins, win_str, opp_str, total_speaks, total_ranks):
		'''
		Constructor
		'''
		self.name = name
		self.debaterA = debaterA
		self.debaterB = debaterB
		self.wins = wins
		self.win_str = win_str
		self.total_speaks = total_speaks
		self.total_ranks = total_ranks

	def get_name(self):
		'''
		Returns the name of the team.
		'''
		return self.name
	def get_debaters(self):
		'''
		Returns the names of the debate team members.
		'''
		return (self.debaterA.get_name(), self.debaterB.get_name())
	def get_wins(self):
		'''
		Returns the number of rounds that the team won 
		over the course of the tournament.
		'''
		return self.wins
	def get_record(self):
		'''
		Returns the win-loss record of the team over the
		course of the tournament. Returns a string consisting
		of W's and L's - representing wins and losses, respectively - 
		such as "WWWLL".
		'''
		return self.win_str
	def get_speaks(self):
		'''
		Returns the total number of speaker scores obtained
		by members of the team.
		'''
		return self.total_speaks





