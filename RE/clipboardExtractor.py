### Introduction
## Scenario
"""This is the first project in the AtBS book.
The project puts forth the use-case of the following:
**Say you have the boring task of finding every phone number and email address in a long web page or document. 
If you manually scroll through the page, you might end up searching for a long time. But if you had a program that could search the text in your clipboard for phone numbers and email addresses, you could simply press CTRL-A to select all the text, press CTRL-C to copy it to the clipboard, and then run your program. 
It could replace the text on the clipboard with just the phone numbers and email addresses it finds.**
"""
## Starting Out
"""
It is recommended to take a step back and think about the workflow of your programme before typing anything. 
This code should do the following:
1 - Get text from the clipboard.
2 - Find all the phone numbers and email addresses in the text.
3 - Paste them onto the clipboard. 
As such the workflow should look like this:
1 - Use the `pyperclip` module to copy and paste strings.
2 - Create two regexes for phone numbers and email addresses.
3 - Find all matches for each regex
4 - Neatly format the matched stings into a single string to paste.
5 - Display some kind of message if no matches were found in the text. 
"""

### STEP ONE : Creating Regexes

#! python3

import pyperclip, re

phoneRegex = re.copmile(r'''(
	(\d{3}|\(\d{3}\))? 						# area code
	(\s|-|\.)?										# separator
	(\d{3})												# first 3 digits
	(\s|-|\.) 										# separator
	(\d{4})												# last 4 digits
	(\s*(ext|x|ext.)\s*(\d{2,5}))?	# extension
)''', re.VERBOSE)

# TODO: Create email regex.

# TODO: Find matches in clipboard text.

# TODO: Copy results to the clipboard.
