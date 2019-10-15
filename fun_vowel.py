def search4vowels(word):
	"""Display any vowels found in asked word"""
	vowels=set('aeiou')
	found=vowels.intersection(set(word))
	for vowel in found:
		print(vowel)
