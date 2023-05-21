# https://www.acmicpc.net/problem/25372
# 성택이의 은밀한 비밀번호



print("\n".join(["yes" if len(x:=input()) >= 6 and len(x) <= 9 else "no" for _ in range(int(input()))]))