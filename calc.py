import random

num1 = random.randint(1, 99)
num2 = random.randint(1, 99)

result = num1 + num2
answer = 0


while answer != result:
    try:
        answer = int(input(f"{num1} + {num2} = "))

        if answer == result:
            print("정답입니다.")
        else:
            print("틀렸습니다. 다시 시도하세요.")

    except ValueError:
        print("잘못된 입력입니다.")
        exit()
