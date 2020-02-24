a = \
	'(asciitree (sometimes you) (just (want to draw)) trees (in (your terminal)))'


def mover(inp):
	b = inp.replace('(', '( ').replace(')', ' )').split(' ')[1:-1]
	count = 0
	cort = []
	description = False
	for el in b:
		if el != '(' and el != ')' and not description:
			cort.append((count, el))
			description = True
			count += 1
		elif el == '(':
			count += 1
		elif el == ')':
			count -= 1
		else:
			cort.append((count, el))
	return cort


print(mover(a))
