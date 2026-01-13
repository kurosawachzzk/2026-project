import time

print("올해 나의 나이는?")
year = int(input("현재는 몇년도인가요?"))
year2 = int(input("내가 태어난 년도는 몇년도인가요?"))
print("나이 계산중입니다...")
time.sleep(3)
age= year - year2 +1 
print("내 나이는 : ",age)
