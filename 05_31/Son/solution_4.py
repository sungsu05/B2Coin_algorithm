def test(**kwargs):
    print(kwargs)


arr = [1,2,3,4]
test(*arr)

# # AC https://www.acmicpc.net/problem/5430
# import sys
#
# def solution(arr,func):
#     D,R = "D","R"
#     while len(func) != 0:
#         if func[0] == R:
#             index_D = func.find(D)
#             idnex_D = len(func) if index_D == -1 else index_D
#             temp = func[0:index_D]
#             arr = arr if len(temp)%2==0 else arr[::-1]
#             func = func[index_D:]
#
#         else:
#             index_R = func.find(R)
#             index_R = len(func) if index_R == -1 else index_R
#             arr = arr[index_R:]
#             func = func[index_R:]
#     return arr
#
#
# for i in range(int(input())):
#     func = input()
#     n = int(input())
#     arr = eval(input())
#     if cnt := func.count('D') >= n :
#         print(0 if cnt == 0 else 'error')
#     else:
#         print(solution(arr,func))
#
#


