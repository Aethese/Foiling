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
if equation == 66.0:
	print('Test 2 passed')
else:
	print('Test 2 failed! Got %s expected %s' % (equation, '66.0'))
	failed += 1

equation = foiling.foil('(13, 15) *(13,28)')
if equation == 1148.0:
	print('Test 3 passed')
else:
	print('Test 3 failed! Got %s expected %s' % (equation, '1148.0'))
	failed += 1


if failed >= 1:
	print(f'{failed} tests failed!')
	os._exit(1)
else:
	print('All tests passed!')
	os._exit(0)
