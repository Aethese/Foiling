'''
foils a number like `(3, 4) * (2, 6)`. please read
through the limitations of this project on the README
under the `Limitations` subheader
'''

__version__ = '2.0.0-b1'
SUPERSCRIPT_TWO = f'\N{SUPERSCRIPT TWO}'      # ^2
SUPERSCRIPT_THREE = f'\N{SUPERSCRIPT THREE}'  # ^3


class IncorrectInput(Exception):
	'''incorrect raw input is passed'''
	pass


def _filter_input(raw_input: str) -> tuple:
	'''
	filters the input. the input will look something like
	this: `(3, 4) * (2, 6)` or `(3 + 4) * (2 + 6)`  what i need to change this to
	is: `(3+4)(2+6)`

	Parameters
	----------
	raw_input : str
		input given by the user. will look something like
		this: `(3, 4) * (2, 6)`

	Returns
	-------
	(first_coord, second_coord) : tuple
		returns a tuple with the first coord (str) is stored
		in the first position, while the second coord (str)
		is stored in the second position
	'''
	#=- start doing checks before we filter -=#
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

	return (first_coord, second_coord)


def _foil_algebra(first_nums: tuple, second_nums: tuple) -> str:
	'''
	foils an equation except for algebraic expressions

	example dict for all numbers are as defined:
	{NUMBER(str), HAS_X(bool), SUPERSCRIPT(int)}
	'''
	...


def foil(equation: str) -> float:
	'''
	foils an equation. the equation given will look
	like this unfiltered: `(3, 4) * (2, 6)`. the end
	goal is to return a float of that equation being
	foiled

	Returns
	-------
	foiled_value : float
		returns a float value if not an algebra equations
	algebra_foiled_value : str
		returns a string of the foiled value
	'''
	if not isinstance(equation, str):
		raise ValueError('Equation must be a string')

	algebra_equation = False
	if 'x' in equation: algebra_equation = True  # only look for x (at least for now)

	filtered_equation: tuple = _filter_input(equation)
	first_nums: str = filtered_equation[0]  # str of first nums
	second_nums: str = filtered_equation[1]

	# nums will look like this: (X,Y)
	first_nums_split: tuple = first_nums.split(',')  # tuple of first nums
	second_nums_split: tuple = second_nums.split(',')

	if algebra_equation:  # if algebra equation just solve it all here
		algebra_solved_value = _foil_algebra(first_nums_split, second_nums_split)
		return algebra_solved_value

	# first coord
	#                                    v   all numbers past (
	first_num1 = int(first_nums_split[0][1:])
	#              all numbers ahead of )   v
	second_num1 = int(first_nums_split[1][:-1])

	# second coord
	first_num2 = int(second_nums_split[0][1:])
	second_num2 = int(second_nums_split[1][:-1])

	foiled_one = (first_num1 * first_num2) + (first_num1 * second_num2)
	foiled_two = (second_num1 * first_num2) + (second_num1 * second_num2)

	return float(foiled_one + foiled_two)
