# 붙임성 좋은 총총이 https://www.acmicpc.net/problem/26069

"""
Test CASE

INPUT
12
bnb2011 chansol
chansol chogahui05
chogahui05 jthis
jthis ChongChong
jthis jyheo98
jyheo98 lms0806
lms0806 pichulia
pichulia pjshwa
pjshwa r4pidstart
r4pidstart swoon
swoon tony9402
tony9402 bnb2011

OUTPUT
10

"""
import sys
corona = ["ChongChong"]
str = ""
for i in range(int(input())):
    str = sys.stdin.readline().rstrip().split(' ')
    if str[0] in corona:
        corona.append((str[1]))
    elif str[1] in corona:
        corona.append((str[0]))

print(len(set(corona)))