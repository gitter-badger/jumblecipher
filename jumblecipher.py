#!/usr/bin/python

# Written by zippynk on BitBucket. https://bitbucket.org/zippynk/jumblecipher
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from random import randint
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode(phraseToCipher):
  outphrase = ""
  letters2 = []
  for i in range(26):
  	i2 = randint(0,len(letters)-1)
  	letters2.append(letters[i2])
  	letters.pop(i2)
  for i in phraseToCipher:
  	for i2 in range(len(letters2)):
  		if i.lower() == letters2[i2]:
  			outphrase = outphrase +str(i2+1)
  	if not str(i.lower()) in letters2:
  		if i in numbers:
  			print "ERROR: Phrase cannot contain a number. Leaving out the number - you may want to re-run cipherer with the number spelled out or removed completely."
  		else:
  			if i == '|':
				print "ERROR: Phrase cannot contain a |. Leaving out the | - you may want to re-run cipherer with the | removed."
  			else:
				outphrase = outphrase +str(i)
  return {"key":letters2,"output":outphrase}

def splitEncodedNumbers(string):
  in_brackets = False
  broken_down_encoded_phrase = ""
  i = 0
  for i_throwaway in range(len(string)):
	if string[i] in numbers: # If the current character is a number
	  if len(string) > i+1: # If it's safe to check for the next characer
		if string[i+1] in numbers: # If the current and next characters are numbers
		  if in_brackets == True: # If the current and next characters are numbers, and we are currently in brackets.
			if int(string[i-1] +string[i]) > 26 or string[i-1] == '0': # If the current character is a number, and so is the next character, we are currently in brackets, and it's time to end them.
			  broken_down_encoded_phrase = broken_down_encoded_phrase +']|' # End the brackets.
			  in_brackets = False # Disable the brackets boolean.
			  if int(string[i] +string[i+1]) < 27: # If the current character is a number, and so is the next character, we are currently not in brackets (although we just broke out of them), and it's time to enter them.
				broken_down_encoded_phrase = broken_down_encoded_phrase +'[' +string[i] # Start the brackets and append the current number.
				in_brackets = True # Officially enable bracket mode.
				i += 1 # Increase the index.
			  else: # If the current character is a number, and so is the next character, we are currently not in brackets (although we just broke out of them), and we need to stay out of them.
				broken_down_encoded_phrase = broken_down_encoded_phrase +string[i] # Append the current item, entering brackets.
				i += 1 # Increase the index.
			else: # If the current character is a number, and so is the next character, we are currently in brackets, and we need to stay in them.
			  broken_down_encoded_phrase = broken_down_encoded_phrase +string[i] # Append the current item, without leaving the brackets.
			  i += 1 # Increase the index.
		  else: # If the current and next characters are numbers, and we are not currently in brackets.
			if int(string[i] +string[i+1]) < 27: # If the current character is a number, and so is the next character, we are currently not in brackets, and it's time to enter them.
			  broken_down_encoded_phrase = broken_down_encoded_phrase +'|[' +string[i] # Start the brackets and append the current number.
			  in_brackets = True # Officially enable bracket mode.
			  i += 1 # Increase the index.
			else: # If the current character is a number, and so is the next character, we are currently not in brackets, and we need to stay out of them.
			  broken_down_encoded_phrase = broken_down_encoded_phrase +'|' +string[i] # Append the current item, entering brackets.
			  i += 1 # Increase the index.
		else: # If the current character is a number, but the next character isn't.
		  if in_brackets == True: # If the current character is a number, but the next character isn't, and we're currently in brackets
									if int(string[i-1] +string[i]) > 26: # If the current character is a number, the next character isn't, we're currently in brackets, and it's time to break out of the brackets that we're currently in.
											broken_down_encoded_phrase = broken_down_encoded_phrase +']|' +string[i] # Append the current item, then close the brackets
											in_brackets = False # Officialize the closing of the brackets
											i += 1 # Increase the index.
									else:
											broken_down_encoded_phrase = broken_down_encoded_phrase +string[i] # Append the current item, keeping the brackets open
											i += 1 # Increase the index.
		  else: # If we are currently dealing with a number and a non-number after it, and we are outside of brackets. (This means that we CANNOT enter a series of brackets, since there's no number it could be combined with.)
			broken_down_encoded_phrase = broken_down_encoded_phrase +"|" +string[i] # Append it.
			i += 1 # Increase the index.
	  else: # If we're dealing with the last character, and it is a number
		if in_brackets == True: # If the current character is a number, but the next character isn't, and we're currently in brackets
								  if int(string[i-1] +string[i]) > 26: # If the current character is a number, the next character isn't, we're currently in brackets, and it's time to break out of the brackets that we're currently in.
										  broken_down_encoded_phrase = broken_down_encoded_phrase +']|' +string[i] # Append the current item, then close the brackets
										  in_brackets = False # Officialize the closing of the brackets
										  i += 1 # Increase the index.
								  else:
										  broken_down_encoded_phrase = broken_down_encoded_phrase +string[i] # Append the current item, keeping the brackets open
										  i += 1 # Increase the index.
		else: # If we are currently dealing with the last character, which is a number, and we are outside of brackets. (This means that we CANNOT enter a series of brackets, since there's no number it could be combined with.)
		  broken_down_encoded_phrase = broken_down_encoded_phrase +"|" +string[i] # Append it.
		  i += 1 # Increase the index.
	else: # If we are currently dealing with a non-number.
	  if in_brackets == True: # If we are currently dealing with a non-number and we are currently in brackets.
		in_brackets = False # Disable the brackets boolean.
		broken_down_encoded_phrase = broken_down_encoded_phrase +"]|" +string[i] # Put a closing bracket, and append the current character
		i += 1 # Increase the index.
	  else: # If we are currently dealing with a non number and not in brackets.
		broken_down_encoded_phrase = broken_down_encoded_phrase +"|" +string[i] # Append it.
		i += 1 # Increase the index.
  if in_brackets == True:
	broken_down_encoded_phrase = broken_down_encoded_phrase +"]"
  return broken_down_encoded_phrase

