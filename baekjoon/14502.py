import copy

# input: map (N * M array, 0: empty, 1: wall, 2: virus)
# propagate virus from virus area to empty area
# if there is no wall around them
# return: modified map
def propagate_virus(virus_map, N, M):

    def check_empty(pos):
        x, y = pos

        if virus_map[y][x] == '0':
            return True
        return False
    
    def set_virus(pos):
        x, y = pos
        virus_map[y][x] = '2'
    

    virus_pos_list = []

    # add initial virus position info
    for y, row in enumerate(virus_map):
        str_row = ''.join(row)
        x = str_row.find('2')
        while x != -1:
            virus_pos_list.append((x, y))
            x = str_row.find('2', x+1)
    
    # propagate virus to left, up, right, down
    while virus_pos_list != []:
        x, y = virus_pos_list.pop()

        left = (x-1, y)
        up = (x, y-1)
        right = (x+1, y)
        down = (x, y+1)

        if x > 0 and check_empty(left):  # check left
            set_virus(left)
            virus_pos_list.append(left)
        if y > 0 and check_empty(up):  # check up
            set_virus(up)
            virus_pos_list.append(up)
        if x < M-1 and check_empty(right):  # check right
            set_virus(right)
            virus_pos_list.append(right)
        if y < N-1 and check_empty(down):  # check down
            set_virus(down)
            virus_pos_list.append(down)


# input: map (N * M array, 0: empty, 1: wall, 2: virus)
# calculate safe area (number of empty)
# return: area of safe area (integer)
def calculate_safe_area(virus_map):
    safe_area = 0

    for row in virus_map:
        safe_area += row.count('0')
    
    return safe_area


def idx_to_pos(idx):
    global M

    y = idx // M
    x = idx % M

    return (x,y)


def add_wall(idx):
    global wall_idx_list
    global virus_map

    wall_idx_list.append(idx)
    x, y = idx_to_pos(idx)
    virus_map[y][x] = '1'


def pop_wall():
    global wall_idx_list
    global virus_map

    idx = wall_idx_list.pop()
    x, y = idx_to_pos(idx)
    virus_map[y][x] = '0'

    return idx


max_safe_area = 0
wall_idx_list = []
idx = -1

# get input
N, M = (int(x) for x in input().split())
virus_map = [ input().split() for x in range(N) ]

# set initial wall
shrinked_map = ''.join([''.join(row) for row in virus_map])
for i in range(3):
    idx = shrinked_map.find('0', idx + 1)
    add_wall(idx)

while len(wall_idx_list) == 3:
    # propagate virus and calculate safe area
    propagated_map = copy.deepcopy(virus_map)
    propagate_virus(propagated_map, N, M)
    max_safe_area = max(max_safe_area, calculate_safe_area(propagated_map))

    del propagated_map

    # move one step
    idx3 = pop_wall()
    new_idx3 = shrinked_map.find('0', idx3 + 1)
    if new_idx3 != -1:  # Hww.. idx3 move one step
        add_wall(new_idx3)
        continue

    idx2 = pop_wall()
    new_idx2 = shrinked_map.find('0', idx2 + 1)
    if new_idx2 != -1:
        new_idx3 = shrinked_map.find('0', new_idx2 + 1)
        if new_idx3 != -1:  # idx2 move one step, and reset idx3
            add_wall(new_idx2)
            add_wall(new_idx3)
            continue
    
    idx1 = pop_wall()
    new_idx1 = shrinked_map.find('0', idx1 + 1)
    new_idx2 = shrinked_map.find('0', new_idx1 + 1)
    new_idx3 = shrinked_map.find('0', new_idx2 + 1)
    if new_idx1 != -1 and new_idx2 != -1 and new_idx3 != -1:
        # idx1 move one step, and reset idx2, idx3
        add_wall(new_idx1)
        add_wall(new_idx2)
        add_wall(new_idx3)

print(max_safe_area)