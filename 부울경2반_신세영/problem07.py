# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def calculator(*numbers):

    if len(numbers) == 1:
        return numbers[0] * numbers[0] * 3.14
    elif len(numbers) == 2:
        if sum(numbers) % 2 == 1:
            return numbers[0] * numbers[1] / 2
        else:
            return numbers[0] * numbers[1]
    elif len(numbers) >= 3:
        sum_num = 0
        for i in range(len(numbers)):
            sum_num += numbers[i]
        return sum_num, (sum_num / len(numbers))
    else:
        return 0


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(calculator(5))                # 78.5
    print(calculator(10, 20))           # 200
    print(calculator(10, 20, 30, 40))   # (100, 25.0)
    print(calculator())                 # 0