'''
Given: Two DNA strings.

Return: An integer value representing the Hamming distance.
'''

def hamming(string1,string2):
  hamming = 0

  for i in zip(string1, string2):
    if i[0] != i[1]:
      hamming += 1

  return hamming
