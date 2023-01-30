# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def is_position_safe(N, M, position):
    new_pos = [position[0], position[1]]

    if M == 0:
        new_pos[0] -= 1
    elif M == 1:
        new_pos[0] += 1
    elif M == 2:
        new_pos[1] -= 1
    else:
        new_pos[1] += 1

    if new_pos[0] < 0 or new_pos[0] >= N or new_pos[1] < 0 or new_pos[1] >= N:
        return False
    else:
        return True

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(is_position_safe(3, 1, (0, 0)))  # True
    print(is_position_safe(3, 0, (0, 0)))  # False
