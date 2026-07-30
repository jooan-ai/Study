import random


# 데코레이터 (decorator)
# - 여러 개의 함수 호출 전/후로 공통된 로직이 필요할 때 활용
# - 예시) 로그인 체크, 보안 체크 등등
# - 직접 만들 일은 별로 없지만, 다른 사람들의 코드에서 많이 보임

# 행동 전/후 손소독 데코레이터
def clean_decorator(func):
    def wrapper(*args, **kwargs):
        print("[시작 전] 손소독을 진행합니다.")
        func(*args, **kwargs)
        print("[종료 후] 손소독을 진행합니다.")

    return wrapper

# class == 설계도
class Doctor:
    # 클래스 변수
    # - 모든 인스턴스가 같은 값을 공유
    hospital_name = "한국대학교병원"
    doctors = []  # 모든 의사 목록

    # 설계도에 작성해야 하는 것들
    # 데이터 (변수)
    # 행동 (method, 메서드)

    # 생성자 매직 메서드
    # 저장하고 싶은 데이터를 생성자에서 모두 초기화
    # - 이름(name)
    # - 과(department)
    # - 명성치(reputation)
    # self: 인스턴스 자기자신
    def __init__(self, name, department, success_rate):
        # 인스턴스 변수 3개
        self.name = name
        self.department = department
        self.reputation = 0
        # [미션] 수술 성공 확률
        self.success_rate = success_rate
        # doctors 클래스 변수에 추가
        Doctor.doctors.append(self)

    # 인스턴스 메서드
    # - "누군가" 수술을 시작합니다.
    # - 특징: 첫 번째 파라미터는 인스턴스 자기자신
    @clean_decorator
    def surgery(self):
        print(f"{self.name} 의사가 수술을 시작합니다.")
        # [미션] 수술 성공 확률 적용하기
        if random.randint(1, 100) <= self.success_rate:
            self.reputation += 10
            print("수술 성공!")
        else:
            self.reputation -= 10
            print("수술 실패!")
        print(f"현재 명성치는 {self.reputation} 입니다.")

    @clean_decorator
    def check(self):
        print(f"{self.name} 의사가 진료를 시작합니다.")

    # doctors 클래스 변수를 출력
    # - 명성치로 내림차순 출력
    # 클래스 메서드
    # - 특징: 첫 번째 파라미터는 클래스 자기자신
    @classmethod
    def show_ranking(cls):
        # TODO: 명성치(reputation) 기준으로 내림차순 구현
        ranking = sorted(cls.doctors, key=lambda x : x.reputation, reverse=True)

        # 인덱스와 데이터를 함께 사용하고 싶다. (1위: 누구 / 2위: 누구)
        # --> enumerate
        for idx, doctor in enumerate(ranking, start=1):
            print(f"{idx}위: {doctor.name} ({doctor.reputation})")
        

# 설계도를 기반으로 실제 데이터를 찍어낸다.
# 객체(Object): 실제 데이터를 가지고 있는 변수
# 인스턴스(Instance): 클래스를 통해서 찍어낸 객체
# ()가 있네 ? == 함수를 호출한다.
# --> "생성자" 메서드가 호출된다.
doctor1 = Doctor("백강혁", "외상외과", 100)  
doctor2 = Doctor("양재원", "항문외과", 75)
doctor3 = Doctor("한유림", "항문외과", 60)

# 클래스.클래스변수 --> 권장
print(f"{Doctor.hospital_name}에 오신 걸 환영합니다")

# 인스턴스.클래스변수 --> 쓰지 마세요!!!
# print(doctor1.hospital_name)

print(doctor1.name)
print(doctor2.name)
print(doctor3.name)

doctor1.surgery()
doctor1.surgery()
doctor1.surgery()
doctor1.surgery()
doctor1.surgery()
doctor2.surgery()
doctor2.surgery()
doctor2.surgery()
doctor2.surgery()
doctor2.surgery()
doctor3.surgery()
doctor3.surgery()
doctor3.surgery()
doctor3.surgery()
doctor3.check()

Doctor.show_ranking()