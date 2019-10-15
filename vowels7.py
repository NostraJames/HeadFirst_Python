vowels = set('aeiou')
word = input("Give me a word and I'll check dem vowels : ")
found = vowels.intersection(set(word)
for vowel in found:
	print(vowel)
