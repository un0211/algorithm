croatia_chars = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']


croatia_str = input()
for c in croatia_chars:
    croatia_str = croatia_str.replace(c, ' ')

print(len(croatia_str))