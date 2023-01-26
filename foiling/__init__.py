__version__ = '0.0.1'

def _filter_input(input: str) -> str:
	'''
	filters the input. the input will look something like
	this: `(3, 4) * (2, 6)`  what i need to change this to
	is: `(3,4)(2,6)`

	Parameters
	----------
	input : str
		input given by the user. will look something like
		this: `(3, 4) * (2, 6)`
	'''
	return ''