# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def caesar(word, n):
    word_list = []

    for i in range(len(word)):

        if word[i] >= 'A' and word[i] <= 'Z':
            if ord(word[i]) + n > 90:
                word_list.append(chr(ord(word[i]) - 26 + n))
            else:
                word_list.append(chr(ord(word[i]) + n))

        elif word[i] >= 'a' and word[i] <= 'z':
            if ord(word[i]) + n > 122:
                word_list.append(chr(ord(word[i]) - 26 + n))
            else:
                word_list.append(chr(ord(word[i]) + n))

    reverse_word = ""

    for i in word_list:
        reverse_word += i

    return reverse_word


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(caesar('apple', 5))      # fuuqj
    print(caesar('ssafy', 1))      # ttbgz
    print(caesar('Python', 10))    # Zidryx
