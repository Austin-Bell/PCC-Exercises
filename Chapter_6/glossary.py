# Think of five programming words you learned. Print each word and its meaning as neatly formatted output.
"""
glossary = {
	'variable': 'A variable stores a datatype',
	'list': 'A list stores mutiple data types',
	'if_statement': 'An if statement can evaluate a statement to see if its true or false.',
	'python': 'A computer programming language that is used in web development and data analysis',
	'for_loop': 'A for loop allows you to manipulate mutiple items in a list'
}

print('variable: ' + glossary['variable'])
print('\nlist: ' + glossary['list'])
print('\nif statement: ' + glossary['if_statement'])
print('\npython: ' + glossary['python'])
print('\nfor loop: ' + glossary['for_loop'])
"""

glossary = {
	'variable': 'A variable stores a datatype',
	'list': 'A list stores mutiple data types',
	'if statement': 'An if statement can evaluate a statement to see if its true or false.',
	'python': 'A computer programming language that is used in web development and data analysis',
	'for_loop': 'A for loop allows you to manipulate mutiple items in a list'
}


for key, value in glossary.items():
	print("\n " + key.title() + ": " + value)
