n = int(input())  # 수의 개수 N 입력받기
numbers = list(map(int, input().split()))  # N개의 수 입력받아 리스트에 저장하기

# 에라토스테네스의 체 알고리즘으로 소수 찾기
x = [True] * 1001  # 1부터 1000까지 소수 판별을 위한 리스트 생성
x[0], x[1] = False, False  # 0과 1은 소수가 아니므로 False로 처리

for i in range(2, 1001):
    if x[i]:  # i가 소수인 경우
        for j in range(2*i, 1001, i):  # i의 배수 모두에 대해 False로 처리
            x[j] = False

# 주어진 수들 중에서 소수의 개수 찾기
count = 0
for num in numbers:
    if x[num]:  # 해당 수가 소수인 경우
        count += 1

print(count)  # 소수의 개수 출력하기




# M(시작 수) N(종료 수)
# A(소수 배열)
# for(N만큼 반복하기) {
#     A 배열 초기화하기
# }
# for(N의 제곱근까지 반복하기)
#     소수가 아니면 넘어감
#     for(소수의 배수 값을 N까지 바복하기) {
#         이 수가 소수가 아니라는 것을 표시하기
#     }
# }
# for(M~N까지 반복하기){
#     A배열에서 소수인 값 출력하기
# }