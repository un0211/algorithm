def check_group_word(word):
    current_alphabet = word[0]

    for idx, char in enumerate(word):
        # 이전과 같은 글자가 연속됨. 그룹 글자 조건 만족
        if char == current_alphabet:
            continue
        
        # 새로운 글자 등장 시, 뒤에 더이상 이전 글자가 나오지 않아야 그룹글자임.
        if word.find(current_alphabet, idx) != -1:
            return False

        # 이전 글자가 조건을 만족하면, 새로 등장한 글자를 타겟으로 변경
        current_alphabet = char
    
    # 모든 글자가 조건을 만족하면 True 리턴.
    return True

num_of_words = int(input())
num_of_group_words = 0

for i in range(num_of_words):
    word = input()
    if check_group_word(word):
        num_of_group_words += 1

print(num_of_group_words)
