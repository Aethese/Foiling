import foiling, os
os.system('cls' if os.name=='nt' else 'clear')

print('Running foiling version', foiling.__version__)
failed = 0

filtered_input = foiling._filter_input('(1, 7) * (4, 8)')
if filtered_input == ('(1,7)', '(4,8)'):
	print('Test 1 passed')
else:
	print('Test 1 failed! Got %s expected %s' % (filtered_input, '((1,7), (4,8))'))
	failed += 1

equation = foiling.foil('(1, 5) *(3,8)')
solved_value = 66.0
if equation == solved_value:
	print('Test 2 passed')
else:
	print('Test 2 failed! Got %s expected %s' % (equation, str(solved_value)))
	failed += 1

equation = foiling.foil('(13, 15) *(13,28)')
solved_value = 1148.0
if equation == solved_value:
	print('Test 3 passed')
else:
	print('Test 3 failed! Got %s expected %s' % (equation, str(solved_value)))
	failed += 1

equation = foiling.foil('(4, -2)(2, 1)')
solved_value = 6.0
if equation == solved_value:
	print('Test 4 passed')
else:
	print('Test 4 failed! Got %s expected %s' % (equation, str(solved_value)))
	failed += 1

algebra_equation = foiling.foil('(3x,2) * (x,7)')
solved_value = f'3x\N{SUPERSCRIPT TWO}+23x+14'
if algebra_equation == solved_value:
	print('Test 5 passed')
else:
	print('Test 5 failed! Got %s expected %s' % (algebra_equation, solved_value))
	failed += 1

equation = foiling.foil('(1.5, 0.5) (2.25, 1)')
solved_value = 6.5
if equation == solved_value:
	print('Test 6 passed')
else:
	print('Test 6 failed! Got %s expected %s' % (equation, solved_value))
	failed += 1

equation = foiling.foil('(1)()')


if failed >= 1:
	print(f'\n{failed} tests failed!')
	os._exit(1)
else:
	print('\nAll tests passed!')
	os._exit(0)
