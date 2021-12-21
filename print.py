#print


# pfing
print('hi')
print("hi")
print("""hi""")
print('''hi''')

print()
# separator

print('1','2','3', sep=',')
print('1','2','3', end=' ')
print()

# format
print('{} and {}'.format('A','B'))
print('{0} and {1}'.format('A','B'))
print('{a} and {b}'.format(a='A', b='B'))
print()

import sys
print(sys.stdin.encoding)