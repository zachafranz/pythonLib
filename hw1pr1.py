'''Name: Zach Franz
hw1pr1.py (Lab 1, part 1) slicing and indexing challenge
'''
pi = [3, 1, 4, 1, 5, 9]
e = [2, 7, 1]

answer1 = [e[1],pi[1]]
print(answer1)

answer2 = [9,e[-1],pi[3]]
print(answer2)

answer3 = [e[-1],pi[2],e[-1],pi[-2],pi[-1]]
print(answer3)

answer4 = [e[-1],e[0],pi[0],pi[2],pi[-2]]
print(answer4)


h = 'harvey'
m = 'mudd'
c = 'college'

answer5 = c[0:4]+m[1:3]+c[-1]
print(answer5)

answer6 = h[1:]+m[1:]
print(answer6)

answer7 = h[0:3] + m[-1] + c[-1] + 3*h[0:3]
print(answer7)

answer8 = c[3:6] + c[1] + m[0] + h[-1] + c[4:6] + c[1]
print(answer8)

answer9 = c[0] + c[3:5] + h[1:3] + c[0] + h[1] + c[2:4]
print(answer9)