def jchelp():
    print """jumblecipher is a python library and a set of command line tools for encoding and assisting with the decoding of jumbled Caesar ciphers of the letters of the alphabet to the numbers 1-26.

jumblecipher is written by zippynk on BitBucket and licensed under the MPL 2.0. Official Notice:
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.

Command Line Usage:
You will be prompted to enter parameters once you run the command.

'jcencode' to encode text.
  - This will return both a key and a string of encoded text. The key is a list of letters, in the order that they are numbered in the key, the first one numbered 1, the last one numbered 26. The encoded text is the jumbleciphered version of the text you entered. Any non-letter characters be the same as their 'keyed' counterparts.
  - You can not use numbers or '|' signs in your text to encode.
'jcsplit' to split encoded numbers the best it can.
  - This will return a string of numbers, split by | signs and brackets. Things split by | are definitely seperate, while things in brackets are not necessarily seperate.
'jchelp' to display this text..

Python Usage:
First, 'import jumblecipher'

Next, use:
'jumblecipher.encode(string_to_encode)' to encode text.
  - This will return a dictionary, which contains both an encryption key (under the key 'key') and a string of encoded text (under the key 'output'). The key is an array of strings, each letters, in the order that they are numbered in the key, the first one numbered 1, the last one numbered 26. The encoded text is a string, the jumbleciphered version of the text you gave as input. Any non-letter characters be the same as their 'keyed' counterparts.
  - You can not use numbers or '|' signs in your text to encode.
'jumblecipher.splitEncodedNumbers(string_of_encoded_text_to_split)' to split encoded numbers the best it can.
  - This will return a string of numbers, split by | signs and brackets. Things split by | are definitely seperate, while things in brackets are not necessarily seperate.
'jumblecipher.jchelp()' to display this text.

Source available at https://bitbucket.org/zippynk/jumblecipher"""
