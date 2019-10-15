def search4vowels(word:str) -> set:
	"""returns any vowles found in a supplied word"""
	vowels=set('aeiou')
	return vowels.intersection(set(word))
