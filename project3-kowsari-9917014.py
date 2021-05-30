string = input("write your massage :")
#convert massage with big letters to a massage with low letters
string =string.lower()

a_file = open("words_alpha.txt", "r")
#change the words_alpha.txt to a list naming dictionary
dictionary = []
for line in a_file:
  stripped_line = line.strip()
  dictionary.append(stripped_line)

a_file.close()

def dictionaryContains(word):
	return word in dictionary


def wordBreak(string):

	# Last argument is prefix
	wordBreakmassage(string, len(string), "")


def wordBreakmassage(string, n, result):

	
	for i in range(1, n + 1):
	
		
		prefix = string[:i]
		
		if dictionaryContains(prefix):
		
			# If no more elements are there, print it
			if i == n:

				# Add this element to previous prefix
				result += prefix
				print(result)
				return
			wordBreakmassage(string[i:], n - i, result+prefix+" ")




if __name__ == "__main__":
	
	wordBreak(string)


