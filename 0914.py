# 우리반 친구들 리스트를 만들어봐요.
#리스트
friends = ["래현", "민호", "헌서"]

# append로 새로운 친구 '재청'를 추가해요.
friends.append("재청")

print("우리반 친구는 총", len(friends), "명 입니다.") # len으로 총 몇 명인지 확인

# for문으로 친구들 이름을 한 명씩 불러줘요.
#오른쪽 집합중 순차적으로 하나씩 가져오는 기능을 수행 iteator
for friend in friends:
    print(friend, "안녕!")