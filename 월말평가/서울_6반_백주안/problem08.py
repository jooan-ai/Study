############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def find_common(list_a, list_b):
    list_a = list(set(list_a)) # 리스트 a, b를 set 형태로 변환해 중복값을 제거하고, 다시 list로 만들어줍니다.
    list_b = list(set(list_b))
    list_c = [] # 교집합값을 입력할 list_c를 만듭니다. 
    for i in list_a: # list_a를 순회하며 나오는 i 값이 list_b에 있다면, list_c에 추가합니다.
        if i in list_b:
            list_c.append(i)
    return list_c # list_c를 반환합니다.

    # 여기에 코드를 작성하여 함수를 완성합니다.

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(find_common([1, 2, 3, 4, 5], [2, 4, 6, 4]))                      # [2, 4]
print(find_common(['apple', 'banana', 'cherry'], ['cherry', 'apple', 'grape']))  # ['apple', 'cherry']
#####################################################
