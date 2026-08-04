############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 제한 내장 함수:  len
# 기본 점수 (9점): 제한 내장 함수를 사용하여 해결
# 가산점(+3점): 제한 내장 함수 없이 직접 구현 (총 12점)

def count_long_names(names, min_length):
    # 여기에 코드를 작성하여 함수를 완성합니다.

    count = 0 # 특정 길이 이상인 닉네인 개수를 카운트 할 변수를 만듭니다.
    for word in names: # names의 각 항목의 글자 수를 조회하며 word_count로 개수를 세어줍니다. 
        word_count = 0
        for _ in word:
            word_count += 1
        if word_count >= min_length : #글자 수가 min_length보다 길면 count를 1 증가시킵니다.
            count += 1

    return count # 최종 카운트 값을 반환합니다.

        



# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(count_long_names(['kim', 'developer', 'ssafy', 'a'], 5))  # 2 ('developer', 'ssafy')
print(count_long_names(['a', 'bb', 'ccc'], 5))                  # 0
#####################################################
