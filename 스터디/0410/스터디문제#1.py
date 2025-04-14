import math
def solution(cards):

    colors = [card[0] for card in cards]  # card[0]은 색깔을 의미([0]은 첫번째)
    numbers = [int(card[1]) for card in cards] # card[1]은 숫자을 의미([1]은 두번째)
    total = sum(numbers)                  # sum()함수는 리스트에 들어있는 숫자 더하기
    unique_colors = set(colors)            # set()은 리스트 안에 중복되는것들을 없애주는 자료형(색이 몇개중복되는지 확인가능)

    if len(unique_colors) == 1:
        return total * 3                    # set크기가 1 -> 색이 모두 같으면 총합 *3
    elif len(unique_colors) == 2:          # " 2 -> 2가지색이 같고 한가지가 다르면 *2
        return total * 2                    # " 3 -> 색이모두 다르면 총합만
    else:
        return total


    answer = 0
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
cards1 = [["blue", "2"], ["red", "5"], ["black", "3"]]
ret1 = solution(cards1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

cards2 = [["blue", "2"], ["blue", "5"], ["black", "3"]]
ret2 = solution(cards2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")