import string

def abbreviate(words):
	ans = ''

    # split the string on spaces
	words = words.split(' ')

	# iterate through the words and find the first character 

	for word in words:
		for c in word:
			if c in string.ascii_letters:
				ans += c.upper()
				break

	return ans

print(abbreviate("GNU Image Manipulation Program"))