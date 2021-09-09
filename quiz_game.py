# 입력문과 조건문을 이용하여 퀴즈 게임을 만들고, 점수를 계산한다.
print("Welcome to my computer quiz! ")

# playing을 입력변수로 받아 yes가 입력되지 않으면 quiz_game을 종료한다.
playing = input("Do you want to play? Please answer yes or no ")
# 입력받은 문자가 대문자, 소문자 관계없이 모두 lower case(소문자)로 변경한다.
if playing.lower() != "yes":
    quit()

print("Okay! Let's play :) ")
# 시작 점수는 0으로 설정한다.
score = 0

# 첫 번째 퀴즈 CPU의 의미는?
answer = input("What dose CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    # 문제를 맞출경우 기존 점수에 1을 더한다. score = score + 1 과 같은 의미
    score += 1
else:
    print("Incorrect!")

# 두 번째 퀴즈 GPU의 의미는?
answer = input("What dose GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# 세 번째 퀴즈 RAM의 의미는?
answer = input("What dose RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# 네 번째 퀴즈 ROM의 의미는?
answer = input("What dose ROM stand for? ")
if answer.lower() == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# 다섯 번째 퀴즈 PSU의 의미는?
answer = input("What dose PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# 퀴즈가 끝난 후 참여자의 최종 점수를 알려준다.
#문자열과 정수형을 연결하기 위해 정수형을 문자열로 바꾸어준다.
print("You got " + str(score) + " questions correct!")
# 퀴즈가 끝난 후 참여자의 최종 정답률을 알려준다.
# 점수를 문제 갯수로 나눈 후 100을 곱한다.
print("You got " + str((score/5) * 100) + "%.")
