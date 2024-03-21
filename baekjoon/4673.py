def d(n):
    result = n

    # 각 자릿수 더하기
    while n > 0:
        result += (n % 10)
        n //= 10

    return result

not_self_number = [d(i) for i in range(1, 10000)]
self_number = [i for i in range(1, 10000) if i not in not_self_number]

for n in self_number:
    print(n)