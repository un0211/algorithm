def array_to_string(arr):
    arr_str = "["
    arr_str += ",".join([str(n) for n in arr])
    arr_str += "]"

    return arr_str


for _ in range(int(input())):
    p = input()
    n = int(input())

    num_D = p.count('D')

    if num_D > n:
        input()
        print('error')
        continue

    if num_D == n:
        input()
        print('[]')
        continue

    arr = [int(x) for x in input().strip("[]").split(",")]

    error = False
    isReverse = False
    start = 0
    end = n

    for func in p:
        if func == 'R':
            isReverse = not isReverse
            continue

        if isReverse:
            end -= 1
        else:
            start += 1

    answer = arr[start : end]
    if isReverse:
        answer.reverse()
    
    print(array_to_string(answer))
