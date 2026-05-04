
import random

# 1. 컴퓨터가 1~50 사이의 숫자를 생각한다
computer_number = random.randint(1, 50)
print("컴퓨터가 1부터 50 사이의 숫자를 하나 선택했습니다!")

# 5. 7번 반복 (기회는 총 7번)
for i in range(1, 8):
    # 2. 사용자 숫자 입력
    user_guess = int(input(f"{i}번째 시도 - 숫자를 입력하세요: "))
    
    # 3. 숫자가 맞으면 사용자 승리
    if user_guess == computer_number:
        print(f"정답입니다! {i}번 만에 맞추셨네요. 당신의 승리!")
        break
    
    # 4. 틀리면 Up/Down 힌트 제공
    elif user_guess < computer_number:
        print("UP! 더 큰 숫자를 생각해보세요.")
    else:
        print("DOWN! 더 작은 숫자를 생각해보세요.")

# 6. 7번 안에 못 맞추면 컴퓨터 승리
else:
    print("-" * 30)
    print(f"아쉽습니다. 모든 기회를 다 썼어요. 컴퓨터 Win!")
    print(f"정답은 {computer_number}였습니다.")