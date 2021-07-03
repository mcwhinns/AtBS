### RegEx

import re

## Basic matching
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search("My number is 415-555-4242.")
print("Phone number found: " + mo.group())

## Matching Groups
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search("My number is 415-555-4242.")
for i in range(3):
	print("passing mo.group({}) yields: {}".format(i, mo.group(i)))
areaCode, mainNumber = mo.groups()
print("mo.groups() yields: " + str(mo.groups()))
# mo.groups yields a touple that must be converted to a string to print

## Matching Various
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
for i in range(2):
	print(mo.group(i))

## Matching Optional
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())
print(mo2.group())

## Matching Zero/One or More
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
mo2 = batRegex.search('The Adventures of Batwoman')
mo3 = batRegex.search('The Adventures of Batwowowowowowoman')
print(mo1.group())
print(mo2.group())
print(mo3.group())
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batman')
mo2 = batRegex.search('The Adventures of Batwoman')
mo3 = batRegex.search('The Adventures of Batwowowowowowoman')
print("mo1 does not find the regex {} in Batman: {}".format(batRegex, mo1 == None))
print(mo2.group())
print(mo3.group())

## (non)Greedy Matching
greedyHaRegex = re.compile(r'(Ha){3,5}')
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
haSearch = 'HaHaHaHaHaHa'
mo1 = greedyHaRegex.search(haSearch)
mo2 = nongreedyHaRegex.search(haSearch)
print("mo1 evaluates to: " + mo1.group())
print("mo2 evaluates to: " + mo2.group())

## finall()
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo)
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo)

## Character Classes
xmasRegex = re.compile(r'\d+\s\w+')
TwelveDays = "12 drummers drumming, 11 pipers piping, 10 lords a-leaping, 9 ladies dancing, 8 maids a-milking, 7 swans a-swimming, 6 geese a-laying, 5 rings of gold, 4 birds a-calling, 3 hens of France, 2 turtleDoves, 1 partridge in a pear tree"
mo = xmasRegex.findall(TwelveDays)
print(mo)

text = 'RoboCop eats baby food. BABY FOOD.'
consonantRegex = re.compile(r'[aeiouAEIOU]')
mo1 = consonantRegex.findall(text)
consonantRegex = re.compile(r'[^aeiouAEIOU]')
mo2 = consonantRegex.findall(text)
print("In the following '{}', vowels are: {}".format(text, mo1))
print("In the following '{}', vowels are not: {}".format(text, mo2))

## Match Wildcard
text = 'The cat in the hat sat on the flat mat.'
atRegex = re.compile(r'.at')
mo = atRegex.findall(text)
print("In the phrase:\n'{}'\nwords matching:\n{} \nare the follwing: \n{}".format(text, atRegex,mo))
#passing re.DOTALL as a argument in re.compile will match newline characters as well. 
text = 'Serve the public trust.\nProtect the innocent.\nUphold the law.'
newlineRegex = re.compile(r'.*', re.DOTALL)
mo = newlineRegex.search(text)
print(mo.group())

## Case Sensitivity
text = 'RoboCop is part man, part machine, all cop.'
roboRegex = re.compile(r'robocop', re.I)
mo = roboRegex.search(text)
print(mo.group())
text = 'ROBOCOP protects the innocent.'
mo = roboRegex.search(text)
print(mo.group())
text = 'Al, why does your programming book talk about robocop so much?'
mo = roboRegex.search(text)
print(mo.group())


### Substitution
namesRegex = re.compile(r'Agent \w+')
sub = namesRegex.sub('CESNORED', 'Agent Alice gave the secred documents to Agent Bob.')
print(sub)
agentNamesRegex = re.compile(r'Agent (\w)\w*')
sub = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(sub)

### Complex RegEx Management

phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))?				# area code
	(\s|-|\.)?								# separator
	\d{3} 										# first 3 digits
	(\s|-|\.)									# separator
	\d{4}											# last 4 digits
	(\s*(ext|x|ext.)\s*\d{2,5})? # extension
)''', re.VERBOSE)
