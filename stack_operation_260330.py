stack = []
capacity = 5

# 함수 사용 형식
# def 함수명 (매개변수1, 매개변수2 ...):
#     알고리즘 코드

def isFull():
    if len(stack) == capacity:
        return True
    else:
        return False

def isEmpty():
    if len(stack) == 0:
        return True
    else:
        return False

def push(data):
    if isFull():
        print('stack이 차 있어서 더이상 추가할 수 없습니다')
    else:
        stack.append(data)

def pop():
    if isEmpty():
        print('Stack이 비어있습니다')
        return -1
    else:
        return stack.pop()


def peek():
    if isEmpty():   # False일때 if문 아래 실행 = stack(바구니)가 텅비어있을때
        print('stack이 비어 있습니다')
    else:
        print('가져올 데이터 : ', stack[len(stack)-1])

    
  
#=========================================================================
print(f'[[ 정수영 스택 연산 실습 (용량 : {capacity})]]')

while True:
    print('=============================')
    print('1.push 2.pop 3.peek 0.Exit')
    print('=============================')
    menu = int(input('> 메뉴 선택 : '))
    if menu == 0:
        break
    elif menu == 1:
        data = int(input('데이터 입력'))
        push(data)
    elif menu == 2:
        data = pop()
        print(data)
    elif menu == 3:
        peek()
    
    
    print('> 현재 스텍 상태', stack)

print('[[ 정수형 스택 연산 실습 종료]]')