#!/usr/bin/python
# Reference from stack overflow: https://stackoverflow.com/questions/11015320/how-to-create-a-trie-in-python
def find_prefix(trie, p):
    ctrie = trie
    for l in p:
        if l in ctrie:
            ctrie = ctrie[l]
        else:
            return False
    return True

def calculateOSADistance(str1, str2):
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
def task4(dictionary, raw):
	"""
	TODO:
		implement your optimized edit distance function for task 4 here
		dictionary : path of dictionary.txt file 
		raw: path of raw.txt file
		return : a list of min_distance of each word in the raw.txt 
		compared with words in the dictonary 
	example return result : [0,1,0,2]
	"""
	
	with open(raw) as r:
		raw = []
		for line in r:
			raw.append(line.strip())
		min_dist = []
	
	with open(dictionary) as r:
		dictionary = []
		for line in r:
			dictionary.append(line.strip())

	trie = {}

	for w in dictionary:
		node = trie
		for l in w:
			node = node.setdefault(l, {})
		node['#'] = '#'

	min_dist = []
	for word in raw:
		word_dis = []
		for i in range(len(word)):
			if find_prefix(trie, word + '#'):
				word_dis.append(0)
				break
			elif find_prefix(trie, word):
				for j in range(len(dictionary)):
					if dictionary[j].startswith(word[0]):
						word_dis.append(calculateOSADistance(word, dictionary[j]))
				break
			elif find_prefix(trie, word[:i+1]):
				pass
			else:
				for j in range(len(dictionary)):
					if dictionary[j].startswith(word[0]):
						word_dis.append(calculateOSADistance(word, dictionary[j]))
				break
		if min(word_dis) > 1:
			for j in range(len(dictionary)):
				word_dis.append(calculateOSADistance(word, dictionary[j]))
		min_dist.append(min(word_dis))
	return min_dist