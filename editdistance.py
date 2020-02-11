#!/usr/bin/python

class EditDistance():
	
	def __init__(self):
		"""
		Do not change this
		"""
	
	def calculateLevenshteinDistance(self, str1, str2):
		"""
		TODO:
			take two strings and calculate their Levenshtein Distance for task 1 
			return an integer which is the distance
		"""
		if len(str1) == 0:
			return len(str2)
		if len(str2) == 0:
			return len(str1)

		d = [[0 for m in range(len(str2) + 1)] for n in range(len(str1) + 1)]
		for i in range(1, len(str1) + 1):
			d[i][0] = i
		for j in range(1, len(str2) + 1):
			d[0][j] = j
		for j in range(1, len(str2) + 1):
			for i in range(1, len(str1) + 1):
				if str1[i-1] == str2[j-1]:
					subsCost = 0
				else:
					subsCost = 1
				d[i][j] = min(d[i-1][j] + 1, d[i][j-1] + 1, d[i-1][j-1] + subsCost)
		return d[-1][-1]
		
	def calculateOSADistance(self, str1, str2):
		"""
		TODO:
			take two strings and calculate their OSA Distance for task 2 
			return an integer which is the distance
		"""
		if len(str1) == 0:
			return len(str2)
		if len(str2) == 0:
			return len(str1)
			
		d = [[0 for m in range(len(str2) + 1)] for n in range(len(str1) + 1)]
		for i in range(1, len(str1) + 1):
			d[i][0] = i
		for j in range(1, len(str2) + 1):
			d[0][j] = j
		for j in range(1, len(str2) + 1):
			for i in range(1, len(str1) + 1):
				if str1[i-1] == str2[j-1]:
					subsCost = 0
				else:
					subsCost = 1
				d[i][j] = min(d[i-1][j] + 1, d[i][j-1] + 1, d[i-1][j-1] + subsCost)

				if i > 1 and j > 1:
					if str1[i-1] == str2[j-2] and str1[i-2] == str2[j-1]:
						d[i][j] = min(d[i][j], d[i-2][j-2] + subsCost)
		return d[-1][-1]

		
	def calculateDLDistance(self, str1, str2):
		"""
		TODO:
			take two strings and calculate their DL Distance for task 3 
			return an integer which is the distance
		"""
		set1 = set(str1)
		set2 = set(str2)
		set3 = set1.union(set2)
		dic = {}
		for s in set3:
			dic[s] = 0
		d = [[0 for m in range(-1, len(str2) + 1)] for n in range(-1, len(str1) + 1)]
		md = len(str1) + len(str2)
		d[0][0] = md
		for i in range(len(str1) + 1):
			d[i+1][0] = md
			d[i+1][1] = i
		for j in range(len(str2) + 1):
			d[0][j+1] = md
			d[1][j+1] = j
		for i in range(1, len(str1) + 1):
			gamma = 0
			for j in range(1, len(str2) + 1):
				k = dic[str2[j-1]]
				beta = gamma
				if str1[i-1] == str2[j-1]:
					subsCost = 0
					gamma = j
				else:
					subsCost = 1
				d[i+1][j+1] = min(d[i][j] + subsCost, d[i+1][j] + 1, d[i][j+1] + 1, d[k][beta] + i - k + j - beta - 1)
			dic[str1[i-1]] = i
		return d[-1][-1]