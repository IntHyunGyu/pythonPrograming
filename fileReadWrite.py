try:
    with open("data.txt","w") as f:
        for i in range(5):
            f.write(input(str(i+1) + "번째 숫자를 입력하세요 : ") + "\n")

    with open("data.txt","r") as f:
        sum = 0
        for line in f:
            sum = sum + int(line)

    print('다섯 숫자의 합 = {}, 평균 = {}'.format(sum, sum / 5))
except FileNotFoundError:
    print("파일이 존재하지 않습니다.")
except Exception as e:
    print(e)

