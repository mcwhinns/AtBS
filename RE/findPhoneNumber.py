def isPhoneNumber(text):
	"""This function does the tedious work of iterating through
	every digit in a given text, returning True if it's a phone number,
	otherwise False.
	This is an inefficient piece of code because it checks
	every single character to match it against a tedioius patter.
	Later, this will be rewritten to use RegEx."""
	
	if len(text) != 12:
		return False
	for i in range(0, 3):
		if not text[i].isdecimal():
			return False
	if text[3] != '-':
		return False
	for i in range(4,7):
		if not text[i].isdecimal():
			return False
	if text[7] != '-':
		return False
	for i in range(8,12):
		if not text[i].isdecimal:
			return False
	return True

# Quick test
print("Is 415-555-4242 a phone number?")
print(isPhoneNumber('415-555-4242'))
print("Is \'Moshi Moshi\' a phone number?")
print(isPhoneNumber('Moshi Moshi'))

# Finding a phone number in a given message
message = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office."
for i in range(len(message)):
	# every iteration is for the length of the message
	chunk = message[i:i+12]
	# a chunk of 12 characters is taken from possition `i`
	if isPhoneNumber(chunk):
		# if phone number is found, it will print it here
		print('Phone number found: ' + chunk)
print("Done")