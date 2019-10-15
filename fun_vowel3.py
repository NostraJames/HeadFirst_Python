def search4vowels(phrase:str, letters:str) -> set:
	"""Return a set of the 'letters' found in 'phrase'"""
	vowels=set('aeiou')
	return set(letters).ntersection(set(phrase))
