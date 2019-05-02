#function that decrypts an input string given a key
def decrypt(inpString):
    #split input string into letters
	cipherLetters = list(inpString)
	messageLetters = []
	message = ''
	
	#loop through each letter
	for letter in cipherLetters:
		if letter.isalpha():
			
			#get ascii value of letter
			letterVal = ord(letter)
			letterVal = int(letterVal) + 2
			if letter.islower():
				if letterVal > 122:
					letterVal = letterVal - 26
			elif letter.isupper():
				if letterVal > 90:
					letterVal = letterVal - 26
			messageLetters.append(chr(letterVal))
		else:
			messageLetters.append(letter)
	
	message = message.join(messageLetters)
	return message
