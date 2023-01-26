import foiling, os
os.system('cls' if os.name=='nt' else 'clear')

failed = 0

if foiling._filter_input('(1, 7) * (4, 8)') == '(1,7)(4,8)':
	print('Test 1 passed')
else:
	print('Test 1 failed!')
	failed += 1


if failed >= 1:
	print(f'{failed} tests failed!')
	os.exit(1)
else:
	print('All tests passed!')
	os.exit(0)
