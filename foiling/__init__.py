__version__ = '0.0.1'

class IncorrectInput(Exception):
	'''incorrect raw input is passed'''
	pass

def _filter_input(raw_input: str) -> str:
	'''
	filters the input. the input will look something like
	this: `(3, 4) * (2, 6)`  what i need to change this to
	is: `(3,4)(2,6)`

	Parameters
	----------
	raw_input : str
		input given by the user. will look something like
		this: `(3, 4) * (2, 6)`
	'''
	#=- start doing checks before we filter -=#
	if not isinstance(raw_input, str):
		return TypeError('Input must be a string')

	if '(' not in raw_input:
		raise IncorrectInput('No coordinates found in raw input')

	para_count1: int = 0  # (
	para_count2: int = 0  # )
	for char in raw_input:  # see if 2 coords are passed
		if char == '(':
			para_count1 += 1
		if char == ')':
			para_count2 += 1
	if para_count1 != 2 or para_count2 != 2:
		raise IncorrectInput('Incorrect amount of coordinates passed. Limit is two')

	#=- attempt to separate the 2 coords -=#
	first_coord  = ''
	second_coord = ''

	for index_num in range(2):  # separate for first coord
		# if we want just 2nd coord, we will want to skip the first set of coords
		skipped_first_coord1 = False
		skipped_first_coord2 = False
		log = False  # if we're currently logging the string
		separate_coord = ''  # store a temp version of the separated string

		for char in raw_input:
			if char == '(':
				if (index_num + 1) == 2 and skipped_first_coord1 == False:
					# if we're trying to log the 2nd coord, we are going to want
					# to skip the first coord, which we do here
					skipped_first_coord1 = True
					continue

				log = True
			if log == True:
				separate_coord += char
			if char == ')':
				if (index_num + 1) == 2 and skipped_first_coord2 == False:
					# same idea when looking for (
					skipped_first_coord2 = True
					continue
				log = False
				break
		
		# now log our temp data to the finalized string
		if (index_num + 1) == 1:
			first_coord = separate_coord
		else:
			second_coord = separate_coord
	
	if ' ' in first_coord:
		split = first_coord.split(' ')
		first_coord = split[0] + split[1]
	if ' ' in second_coord:
		split = second_coord.split(' ')
		second_coord = split[0] + split[1]

	return f'{first_coord}{second_coord}'