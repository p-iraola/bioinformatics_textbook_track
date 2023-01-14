'''
Given: A DNA string Pattern.

Return: Pattern, the reverse complement of Pattern.
'''

def reverse_compliment(string1):
	string2 = ''
	for i in string1[::-1]:
		if i == 'A':
			string2 += 'T'
		if i == 'T':
			string2 += 'A'
		if i == 'C':
			string2 += 'G'
		if i == 'G':
			string2 += 'C'
	return(string2)
