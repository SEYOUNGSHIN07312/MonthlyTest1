# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
# python 내장함수 min, max 사용 금지
def min_max(scores):
    min_score = 100
    max_score = 0

    for i in range(len(scores)):
        if scores[i] > max_score:
            max_score = scores[i]
        
        if scores[i] < min_score:
            min_score = scores[i]

    return min_score, max_score

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    scores = [80, 90, 85, 75]
    print(min_max(scores))    # (75, 90)
