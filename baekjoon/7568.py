ranks = []
sizes = []

for i in range(int(input())):
    my_size = [int(x) for x in input().split()]
    my_rank = 1

    for idx, size in enumerate(sizes):
        if size[0] > my_size[0] and size[1] > my_size[1]:
            my_rank += 1
        elif size[0] < my_size[0] and size[1] < my_size[1]:
            ranks[idx] += 1
    
    ranks.append(my_rank)
    sizes.append(my_size)

print(' '.join(list(map(lambda x: str(x), ranks))))
