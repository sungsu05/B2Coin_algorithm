n = int(input()) 

is_dancing = False 
for i in range(n):
    person1, person2 = input().split()

    if "ChongChong" in (person1, person2): 
        if is_dancing: 
            is_dancing = False 
        else: 
            is_dancing = True 

print(sum(1 for i in range(n) if "ChongChong" in input().split()) - 2 if is_dancing else 0)
