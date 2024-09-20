'''
author: Adam Thomson
PHY 571 Coding Assignment 1

Exercise 2.7: Catalan numbers
The Catalan numbers Cn are a sequence of integers 1, 1, 2, 5, 14, 42, 132. . . that play
an important role in quantum mechanics and the theory of disordered systems. (They
were central to Eugene Wigner’s proof of the so-called semicircle law.) They are given by
C0 = 1, Cn+1 = ((4n + 2)/(n + 2))*Cn
Write a program that prints in increasing order all Catalan numbers less than or equal
to one billion.
'''

# Loop to calculate the next value in sequence
def _next_catalan(prev, n):
    return (((4*n) + 2)/(n + 2)) * prev

print('Printing Catalan numbers less than a billion:')

# Initialize sequence
cat_nums = []
curr_cat = 1
curr_n = 0

# Use recursion to generate the sequence
while curr_cat < 1000000000:
    cat_nums.append(curr_cat)
    curr_cat = int(_next_catalan(curr_cat, curr_n))
    curr_n += 1

print(cat_nums)
