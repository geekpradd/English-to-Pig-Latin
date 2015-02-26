#Core lists
LETTERS=list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
VOWELS=list('aeiouAEIOU')
CONSONANTS=list(set(LETTERS)-set(VOWELS))


def allConsonants(part):
	for a in part:
		if not a in CONSONANTS:
			return False
	return True
def paginate(word):
	d = {}
	for a in range(len(word)):
		if allConsonants(word[:a:]):
			d[a]=word[:a:]
	return d[max(d.keys())]

def toPigLatin(word):
	if word[0] in VOWELS:
		return word+"ay"
	elif word[0] in CONSONANTS:
		if word[0].isupper():
			return (word.replace(paginate(word),'')+paginate(word)+'ay').lower().capitalize()
		return (word.replace(paginate(word),'')+paginate(word)+'ay').lower()


if __name__=='__main__':
	print ("Welcome to the Pig Latin Translator.. Enter the words in the prompt and press enter or enter 'quit' to exit\n")
	words=False
	while True:
		if words:
			print(' '.join([toPigLatin(word) for word in words]))
		print(">>> ",end='')
		words=str(input()).split(' ')
		if words=="quit":
			break